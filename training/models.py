from django.db import models
import uuid
from athletes.models import *
# Create your models here.

class StrengthTraining(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='strength_trainings', null=True, blank=True)
    strength_exercises = [
        ('Full Squat', 'Full Squat'),
        ('Full Front Squat', 'Full Front Squat'),
        ('1/2 Squat', '1/2 Squat'),
        ('1/4 Squat', '1/4 Squat'),
        ('Squat Jump', 'Squat Jump'),
        ('Bulgarian Squat', 'Bulgarian Squat'),
        ('Power Clean', 'Power Clean'),
        ('Hang Clean', 'Hang Clean'),
        ('Power Snatch', 'Power Snatch'),
        ('Hang Snatch', 'Hang Snatch'),
        ('Dead Lift', 'Dead Lift'),
        ('Bench Press', 'Bench Press'),
        ('Hip Trust', 'Hip Trust'),
        ('Lunges', 'Lunges'),
        ('Chin Up', 'Chin Up'),
        ('Pull Up', 'Pull Up'),
        ('Pull Over', 'Pull Over')  
    ]
    exercise = models.CharField(max_length=60, choices=strength_exercises, default='Full Squat',blank=False)
    date = models.DateTimeField(blank=False)  
    exercise_notes_choices = [
        ('Excentric', 'Excentric'), 
        ('Concentric', 'Concentric'),
        ('Isometric', 'Isometric'),
    ]
    exercise_notes = models.CharField(max_length=60, choices=exercise_notes_choices, default='Concentric')
    set = models.IntegerField(blank=False)
    nr_repetitions = models.IntegerField(blank=False)  
    weight = models.IntegerField(blank=False)
    median_speed = models.IntegerField()
    median_rom = models.IntegerField()
    best_rep = models.JSONField(null=True, blank=True)  
    left_in_tank = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.exercise} - {self.athlete} - {self.date}"

class JumpsTraining(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='jumps_trainings', null=True, blank=True)
    jumps_training_type_exercises = [
        ('Multijumps', 'Multijumps'),
        ('Technical Training', 'Technical Training')
    ]
    jumps_training_type = models.CharField(max_length=60, choices=jumps_training_type_exercises, default='Multijumps',blank=False)
    technical_training_exercises = [
        ('High Jump', 'High Jump'),
        ('Long Jump', 'Long Jump'),
        ('Triple Jump', 'Triple Jump'),
        ('Pole Vault', 'Pole Vault')
    ]
    technical_training = models.CharField(max_length=60, choices=technical_training_exercises, default=None,blank=True)
    multijumps_training_exercises = [
        ('Horizontal Impulsion', 'Horizontal Impulsion'),
        ('Triple Step', 'Triple Step'),
        ('Triple Hop', 'Triple Hop'),
        ('Penta Step', 'Penta Step'),
        ('Penta Hop', 'Penta Hop'),
        ('Deca Step', 'Deca Step'),
        ('Penta 4 steps', 'Penta 4 steps'),
        ('Penta 6 steps', 'Penta 6 steps')
    ]
    multijumps_training = models.CharField(max_length=60, choices=multijumps_training_exercises, default=None,blank=True)
    poles_info = models.JSONField(null=True, blank=True)
    high_jump_choices = [
        ("Tesouras", "Tesouras"),
        ("Costas", "Costas")
    ]
    high_jump_technique = models.CharField(max_length=60, choices=high_jump_choices, default=None,blank=True)
    nr_steps = models.IntegerField()
    result = models.IntegerField()
    date = models.DateTimeField(blank=False)  


    def __str__(self):
        return f"{self.jumps_training_type} - {self.athlete} - {self.date}"

