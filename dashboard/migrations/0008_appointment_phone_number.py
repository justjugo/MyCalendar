# Generated by Django 4.2.9 on 2024-07-10 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_remove_appointment_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(default='default', max_length=15, unique=True),
        ),
    ]
