# Generated by Django 4.2.7 on 2024-02-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0014_alter_competition_wind_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='wind_direction',
            field=models.CharField(choices=[('+', 'Positive'), ('NW', 'Indoor'), ('-', 'Negative')], default='NW', max_length=10, null=True),
        ),
    ]
