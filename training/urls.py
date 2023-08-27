from django.urls import path
from . import views 

urlpatterns = [
    path('strength/new', views.create_strength_training, name='strength_registation'),
    path('jumps/new', views.create_jumps_training, name='jumps_registration'),

]
