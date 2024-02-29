from django.db import models
import uuid
from athletes.models import Athlete
# Create your models here.
class CompetitionEvent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    event_name = models.CharField(max_length=200, blank=True, null=True)
    short_track = models.BooleanField(default=True)
    timing = models.BooleanField(default=False)
    wind_influence = models.BooleanField(default=False)
    def __str__(self):
        return str(self.event_name)
    
class Competition(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    event = models.ForeignKey(CompetitionEvent, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='competitions', null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    local = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    is_timing = models.BooleanField(default=True)
    is_championship = models.BooleanField(default=False)
    result= models.CharField(blank=True, null=True, max_length=30)
    competition_wind = models.FloatField(blank=True, null=True, default=0)
    competition_period_choices = (
        ('Indoor', 'Pista Coberta'),
        ('Outdoor', 'Ar Livre')
    )
    competition_period = models.CharField(max_length=10, choices=competition_period_choices, default="Outdoor")
    world_athletics_points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.athlete.profile.first_name} {self.athlete.profile.last_name} - {self.name} - {self.date} - {self.event}"


class AthleticsCurriculum(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='athletics_curriculum', null=True, blank=True)
    competition_event = models.ForeignKey(CompetitionEvent, on_delete=models.CASCADE, related_name='competition_event_curriculum', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)  # Typically, class attributes should be lowercase, consider renaming this to "position"
    competition_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.athlete.profile.first_name} {self.athlete.profile.last_name} - {self.title} - {self.position}"
