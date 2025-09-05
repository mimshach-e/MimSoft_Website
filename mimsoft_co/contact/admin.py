from django.contrib import admin
from .models import ContactSubmission


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'project_interest', 'submission_date']
    list_filter = ['project_interest', 'submission_date', 'consent_to_store']
    search_fields = ['name', 'email', 'company', 'message']
    readonly_fields = ['submission_date']
    ordering = ['-submission_date']




