from django.contrib import admin
from .models import ResumeTemplate, UserResume

@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(UserResume)
class UserResumeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']