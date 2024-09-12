from django.urls import path
from . import views

urlpatterns = [
    path('wellness/<str:pk>/', views.wellness_questionnaire, name='wellness_questionnaire'),
]