from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # Infos User
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_user', null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='static/profiles/', default="profiles/profile_default.png")
    birth_date = models.DateField(null=True, blank=True)
    gender_choices = (('M', 'Masculino'), ('F', 'Feminino'))
    gender = models.CharField(max_length=10, choices=gender_choices)
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    nationality = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
            # Remove o prefixo 'static/' da URL
            if url.startswith('static/'):
                url = url[len('static/'):]
        except:
            url = ''
        return url

class AthleticsEvent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    event_group = models.CharField(max_length=200, blank=True, null=True)
    event_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.event_name)
    
class Staff(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='staff_profile', null=True, blank=True)
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
        return f"{self.name}"
    
class Athlete(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='athlete_profile', null=True, blank=True)
    athletics_event = models.ForeignKey(AthleticsEvent, on_delete=models.CASCADE, related_name='athlete_athletics_event', null=True, blank=True)
    event_group_choices = (
        ('Speed', 'Velocidade'),
        ('Jumps', 'Saltos'),
        ('Throws', 'Lançamentos'),
        ('Long distance, Middle Distance e Racewalking', 'Fundo, Meio Fundo e Marcha'),
        ('Combined Events', 'Provas Combinadas')
    )
    event_group = models.CharField(max_length=200, choices=event_group_choices, default='Combined Events', blank=True, null=True)
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
    url_world_athletics = models.CharField(max_length=1000, blank=True, null=True)
    #Team
    agent = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='agent', null=True, blank=True)
    doctor = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='doctor', null=True, blank=True)
    nutritionist = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='nutritionist', null=True, blank=True)
    physiotherapist = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='physiotherapist', null=True, blank=True)
    psychologist = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='psychologist', null=True, blank=True)
    second_coach = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='athlete_second_coach', null=True, blank=True)
    main_coach = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='coach_name', null=True, blank=True)
    def __str__(self):
        return f"{self.profile} - {self.event_group}"



