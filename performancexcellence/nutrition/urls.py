from django.urls import path
from . import views

urlpatterns = [
   path('create', views.antropometric_data_create, name="create_nutrition_evaluation"),
]
