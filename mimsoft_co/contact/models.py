from django.db import models


class ContactSubmission(models.Model):
    WEB_DEV = 'WEB_DEV'
    MOBILE_APP = 'MOBILE_APP'
    MARKETING = 'MARKETING'
    DESIGN = 'DESIGN'
    CONSULTING = 'CONSULTING'
    
    PROJECT_INTEREST_CHOICES = [
        (WEB_DEV, 'Website Development'),
        (MOBILE_APP, 'Mobile App Development'),
        (MARKETING, 'Digital Marketing'),
        (DESIGN, 'UI/UX Design'),
        (CONSULTING, 'IT Consulting'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)
    project_interest = models.CharField(max_length=20, choices=PROJECT_INTEREST_CHOICES)
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    consent_to_store = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-submission_date']
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'
    
    def __str__(self):
        return f"{self.name} - {self.company} - {self.submission_date.strftime('%Y-%m-%d')}"

