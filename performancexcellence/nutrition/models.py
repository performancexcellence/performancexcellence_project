from django.db import models
from athletes.models import Athlete

# Create your models here.
class AntropometricData(models.Model):
    date = models.DateField()
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='athlete_antropometric', null=True, blank=True)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    body_fat = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    body_muscle = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    prega_tricipal = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    prega_subescapular = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    prega_bicipal = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    prega_ilio_cristal = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    prega_supra_espinal = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    prega_abdominal = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    prega_coxa = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    prega_gemeo = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    perimeter_relax_arm = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    perimeter_strenght_arm = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    perimeter_abdominal = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    perimeter_hip = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    perimeter_thigh = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    perimeter_calf = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    obs = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.athlete.profile.first_name} {self.athlete.profile.last_name} - {self.date}"