from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    #Infos User
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    #Infos Profile
    name = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default = "profiles/profile_default.png")
    birth_date = models.DateField(max_length=8)
    event_group_choices = (
        ('Velocidade', 'Velocidade'),
        ('Saltos', 'Saltos'),
        ('Lançamentos', 'Lançamentos'),
        ('Fundo, Meio Fundo e Marcha', 'Fundo, Meio Fundo e Marcha'),
        ('Provas Combinadas', 'Provas Combinadas')
    )
    event_group = models.CharField(max_length=60, choices=event_group_choices, default='Provas Combinadas')
    gender_choices = (
        ('m', 'Masculino'),
        ('f', 'Feminino')
    )
    gender = models.CharField(max_length=10, choices=gender_choices)
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    nationality = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    #Team
    agent_name = models.CharField(max_length=200, blank=True, null=True)
    doctor_name = models.CharField(max_length=200, blank=True, null=True)
    nutritionist_name = models.CharField(max_length=200, blank=True, null=True)
    physiotherapist_name = models.CharField(max_length=200, blank=True, null=True)
    psychologist_name = models.CharField(max_length=200, blank=True, null=True)
    team_name = models.CharField(max_length=50, blank=True, null=True)
    second_coach_name = models.CharField(max_length=50, blank=True, null=True)
    coach_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.username)
    
    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url