# Generated by Django 4.2.4 on 2023-09-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_evaluation', '0004_alter_strength_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strength',
            name='exercise',
            field=models.CharField(choices=[('Power Clean', 'Power Clean'), ('Parallel Squat', 'Parallel Squat'), ('Half Squat', 'Half Squat'), ('Bench Press', 'Bench Press')], default='Parallel Squat', max_length=50),
        ),
    ]
