from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'company', 'role', 'is_featured', 'created_at']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['client_name', 'company', 'content']
    list_editable = ['is_featured']
    ordering = ['-is_featured', '-created_at']

