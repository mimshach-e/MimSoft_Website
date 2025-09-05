from django.views.generic import ListView
from django.shortcuts import render
from .models import TeamMember


class TeamListView(ListView):
    model = TeamMember
    template_name = 'team/team_list.html'
    context_object_name = 'team_members'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Group team members by department
        team_by_department = {}
        for member in TeamMember.objects.all():
            department = member.get_department_display()
            if department not in team_by_department:
                team_by_department[department] = []
            team_by_department[department].append(member)
        
        context['team_by_department'] = team_by_department
        return context


def team_member_detail(request, pk):
    member = TeamMember.objects.get(pk=pk)
    return render(request, 'team/team_member_detail.html', {'member': member})

