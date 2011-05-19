from django.contrib import admin
from django.contrib import databrowse
from gtd.models import Thing, Project, Context, Reminder
from django import forms

class ReminderInline(admin.TabularInline):
    model = Reminder
    extra = 0

class ThingAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('get_name', 'get_context', 'get_project', 'get_progress',
                    'status', 'get_reminders', 'get_created')
    list_display_link = ('get_name', 'status')
    list_filter = ('context', 'project', 'schedule','status', 'deleted', 'archived', )
    list_editable = ('status', )
    search_fields = ['name', 'description']
    inlines = [ReminderInline,]
    select_related = True

    class Media:
        css = {"all": ("admin/css/changelist.css",)}

class ThingModelForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'context', 'progress', 'status', 'project', 'deleted', 'archived')

class ThingInline(admin.TabularInline):
    model = Thing
    form = ThingModelForm

class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('name', 'active', 'thing_count', 'thing_todo_count', 'thing_done_count', 'get_progress_bar', 'get_deadline')
    list_filter = ('active', 'deadline')
    list_editable = ('active', )
    search_fields = ['name', 'description']
    inlines = [ThingInline,]
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
        'fields': ('name', 'slug', 'deadline', 'get_progress', 'description', 'active')
        }),
    )
    readonly_fields = ['get_progress',]

    class Media:
        css = {"all": ("admin/css/changelist.css",)}

class ContextAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'thing_count', 'thing_todo_count', 'thing_done_count')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ThingInline,]

class ReminderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'countdown')
    list_filter = ('method',)
    search_fields = ['thing__name', 'thing__description']

admin.site.register(Thing, ThingAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Context, ContextAdmin)
admin.site.register(Reminder, ReminderAdmin)
databrowse.site.register(Thing)
databrowse.site.register(Project)
databrowse.site.register(Context)
databrowse.site.register(Reminder)
