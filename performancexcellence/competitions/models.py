from django.db import models
import uuid
from athletes.models import Athlete
# Create your models here.
class Competition(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='competitions', null=True, blank=True)
    competition_name = models.CharField(max_length=200, blank=True, null=True)
    competition_local = models.CharField(max_length=200, blank=True, null=True)
    competition_date = models.DateField(null=True, blank=True)
    competition_result = models.FloatField(blank=True, null=True)
    competition_wind = models.FloatField(blank=True, null=True)
    competition_period_choices = (
        ('Indoor', 'Pista Coberta'),
        ('Outdoor', 'Ar Livre')
    )
    competition_period = models.CharField(max_length=10, choices=competition_period_choices)
    is_final = models.BooleanField(default=False)
    is_heat = models.BooleanField(default=False)
    is_semi_final = models.BooleanField(default=False)
    competition_category_choices = (
    ('OW', 'OW 1'),
    ('DF', 'DF'),
    ('GW', 'GW'),
    ('GL', 'GL'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F')
    )
    competition_category = models.CharField(max_length=10, choices=competition_category_choices)
    world_athletics_points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.competition_name)