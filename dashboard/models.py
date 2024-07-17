
from django.db import models
from django.db.models.functions import TruncMonth
from django.db.models import Sum
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
   
    phone_number = models.CharField(max_length=15,unique=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    client_first_name = models.CharField(max_length=30)
    client_last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15 )
    coiffeur = models.ForeignKey(Coiffeur, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')]
    )

    class Meta:
        ordering = ['date', 'time']  # Ordonne par date puis par heure si les dates sont identiques

    @classmethod
    def get_monthly_earnings(cls):
        return cls.objects.filter(status='completed').annotate(month=TruncMonth('date')).values('month').annotate(total_earnings=Sum('service__price')).order_by('month')


