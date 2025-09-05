from django.db import models


class TeamMember(models.Model):
    DEVELOPMENT = 'DEVELOPMENT'
    DESIGN = 'DESIGN'
    MARKETING = 'MARKETING'
    MANAGEMENT = 'MANAGEMENT'
    
    DEPARTMENT_CHOICES = [
        (DEVELOPMENT, 'Development'),
        (DESIGN, 'Design'),
        (MARKETING, 'Marketing'),
        (MANAGEMENT, 'Management'),
    ]
    
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/photos/', blank=True, null=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    linkedin_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
    
    def __str__(self):
        return f"{self.name} - {self.role}"

