# Generated by Django 4.2.7 on 2023-12-15 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='antropometricdata',
            old_name='head',
            new_name='perimeter_abdominal',
        ),
        migrations.RenameField(
            model_name='antropometricdata',
            old_name='lean_mass',
            new_name='perimeter_calf',
        ),
        migrations.RenameField(
            model_name='antropometricdata',
            old_name='left_arm',
            new_name='perimeter_hip',
        ),
        migrations.RenameField(
            model_name='antropometricdata',
            old_name='left_leg',
            new_name='perimeter_relax_arm',
        ),
        migrations.RenameField(
            model_name='antropometricdata',
            old_name='right_arm',
            new_name='perimeter_strenght_arm',
        ),
        migrations.RenameField(
            model_name='antropometricdata',
            old_name='trunk',
            new_name='perimeter_thigh',
        ),
        migrations.RemoveField(
            model_name='antropometricdata',
            name='metabolism',
        ),
        migrations.RemoveField(
            model_name='antropometricdata',
            name='right_leg',
        ),
    ]
