from django.contrib import admin
from competitions.models import Competition, CompetitionEvent
# Register your models here.
admin.site.register(Competition)
admin.site.register(CompetitionEvent)
