from django.contrib import admin
from .models import FAQ, Member


admin.site.register(FAQ)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation']
    list_filter = ['role']