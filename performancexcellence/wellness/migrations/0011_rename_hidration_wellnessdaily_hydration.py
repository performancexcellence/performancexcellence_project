# Generated by Django 4.2.4 on 2023-10-01 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wellness', '0010_wellnessdaily_hidration_wellnessdaily_nutrition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wellnessdaily',
            old_name='hidration',
            new_name='hydration',
        ),
    ]
