from django.contrib import admin
from competitions.models import Competition, CompetitionEvent, AthleticsCurriculum
class FilterAdmin(admin.ModelAdmin):
    list_filter = [
        "athlete",
        "event"
    ]

# Register your models here.
admin.site.register(Competition, FilterAdmin)
admin.site.register(CompetitionEvent)
admin.site.register(AthleticsCurriculum)

