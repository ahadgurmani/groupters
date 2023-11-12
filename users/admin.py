from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import admin as auth_admin

from .models import School, Grade,SignupUser


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name']


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_grade']


@admin.register(SignupUser)
class SignupAdmin(UserAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'school_email', 'school', 'grade', 'password', 'confirm_password', 'image', 'about']
    fieldsets = ((SignupUser, {'fields': ('school_email', 'school', 'grade', 'image', 'about')}),) + auth_admin.UserAdmin.fieldsets


# Register your models here.
