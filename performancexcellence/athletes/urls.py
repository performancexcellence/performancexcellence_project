from django.urls import path
from . import views 

urlpatterns = [
    path('<pk>/', views.show_athlete, name='show_athlete'),
    path('', views.athletes_list, name='athletes_list'),
    path('wellness/<pk>/', views.show_athlete_wellness, name='show_athlete_wellness'),
    path('personal_records/<pk>/', views.show_athlete_personal_records, name='show_athlete_personal_records'),
    path('progression/<pk>/', views.show_athlete_progression, name='show_athlete_progression'),
    path('goals/<pk>/', views.show_athlete_goals, name='show_athlete_goals'),
    path('control&Evaluation/<pk>/', views.show_control_evaluation, name='show_control_evaluation'),
    path('injuries/<pk>/', views.show_control_injuries, name='show_control_injuries'),
    path('antropometric/<pk>/', views.show_athlete_antropometric, name='show_athlete_antropometric')

]
