from django.contrib import admin
from .models import Profile, Athlete, AthleticsEvent, Staff
# Register your models here.

admin.site.register(Profile)
admin.site.register(Athlete)
admin.site.register(AthleticsEvent)
admin.site.register(Staff)