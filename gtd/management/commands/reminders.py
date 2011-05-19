from django.core.management.base import BaseCommand, CommandError
from gtd.models import Reminder

class Command(BaseCommand):
    help = 'Execute action reminders'

    def handle(self, *args, **options):
        for reminder in Reminder.objects.all():
            print u'%s' % reminder
