from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
from users.models import Profile

class AthleticsEventGroup(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    event_groups = (
        ('Speed', 'Velocidade'),
        ('Jumps', 'Saltos'),
        ('Throws', 'Lançamentos'),
        ('Long distance, Middle Distance e Racewalking', 'Fundo, Meio Fundo e Marcha'),
        ('Combined Events', 'Provas Combinadas')
    )
    event_group = models.CharField(max_length=60, choices=event_groups, default='Combined Events')
    def __str__(self):
        return str(self.event_group)


class Athlete(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='athlete_profile', null=True, blank=True)
    event_group = models.ForeignKey(AthleticsEventGroup, on_delete=models.CASCADE)
    #Infos Profile
    team_name = models.CharField(max_length=50, blank=True, null=True)
    url_world_athletics = models.CharField(max_length=1000, blank=True, null=True)
    url_fpacompeticoes = models.CharField(max_length=1000, blank=True, null=True)
    #Team
    agent = models.CharField(max_length=200, blank=True, null=True)
    doctor = models.CharField(max_length=200, blank=True, null=True)
    nutritionist = models.CharField(max_length=200, blank=True, null=True)
    physiotherapist = models.CharField(max_length=200, blank=True, null=True)
    psychologist = models.CharField(max_length=200, blank=True, null=True)
    second_coach = models.CharField(max_length=200, blank=True, null=True)
    main_coach = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return f"{self.profile} - {self.event_group}"
