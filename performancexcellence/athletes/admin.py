from django.contrib import admin
from athletes.models import *

# Register your models here.
admin.site.register(Athlete)
admin.site.register(AthleticsEvent)
admin.site.register(AthleticsEventGroup)