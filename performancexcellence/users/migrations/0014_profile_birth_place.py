# Generated by Django 4.2.2 on 2023-07-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_techincalteam_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_place',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
