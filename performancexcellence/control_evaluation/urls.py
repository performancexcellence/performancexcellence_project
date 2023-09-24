from django.urls import path
from . import views 

urlpatterns = [
    path('strength/', views.strength_test_create, name='add_strength_test'),
    path('create_speed/', views.create_speed, name='create_speed'),
    #Cenas
]
