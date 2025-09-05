from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'department', 'order', 'created_at']
    list_filter = ['department', 'created_at']
    search_fields = ['name', 'role', 'bio']
    list_editable = ['order']
    ordering = ['order', 'name']

