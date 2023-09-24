# Generated by Django 4.2.2 on 2023-07-03 14:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_profile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='athlete_profile', to='users.profile'),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('team_role', models.CharField(choices=[('Coach', 'Treinador'), ('Nutritionist', 'Nutricionista'), ('Doctor', 'Médico'), ('Psychologist', 'Psicólogo'), ('Physiotherapist', 'Fisioterapeuta'), ('Sport Agent', 'Agente Desportivo')], default='Coach', max_length=60)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_profile', to='users.profile')),
            ],
        ),
        migrations.AlterField(
            model_name='athlete',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='users.staff'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='coach_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach_name', to='users.staff'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='users.staff'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='nutritionist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nutritionist', to='users.staff'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='physiotherapist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='physiotherapist', to='users.staff'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='psychologist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='psychologist', to='users.staff'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='second_coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_coach', to='users.staff'),
        ),
        migrations.DeleteModel(
            name='TechincalTeam',
        ),
    ]
