# Generated by Django 4.2.2 on 2023-07-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_techincalteam_profile_techincalteam_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='athleticsevent',
            name='event_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='athleticsevent',
            name='event_group',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
