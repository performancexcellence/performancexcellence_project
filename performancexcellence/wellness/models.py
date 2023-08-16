from django.db import models
import uuid
from athletes.models import Athlete

# Create your models here.
class WellnessDaily(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='athlete_profile', null=True, blank=True)
    weight = models.FloatField(max_length=200, blank=True, null=True)
    heart_rate = models.IntegerField(max_length=10, default= 0)
    registation_date = models.DateField()
    levels_groups = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    mood =  models.IntegerField(choices=levels_groups, default=0)
    stress_level =  models.IntegerField(choices=levels_groups, default=0)
    muscle_soreness =  models.IntegerField(choices=levels_groups, default=0)
    sleep_quality = models.IntegerField(choices=levels_groups, default=0)
    fatigue = models.IntegerField(choices=levels_groups, default=0)

    def __str__(self):
        return f"{self.athlete.name} - {self.registation_date}"