from django.urls import path
from . import views 

urlpatterns = [
    path('athlete/<pk>/', views.show_athlete, name='show_athlete'),
    path('', views.athletes_list, name='athletes_list'),
    #path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    #path('edit-account/<str:pk>/', views.editAccount, name="edit-account"),

]
