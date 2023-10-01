from django.db import models

# Create your models here.
class AntropometricData(models.Model):
    date = models.DateField()
    height = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    body_fat = models.DecimalField(max_digits=6, decimal_places=2)
    lean_mass = models.DecimalField(max_digits=6, decimal_places=2)
    left_arm = models.DecimalField(max_digits=6, decimal_places=2)
    right_arm = models.DecimalField(max_digits=6, decimal_places=2)
    trunk = models.DecimalField(max_digits=6, decimal_places=2)
    left_leg = models.DecimalField(max_digits=6, decimal_places=2)
    right_leg = models.DecimalField(max_digits=6, decimal_places=2)
    head = models.DecimalField(max_digits=6, decimal_places=2)
    metabolism = models.CharField(max_length=255)
    obs = models.TextField()

    def __str__(self):
        return f"{self.athlete.profile.name} - {self.date}"