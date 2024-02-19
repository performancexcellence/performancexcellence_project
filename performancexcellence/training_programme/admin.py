from django.contrib import admin
from training_programme.models import *

# Register your models here.

class FilterAdmin(admin.ModelAdmin):
    list_filter = [
        "athlete"
    ]

admin.site.register(Goals, FilterAdmin)
admin.site.register(TrainingProgramme, FilterAdmin)
