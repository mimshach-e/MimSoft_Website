from django.db import models
from services.models import Service


class Project(models.Model):
    ECOMMERCE = 'ECOMMERCE'
    MOBILE_APP = 'MOBILE_APP'
    FINTECH = 'FINTECH'
    WEB_APP = 'WEB_APP'
    MARKETING = 'MARKETING'
    
    CATEGORY_CHOICES = [
        (ECOMMERCE, 'E-commerce'),
        (MOBILE_APP, 'Mobile App'),
        (FINTECH, 'FinTech'),
        (WEB_APP, 'Web Application'),
        (MARKETING, 'Digital Marketing'),
    ]
    
    title = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/images/')
    client_logo = models.ImageField(upload_to='projects/client_logos/', blank=True, null=True, help_text='Logo of the client company')
    date_delivered = models.DateField()
    service_provided = models.ManyToManyField(Service, related_name='projects')
    testimonial = models.ForeignKey('testimonials.Testimonial', on_delete=models.SET_NULL, blank=True, null=True, related_name='related_projects')
    project_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_delivered']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return f"{self.title} - {self.client_name}"
