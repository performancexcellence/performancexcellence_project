from django.db import models
from athletes.models import Athlete
import uuid
import json

class Strength(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='strength_records', null=True, blank=True)
    GOAL_CHOICES = (("1 RM", "1 RM"), ("Power", "Power"))
    goal = models.CharField(max_length=10, choices=GOAL_CHOICES, default="Power")
    STRENGTH_EXERCISE_CHOICES = (
        ('Power Clean', 'Power Clean'),
        ('Parallel Squat', 'Parallel Squat'),
        ('Half Squat', 'Half Squat'),
        ('Bench Press', 'Bench Press'),
    )
    exercise = models.CharField(max_length=50, choices=STRENGTH_EXERCISE_CHOICES, default="Parallel Squat")
    date = models.DateField(null=True, blank=True)
    sets = models.IntegerField()
    mpv = models.JSONField(default=list, blank=True, null=True)  
    peak_velocity = models.JSONField(default=list, blank=True, null=True)  
    rom = models.JSONField(default=list, blank=True, null=True)  
    mean_power = models.JSONField(default=list, blank=True, null=True)  

    def __str__(self):
        return f"{self.athlete} - {self.exercise} - {self.date}"

    def set_reps(self, reps):
        self.reps = json.dumps(reps)

    def set_mpv(self, mpv):
        self.mpv = json.dumps(mpv)

    def get_mpv(self):
        return json.loads(self.mpv)

    def set_peak_velocity(self, peak_velocity):
        self.peak_velocity = json.dumps(peak_velocity)

    def get_peak_velocity(self):
        return json.loads(self.peak_velocity)

    def set_rom(self, rom):
        self.rom = json.dumps(rom)

    def get_rom(self):
        return json.loads(self.rom)

    def set_mean_power(self, mean_power):
        self.mean_power = json.dumps(mean_power)

    def get_mean_power(self):
        return json.loads(self.mean_power)

class Speed(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='speed_records', null=True, blank=True)
    EVALUATION_CHOICES = (("Aceleração", "Aceleração"), ("Velocidade Máxima", "Velocidade Máxima"), ("Completo 0-40", "Completo 0-40"), ("150", "150"), ("300", "300"), ("350", "350"))
    evaluation_choice = models.CharField(max_length=30, choices=EVALUATION_CHOICES, default="Speed")
    date = models.DateField(null=True, blank=True)
    distance = models.JSONField(default=list, blank=True, null=True)  
    time = models.JSONField(default=list, blank=True, null=True)  
