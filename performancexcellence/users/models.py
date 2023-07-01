from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    #Infos User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default = "profiles/profile_default.png")
    birth_date = models.DateField(max_length=8)
    gender_choices = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    gender = models.CharField(max_length=10, choices=gender_choices)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    nationality = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url
    
class TechincalTeam(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    team_choices = (
        ('Coach', 'Treinador'),
        ('Nutritionist', 'Nutricionista'),
        ('Doctor', 'Médico'),
        ('Psychologist', 'Psicólogo'),
        ('Physiotherapist', 'Fisioterapeuta'),
        ('Sport Agent', 'Agente Desportivo')
    )
    team_role = models.CharField(max_length=60, choices=team_choices, default='Coach')
    def __str__(self):
        return f"{self.name} - {self.team_role}"
    
class Athlete(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    #Infos Profile
    team_name = models.CharField(max_length=50, blank=True, null=True)
    event_group_choices = (
        ('Speed', 'Velocidade'),
        ('Jumps', 'Saltos'),
        ('Throws', 'Lançamentos'),
        ('Long distance, Middle Distance e Racewalking', 'Fundo, Meio Fundo e Marcha'),
        ('Combined Events', 'Provas Combinadas')
    )
    event_group = models.CharField(max_length=60, choices=event_group_choices, default='Combined Events')
    #Team
    agent = models.OneToOneField(TechincalTeam, on_delete=models.CASCADE, related_name='agent', null=True, blank=True)
    doctor = models.OneToOneField(TechincalTeam, on_delete=models.CASCADE, related_name='doctor', null=True, blank=True)
    nutritionist = models.OneToOneField(TechincalTeam, on_delete=models.CASCADE, related_name='nutritionist', null=True, blank=True)
    physiotherapist = models.OneToOneField(TechincalTeam, on_delete=models.CASCADE, related_name='physiotherapist', null=True, blank=True)
    psychologist = models.OneToOneField(TechincalTeam, on_delete=models.CASCADE, related_name='psychologist', null=True, blank=True)
    second_coach = models.OneToOneField(TechincalTeam, on_delete=models.CASCADE, related_name='second_coach', null=True, blank=True)
    coach_name = models.OneToOneField(TechincalTeam, on_delete=models.CASCADE, related_name='coach_name', null=True, blank=True)
    def __str__(self):
        return f"{self.profile.name} - {self.event_group}"


class AthleticsEvent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    event_group = models.CharField(max_length=200, blank=True, null=True)
    event_name = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return str(self.event_name)
