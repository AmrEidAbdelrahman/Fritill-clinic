# Generated by Django 4.0.2 on 2022-02-21 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_appointment_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reschedulerequest',
            old_name='refuased',
            new_name='refused',
        ),
    ]
