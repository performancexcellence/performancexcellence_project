from django.db import models
import uuid
from athletes.models import Athlete
from competitions.models import *
# Create your models here.
class TrainingProgramme(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='athlete_profile_training_programme', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    local = models.CharField(max_length=100,null=True, blank=True)
    intensity = models.IntegerField(default=1)
    hours = models.CharField(max_length=100, null=True, blank=True)
    warmup = models.TextField(null=True, blank=True)
    main =  models.TextField(null=True, blank=True)
    cool_down =  models.TextField(null=True, blank=True)
    obs =  models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.athlete.profile.first_name} {self.athlete.profile.last_name} - {self.date}"

class Goals(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='athlete_profile_goal', null=True, blank=True)
    competition_event = models.ForeignKey(CompetitionEvent, on_delete=models.CASCADE, related_name='athlete_profile_goal', null=True, blank=True)
    season = models.CharField(max_length=255, null=True, blank=True)  # Typically, class attributes should be lowercase, consider renaming this to "season"
    season_period = models.CharField(max_length=255, null=True, blank=True)
    competition_result = models.CharField(null=True, blank=True, max_length=20)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.athlete.profile.first_name} {self.athlete.profile.last_name} - {self.competition_event} - {self.season} - {self.season_period}"