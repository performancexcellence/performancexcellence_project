from django.urls import path
from . import views 

urlpatterns = [
    path('wellness/', views.wellness, name="wellness"),
]