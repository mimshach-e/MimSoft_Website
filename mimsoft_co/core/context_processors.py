from django.conf import settings
from services.models import Service


def company_info(request):
    """Context processor to inject company information into all templates."""
    context = {
        'company_name': getattr(settings, 'COMPANY_NAME', 'MimSoft Corporation'),
        'company_tagline': getattr(settings, 'COMPANY_TAGLINE', 'Empowering Businesses Through Innovative Digital Solutions'),
        'company_mission': getattr(settings, 'COMPANY_MISSION', 'To deliver cutting-edge software solutions that drive business growth and digital transformation.'),
        'company_achievements': getattr(settings, 'COMPANY_ACHIEVEMENTS', {
            'projects_completed': 50,
            'client_satisfaction': 98,
            'years_experience': 5,
            'team_members': 15,
        }),
    }
    
    # Add service categories for navigation
    try:
        context['service_categories'] = Service.objects.values_list('category', flat=True).distinct()
    except:
        context['service_categories'] = []
    
    return context

