from django.shortcuts import render
from account.models import Account
from .models import Appointment
# Create your views here.

def index(request):
    if request.user.is_authenticated :
        print(request.user.nick_name)
        if request.user.is_admin  :
            appointment= Appointment.objects.all()
            return render(request,'admin/dashboardadmin.html',{'Appointment':appointment})
        else:
            appointment= Appointment.objects.all()    
            return render (request,'stuff/dashboardstuff.html',{'Appointment':appointment})
        
    return render(request,'user/index.html')

