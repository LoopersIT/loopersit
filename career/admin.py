from django.contrib import admin
from .models import Job, Application



@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline']
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Application)
class ApplicaitonAdmin(admin.ModelAdmin):
    list_display = ['role', 'name', 'email', 'mobile_number']
    list_filter = ['role']

