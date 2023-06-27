from django.urls import path
from . import views 

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('edit-account/<str:pk>/', views.editAccount, name="edit-account"),
    
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
