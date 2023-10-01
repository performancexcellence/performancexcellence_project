# Generated by Django 4.2.4 on 2023-10-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AntropometricData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=6)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('body_fat', models.DecimalField(decimal_places=2, max_digits=6)),
                ('lean_mass', models.DecimalField(decimal_places=2, max_digits=6)),
                ('left_arm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('right_arm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('trunk', models.DecimalField(decimal_places=2, max_digits=6)),
                ('left_leg', models.DecimalField(decimal_places=2, max_digits=6)),
                ('right_leg', models.DecimalField(decimal_places=2, max_digits=6)),
                ('head', models.DecimalField(decimal_places=2, max_digits=6)),
                ('metabolism', models.CharField(max_length=255)),
                ('obs', models.TextField()),
            ],
        ),
    ]
