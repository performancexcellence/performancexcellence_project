from django.db import models
import uuid
from users.models import Profile
# Create your models here.
class Staff(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='staff', null=True, blank=True)
    staff_choices = (
    ('Treinador', 'main_coach'),
    ('Treinador Adjunto', 'second_coach'),
    ('Agente Desportivo', 'agent'),
    ('Psicologo', 'psychologist'),
    ('Fisioterapeuta', 'physiotherapist'),
    ('Fisiologista', 'physiologist'),
    ('Médico', 'doctor'),
    ('Nutricionista', 'nutritionist')
    )
    staff_type = models.CharField(max_length=30, choices=staff_choices)
    def __str__(self):
        return str(self.profile.first_name)