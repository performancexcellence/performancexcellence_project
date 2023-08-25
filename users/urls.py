from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('edit-account/<str:pk>/', views.editAccount, name="edit-account"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
