from django.contrib import admin

from notifications.models import NotificationModel


@admin.register(NotificationModel)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'receiver', 'title', 'body', 'read', 'time']
