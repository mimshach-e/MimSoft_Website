from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('', views.TeamListView.as_view(), name='team_list'),
    path('<int:pk>/', views.team_member_detail, name='team_member_detail'),
]

