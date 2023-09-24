from django.urls import path
from . import views 

urlpatterns = [
    path('evaluation', views.strength_test_create, name="create_evaluation"),
]
