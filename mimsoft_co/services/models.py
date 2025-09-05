from django.db import models


class Service(models.Model):
    SOFTWARE_DEV = 'SOFTWARE_DEV'
    SOCIAL_MARKETING = 'SOCIAL_MARKETING'
    CREATIVE = 'CREATIVE'
    
    CATEGORY_CHOICES = [
        (SOFTWARE_DEV, 'Software Development'),
        (SOCIAL_MARKETING, 'Social Media & Marketing'),
        (CREATIVE, 'Creative Design'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    specialized_solutions = models.TextField(blank=True, null=True, help_text='Detailed specialized solutions and features for this service')
    icon = models.ImageField(upload_to='services/icons/', blank=True, null=True)
    image = models.ImageField(upload_to='services/images/', blank=True, null=True, help_text='Service image for cards')
    video = models.FileField(upload_to='services/videos/', blank=True, null=True, help_text='Service video for cards (MP4, WebM, etc.)')
    media_type = models.CharField(
        max_length=10,
        choices=[
            ('image', 'Image'),
            ('video', 'Video'),
        ],
        default='image',
        help_text='Choose whether to display image or video'
    )
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.name

