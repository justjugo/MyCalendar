
from django.db import models
from django.conf import settings

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()  # Durée du service
    def __str__(self):
        return self.name

class Coiffeur(models.Model):
    first_name = models.CharField(max_length=30,default="default")
    last_name = models.CharField(max_length=30,default="default")
    email = models.EmailField(unique=True,default="default")
    phone_number = models.CharField(max_length=15,default="default")
    address = models.TextField(default="default")
    specialties = models.ManyToManyField(Service, related_name='coiffeurs')  # Les services offerts par le coiffeur

    def __str__(self):
        return self.first_name
    

class Client(models.Model):
    first_name = models.CharField(max_length=30,default="default")
    last_name = models.CharField(max_length=30,default="default")
    email = models.EmailField(unique=True,default="default")
    phone_number = models.CharField(max_length=15,unique=True)
    address = models.TextField(default="default")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(models.Model):
    client_first_name = models.CharField(max_length=30,default="default")
    client_last_name = models.CharField(max_length=30,default="default")
    coiffeur = models.ForeignKey(Coiffeur, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')]
    )

    def __str__(self):
        return f"{self.client_first_name} {self.client_last_name} - {self.service.name} avec {self.coiffeur.first_name} le {self.date} à {self.time}"