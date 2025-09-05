from django.db import models


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    content = models.TextField()
    avatar = models.ImageField(upload_to='testimonials/avatars/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    project = models.OneToOneField('projects.Project', on_delete=models.SET_NULL, blank=True, null=True, related_name='related_testimonial')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_featured', '-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
    
    def __str__(self):
        return f"{self.client_name} - {self.company}"
