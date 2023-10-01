from django.db import models
import uuid
from athletes.models import Athlete

# Create your models here.
class WellnessDaily(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='athlete_profile', null=True, blank=True)
    weight = models.FloatField(default=0, blank=False, null=False)
    registration_date = models.DateField()
    mood = models.IntegerField(default=50, blank=False, null=False)
    stress_level = models.IntegerField(default=50, blank=False, null=False)
    muscle_soreness = models.IntegerField(default=50, blank=False, null=False)
    sleep_quality = models.IntegerField(default=50, blank=False, null=False)
    fatigue = models.IntegerField(default=50, blank=False, null=False)
    nutrition = models.IntegerField(default=50, blank=False, null=False)
    hydration = models.IntegerField(default=50, blank=False, null=False)

    def __str__(self):
        return f"{self.athlete.profile.name} - {self.registration_date}"