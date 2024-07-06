from django.contrib import admin
from .models import Appointment,Client,Coiffeur,Service
# Register your models here.
admin.site.register(Appointment)
admin.site.register(Client)
admin.site.register(Coiffeur)
admin.site.register(Service)
