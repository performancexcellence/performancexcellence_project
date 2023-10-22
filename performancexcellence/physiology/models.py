from django.db import models
import uuid
from athletes.models import Athlete

# Create your models here.
class Evaluation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='athlete_profile_physiology_evaluation', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    #CMJ
    cmj= models.FloatField(null=True, blank=True, verbose_name='Counter Movement Jump (CMJ)')
    #10-5
    average_rsi= models.FloatField(null=True, blank=True)
    #MTP
    imtp_peak_force= models.FloatField(null=True, blank=True)
    #Adutor
    adductor_left_peak_force= models.FloatField(null=True, blank=True)
    adductor_right_peak_force= models.FloatField(null=True, blank=True)
    #Abdutor 
    abductor_left_peak_force= models.FloatField(null=True, blank=True)
    abductor_right_peak_force= models.FloatField(null=True, blank=True)
    #Hamstrings
    hams_right = models.FloatField(null=True, blank=True)
    hams_left = models.FloatField(null=True, blank=True)
    #Quad
    quad_left = models.FloatField(null=True, blank=True)
    quad_right = models.FloatField(null=True, blank=True)
    #Gemeos
    calf_left = models.FloatField(null=True, blank=True)
    calf_right = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.athlete.profile.first_name} {self.athlete.profile.last_name} - {self.date}"