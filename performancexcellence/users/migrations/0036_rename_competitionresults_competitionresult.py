# Generated by Django 4.2.2 on 2023-07-10 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_competitionresults_delete_athletecurriculum'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompetitionResults',
            new_name='CompetitionResult',
        ),
    ]
