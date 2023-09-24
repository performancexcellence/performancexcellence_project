from django.urls import path
from . import views 

urlpatterns = [
    path('create', views.training_programme_create, name="create_programme"),
    #path('create_goals', views.training_programme_create, name="create_goals"),
]
