# Generated by Django 4.2.7 on 2023-11-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_evaluation', '0007_strength_load_alter_speed_evaluation_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strength',
            name='sets',
        ),
        migrations.AlterField(
            model_name='strength',
            name='mean_power',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='strength',
            name='mpv',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='strength',
            name='peak_velocity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='strength',
            name='rom',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
