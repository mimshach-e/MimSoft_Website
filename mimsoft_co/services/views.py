from django.views.generic import ListView
from django.shortcuts import render
from .models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Group services by category
        services_by_category = {}
        for service in Service.objects.all():
            category = service.get_category_display()
            if category not in services_by_category:
                services_by_category[category] = []
            services_by_category[category].append(service)
        
        context['services_by_category'] = services_by_category
        return context


def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})

