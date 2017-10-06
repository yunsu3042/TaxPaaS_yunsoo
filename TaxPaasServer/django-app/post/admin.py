from django.contrib import admin
from post.models import Task, ScheduledTask, ScheduledTaskInstance

admin.site.register(Task)
admin.site.register(ScheduledTask)
admin.site.register(ScheduledTaskInstance)