from django.db import models

class FocusManager(models.Manager):
    def get_query_set(self):
        return super(FocusManager, self).get_query_set().filter(deleted=False)

    def today(self, queryset):
        pass

    def tomorrow(self, queryset):
        pass

    def overdue(self, queryset):
        pass

    def executable(self, queryset):
        pass

    def following(self, queryset):
        pass

    def delegated(self, queryset):
        pass

    def deferred(self, queryset):
        pass

    def incubated(self, queryset):
        pass

