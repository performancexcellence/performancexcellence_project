from django.urls import path
from . import views 

urlpatterns = [
    path('<pk>/', views.show_athlete, name='show_athlete'),
    path('', views.athletes_list, name='athletes_list'),
    path('wellness/<pk>/', views.show_athlete_wellness, name='show_athlete_wellness'),
    path('personal_records/<pk>/', views.show_athlete_personal_records, name='show_athlete_personal_records'),
    path('progression/<pk>/', views.show_athlete_progression, name='show_athlete_progression')
]
