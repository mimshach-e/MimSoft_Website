from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Project
from services.models import Service


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Project.CATEGORY_CHOICES
        context['services'] = Service.objects.all()
        
        # Filter by category if provided
        category = self.request.GET.get('category')
        if category:
            context['projects'] = Project.objects.filter(category=category)
        
        # Filter by service if provided
        service = self.request.GET.get('service')
        if service:
            context['projects'] = Project.objects.filter(service_provided__id=service)
        
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

