from django.contrib import admin
from .models import Profile, Athlete, AthleticsEvent, TechincalTeam
# Register your models here.

admin.site.register(Profile)
admin.site.register(Athlete)
admin.site.register(AthleticsEvent)
admin.site.register(TechincalTeam)


