# Generated by Django 4.2.9 on 2024-07-15 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_appointment_client_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
    ]