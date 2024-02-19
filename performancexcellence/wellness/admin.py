from django.contrib import admin
from wellness.models import *
class FilterAdmin(admin.ModelAdmin):
    list_filter = [
        "athlete"
    ]

# Register your models here.
admin.site.register(WellnessDaily, FilterAdmin)
admin.site.register(LoadControl, FilterAdmin)
