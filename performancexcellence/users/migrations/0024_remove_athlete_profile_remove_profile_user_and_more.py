# Generated by Django 4.2.2 on 2023-07-03 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20230703_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='profile',
        ),
    ]
