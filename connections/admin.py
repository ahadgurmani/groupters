from django.contrib import admin
from .models import ConnectionRequests

@admin.register(ConnectionRequests)
class ConnectionRequestsAdmin(admin.ModelAdmin):
    list_display = ['id', 'connection_to', 'connection_by', 'connection_status']

