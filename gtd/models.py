from django.db import models
from gtd import managers
from django.core.exceptions import ValidationError
from django.db.models import Sum
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.humanize.templatetags.humanize import naturalday
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

class Project(models.Model):
    """
    Projects are a set of 'things' that could be tasks, this indentify the
    progress as the sum of all task progress. So you can have a big picture of
    the advance of all the set of task.

    All projects are prefixed with '#'. A Project can have 'Things' (tasks)
    with diferent contexts.
    """
    name = models.CharField(_('name'), max_length=90)
    slug = models.SlugField(_('code'))
    description = models.TextField(_('description'), blank=True)
    active = models.BooleanField(_('active'), default=True)
    deadline = models.DateTimeField(_('deadline'), blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        get_latest_by = 'created'
        ordering = ['-created',]

    def __unicode__(self):
        return u"#%s" % self.slug

    @property
    def progress(self):
        things = self.thing_set.filter(deleted=False).exclude(status=Thing.STATE_INCUBATE)
        things_count = things.count()
        if things_count > 0 :
            return things.all().aggregate(Sum('progress'))['progress__sum'] / things_count
        else:
            return 0

    def get_progress(self):
        return u'%s%%' % (self.progress)
    get_progress.short_description = 'Progress'

    def get_progress_bar(self):
        return u'<div class="progress_bar"><span style="width: %spx">%s%%</span></div>' % (self.progress, self.progress)
    get_progress_bar.allow_tags = True
    get_progress_bar.short_description = 'Progress Bar'

    def thing_count(self):
        return self.thing_set.filter(deleted=False).count()
    thing_count.short_description = 'Things'

    def thing_todo_count(self):
        return self.thing_set.filter(status=Thing.STATE_ACTIONABLE, deleted=False).count()
    thing_todo_count.short_description = 'Things to do'

    def thing_done_count(self):
        return self.thing_set.filter(status=Thing.STATE_DONE, deleted=False).count()
    thing_done_count.short_description = 'Things done'

    def get_deadline(self):
        if self.deadline:
            return naturalday(self.deadline)
        else:
            return u''
    get_deadline.allow_tags = True
    get_deadline.short_description = 'Deadline'

class Context(models.Model):
    """
    Context is a categorization for task that describes if this is a tool,
    location or person that is required to be able to complete an action.

    Context are long term definitions, isn't the same as projects. A 'Thing'
    can just have one context, and couldb be involve (or not) in one project.
    A Project can have tasks in many context.
    """
    name = models.CharField(_('name'), max_length=90)
    slug = models.SlugField(_('code'))
    description = models.TextField(_('description'), blank=True)

    class Meta:
        ordering = ['slug']

    def __unicode__(self):
        return u"@%s" % self.slug

    def thing_count(self):
        return self.thing_set.filter(deleted=False).count()
    thing_count.short_description = 'Things'

    def thing_done_count(self):
        return self.thing_set.filter(status=Thing.STATE_DONE, deleted=False).count()
    thing_done_count.short_description = 'Things done'

    def thing_todo_count(self):
        return self.thing_set.filter(status=Thing.STATE_ACTIONABLE, deleted=False).count()
    thing_todo_count.short_description = 'Things to do'

def validate_progress(value):
    if value > 100 or value < 0:
        raise ValidationError(_(u'%s is not a valid progress value') % value)

def validate_schedule(value):
    if value < datetime.now() :
        raise ValidationError(_(u'Schedule date must be in future'))

class Thing(models.Model):
    STATE_THING = 1
    STATE_WAITING = 2
    STATE_ACTIONABLE = 3
    STATE_DELEGATED = 4
    STATE_DEFERRED = 5
    STATE_INCUBATE = 6
    STATE_DONE = 7

    STATES = (
        (STATE_THING, _('thing')),
        (STATE_WAITING, _('waiting')),
        (STATE_ACTIONABLE, _('actionable')),
        (STATE_DELEGATED, _('delegated')),
        (STATE_DEFERRED, _('deferred')),
        (STATE_INCUBATE, _('incubate')),
        (STATE_DONE, _('done')),
    )

    name = models.CharField(_('name'), max_length=140)
    description = models.TextField(_('description'), blank=True)
    status = models.IntegerField(_('status'), choices=STATES, default=STATE_THING)
    project = models.ForeignKey(Project, null=True, blank=True)
    context = models.ForeignKey(Context)
    deleted = models.BooleanField(_('deleted'), default=False)
    archived = models.BooleanField(_('archived'), default=False)
    progress = models.IntegerField(_('progress'), default=0, validators=[validate_progress])
    schedule = models.DateTimeField(_('schedule'), null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    focus = managers.FocusManager()

    class Meta:
        get_latest_by = 'created'
        ordering = ['-created',]

    def __unicode__(self):
        return u'%s : %s [%s]' % (self.context, self.name, self.get_status_display())

    def get_name(self):
        if self.deleted:
            return u'<del>%s</del>' % self.name
        elif self.status == self.STATE_DONE:
            return u'<span class="thing_done">%s</span>' % self.name
        else:
            return u'%s' % self.name
    get_name.allow_tags = True
    get_name.short_description = 'Thing'

    def get_project(self):
        if self.project:
            return u'<a href="%s">%s</a>' % (reverse('admin:gtd_project_change', args=[self.project.id]), self.project.name)
        else:
            return u''
    get_project.allow_tags = True
    get_project.short_description = 'Project'

    def get_context(self):
        return u'<a href="%s">%s</a>' % (reverse('admin:gtd_context_change', args=[self.context.id]), self.context.__unicode__())
    get_context.allow_tags = True
    get_context.short_description = 'Context'

    def get_progress(self):
        return u'<div class="progress_bar"><span style="width: %spx">%s%%</span></div>' % (self.progress, self.progress)
    get_progress.allow_tags = True
    get_progress.short_description = 'Progress'

    def get_reminders(self):
        return render_to_string('gtd/admin/reminders.html', dict(thing=self))
    get_reminders.allow_tags = True
    get_reminders.short_description = 'Reminders'

    def get_created(self):
        return naturalday(self.created)
    get_created.allow_tags = True
    get_created.short_description = 'Created'

    def save(self, *args, **kwargs):
        if self.schedule and not self.status in (self.STATE_DONE, ):
            self.status = self.STATE_DEFERRED
        if self.progress == 100:
            self.status = self.STATE_DONE
        elif self.status == self.STATE_DONE:
            self.progress = 100

        super(Thing, self).save(*args, **kwargs)

class Reminder(models.Model):
    UNIT_MINUTE = 1
    UNIT_HOUR = 2
    UNIT_DAY = 3

    UNITS = (
        (UNIT_MINUTE, _('minutes')),
        (UNIT_HOUR, _('hours')),
        (UNIT_DAY, _('days')),
    )

    METHOD_ALERT = 1
    METHOD_EMAIL = 2

    METHODS = (
        (METHOD_ALERT, _('flash alert')),
        (METHOD_EMAIL, _('email notification')),
    )

    thing = models.ForeignKey(Thing,
                  limit_choices_to = {'schedule__gte': datetime.now})
    number = models.IntegerField()
    unit = models.IntegerField(choices=UNITS, default=UNIT_DAY)
    method = models.IntegerField(choices=METHODS, default=METHOD_ALERT)

    def __unicode__(self):
        return _(u'Remind "%s" %s %s before by %s') % (
                self.thing,
                self.number,
                self.get_unit_display(),
                self.get_method_display()
        )

    @property
    def countdown(self):
        return self.thing.schedule - datetime.now()

    def clean(self):
        if not self.thing.schedule:
            raise ValidationError(_(u'Thing must have a schedule date to add a reminder'))

