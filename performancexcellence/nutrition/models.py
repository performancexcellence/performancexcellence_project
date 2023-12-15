from django.db import models

# Create your models here.
class AntropometricData(models.Model):
    date = models.DateField()
    height = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    body_fat = models.DecimalField(max_digits=6, decimal_places=2)
    perimeter_relax_arm = models.DecimalField(max_digits=6, decimal_places=2)
    perimeter_strenght_arm = models.DecimalField(max_digits=6, decimal_places=2)
    perimeter_abdominal = models.DecimalField(max_digits=6, decimal_places=2)
    perimeter_hip = models.DecimalField(max_digits=6, decimal_places=2)
    perimeter_thigh = models.DecimalField(max_digits=6, decimal_places=2)
    perimeter_calf = models.DecimalField(max_digits=6, decimal_places=2)
    obs = models.TextField()

    def __str__(self):
        return f"{self.athlete.profile.first_name} {self.athlete.profile.last_name} - {self.date}"