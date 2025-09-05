from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from .models import ContactSubmission
from .forms import ContactForm


class ContactView(CreateView):
    model = ContactSubmission
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact:contact')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            'Thank you for your message! We will get back to you soon.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Add debugging information
        print("Form errors:", form.errors)
        print("Form non-field errors:", form.non_field_errors)
        
        # Create a more detailed error message
        error_details = []
        for field, errors in form.errors.items():
            for error in errors:
                if field == '__all__':
                    error_details.append(error)
                else:
                    field_name = form.fields[field].label or field
                    error_details.append(f"{field_name}: {error}")
        
        if error_details:
            error_message = "Please correct the following errors: " + "; ".join(error_details)
        else:
            error_message = "Please correct the errors below and try again."
        
        messages.error(
            self.request,
            error_message
        )
        return super().form_invalid(form)

