"""
URL configuration for performancexcellence project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('athletes/', include('athletes.urls')),
    path('competition/', include('competitions.urls')),
    path('staff/', include('staffs.urls')),
    path('wellness/', include('wellness.urls')),
    path('physiology/', include('physiology.urls')),
    path('control-evaluation/', include('control_evaluation.urls')),
    path('training-programme/', include('training_programme.urls')),
    path('nutrition/', include('nutrition.urls')),
]
