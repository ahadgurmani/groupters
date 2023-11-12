from django.contrib import admin
from .models import GroupCategory, CreateGroup


@admin.register(GroupCategory)
class GroupCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']


@admin.register(CreateGroup)
class CreateGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'admin', 'image', 'group_Type', 'group_category', 'description', 'title']
