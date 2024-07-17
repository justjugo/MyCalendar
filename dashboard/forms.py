from django import forms
from django.forms import ModelForm
from .models import Appointment
from datetime import time, date
from django.core.exceptions import ValidationError
from django.db.models import Q

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'client_first_name', 'client_last_name', 'phone_number',
            'coiffeur', 'service', 'date', 'time', 'status'
        ]
        labels = {
            'client_first_name': 'First Name',
            'client_last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'coiffeur': 'Employe',
            'service': 'Service',
            'date': 'Date',
            'time': 'Time',
            'status': 'Status'
        }
        widgets = {
            'client_first_name': forms.TextInput(attrs={
                'type': "text", 'class': "form-control", 'id': "a1", 'placeholder': "Enter first name"
            }),
            'client_last_name': forms.TextInput(attrs={
                'type': "text", 'class': "form-control", 'id': "a2", 'placeholder': "Enter last name"
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': "form-control", 'id': "a5", 'placeholder': "Enter phone number"
            }),
            'coiffeur': forms.Select(attrs={
                'class': "form-select", 'id': "a3"
            }),
            'service': forms.Select(attrs={
                'class': "form-select", 'id': "a4"
            }),
            'date': forms.DateInput(attrs={
                'type': "date", 'class': "form-control", 'id': "a6", 'placeholder': "Select date"
            }),
            'time': forms.TimeInput(attrs={
                'type': "time", 'class': "form-control", 'id': "a7", 'placeholder': "Select time"
            }),
            'status': forms.Select(attrs={
                'class': "form-select", 'id': "a8"
            }),
        }
        input_formats = {
            'time': ['%H:%M', '%I:%M %p']  # %H:%M pour 24 heures, %I:%M %p pour 12 heures
        }

    def clean_time(self):
        appointment_time = self.cleaned_data['time']
        start_time = time(8, 0)  # 8:00 AM
        end_time = time(18, 0)   # 6:00 PM

        if not (start_time <= appointment_time <= end_time):
            raise ValidationError("L'heure du rendez-vous doit être comprise entre 08:00 et 18:00.")
        
        return appointment_time

    def clean_date(self):
        appointment_date = self.cleaned_data['date']
        # Vérifiez si le jour est un vendredi (5 correspond à vendredi)
        if appointment_date.weekday() == 4:  # En Python, lundi = 0, mardi = 1, ..., vendredi = 4
            raise ValidationError("Les rendez-vous ne peuvent pas être pris pour le vendredi.")
        
        current_date = date.today()

        if appointment_date < current_date:
            raise ValidationError("La date du rendez-vous ne peut pas être antérieure à la date actuelle.")

        return appointment_date

