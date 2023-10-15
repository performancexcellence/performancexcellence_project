from django.db import models
from athletes.models import Athlete

# Create your models here.
class Injury(models.Model):
    date = models.DateField()
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='athlete_injury', null=True, blank=True)
    injury_type = models.CharField(max_length=255)
    observation = models.TextField()
    severity = models.CharField(max_length=255)
    recuperation_days = models.IntegerField()

    def __str__(self):
        return f"{self.athlete.profile.first_name} {self.athlete.profile.last_name} - {self.date}"