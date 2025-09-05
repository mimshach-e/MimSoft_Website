from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client_name', 'category', 'date_delivered', 'created_at']
    list_filter = ['category', 'date_delivered', 'created_at']
    search_fields = ['title', 'client_name', 'description']
    filter_horizontal = ['service_provided']
    date_hierarchy = 'date_delivered'
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'client_name', 'category', 'description')
        }),
        ('Media', {
            'fields': ('image', 'client_logo')
        }),
        ('Project Details', {
            'fields': ('date_delivered', 'service_provided', 'project_url')
        }),
        ('Related Content', {
            'fields': ('testimonial',),
            'classes': ('collapse',)
        }),
    )

