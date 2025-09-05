from django.views.generic import TemplateView
from django.shortcuts import render
from services.models import Service
from team.models import TeamMember
from projects.models import Project
from testimonials.models import Testimonial


class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()[:6]
        context['team_members'] = TeamMember.objects.all()[:4]
        context['projects'] = Project.objects.all()[:6]
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)[:3]
        return context


def about_view(request):
    return render(request, 'core/about.html')

