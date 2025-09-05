from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    # Use ReCaptchaV3 for invisible verification
    captcha = ReCaptchaField(
        widget=ReCaptchaV3,
        label='Security Verification',
        help_text='This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.'
    )
    
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'company', 'phone', 'project_interest', 'message', 'consent_to_store', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Company Name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone Number (Optional)'
            }),
            'project_interest': forms.Select(attrs={
                'class': 'form-select'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Tell us about your project...'
            }),
            'consent_to_store': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'consent_to_store': 'I consent to MimSoft Corporation storing my information for project communication purposes.'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        print("Form cleaning - cleaned_data:", cleaned_data)
        return cleaned_data
    
    def clean_consent_to_store(self):
        consent = self.cleaned_data.get('consent_to_store')
        print("Consent validation - consent value:", consent)
        if not consent:
            raise forms.ValidationError(
                'You must consent to data storage to submit this form.'
            )
        return consent
    
    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        print("Captcha validation - captcha value:", captcha)
        return captcha
