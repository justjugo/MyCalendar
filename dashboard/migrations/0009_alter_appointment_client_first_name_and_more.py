# Generated by Django 4.2.9 on 2024-07-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_appointment_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='client_first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='client_last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
