from django.contrib import admin

import Playable
from Playable.models import User, Job, Project,Asset,AnalyticsEvent
from Playable.views import AnalyticsEventView

# Register your models here.
admin.site.register(User)
admin.site.register(Job)
admin.site.register(Project)
admin.site.register(Asset)
admin.site.register(AnalyticsEvent)