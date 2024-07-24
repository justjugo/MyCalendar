from django.shortcuts import render,get_object_or_404, redirect
from account.models import Account
from .models import Appointment,Client,Coiffeur
from django.utils import timezone
from .forms import AppointmentForm
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.

def index(request):
    if request.user.is_authenticated :
        print(request.user.nick_name)
        if request.user.is_admin  :
            client =Client.objects.all()
            emploies = Coiffeur.objects.all()
            staff= Account.objects.filter(is_staff=True)
            monthly_earning = Appointment.get_monthly_earnings()
            uppcomingappointment= Appointment.objects.filter(Q(date=timezone.now().date()) and Q(status='confirmed'))
            uppcomingappointment= Appointment.objects.filter( status='Scheduled')
            current_month = timezone.now().replace(day=1).date()
            print(current_month.month)
            current_month_earnings = next((item['total_earnings'] for item in monthly_earning if item['month'].month == current_month.month),0 )
            
            
            return render(request,'admin/appointments/dashboardadmin.html',{'Appointment':appointment,'Client':client,'total_earnings':monthly_earning,'current_month_earnings':current_month_earnings, 'staff':staff,'emploies':emploies})
        else:
            appointment= Appointment.objects.all()    
            return render (request,'stuff/dashboardstuff.html',{'Appointment':appointment})
        
    return render(request,'user/index.html')


def appointmentsList(request):
    appointments=Appointment.objects.all()
    return render(request,'admin/appointments/appointmentsList.html',{'appointments':appointments})

def book_appointment(request):
    
    succes=False
    appointments=Appointment.objects.all()
    where="Book Appointment"
    
    if request.method=='POST':
         form= AppointmentForm(request.POST)
         
         if form.is_valid():
             client =Client.objects.filter(phone_number=form.cleaned_data['phone_number'])
             if client.count() == 0:
                 newClient=Client(
                     first_name=form.cleaned_data['client_first_name'],
                     last_name=form.cleaned_data['client_last_name'],
                     phone_number=form.cleaned_data['phone_number']
                 )
                 newClient.save()
             
             form.save()
             succes=True
             return render(request,'admin/appointments/appointmentsList.html',{'appointments':appointments,'succes':succes})
         else:
             
             return render(request,'admin/appointments/bookAppointment.html',{'form':form,'where':where})
    else:
        form=AppointmentForm()
       
    
    return render(request,'admin/appointments/bookAppointment.html',{'form':form,'where':where})
    
def editAppointment(request,appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    where="Edit Appointment"
   
    if request.method == 'POST':
        
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            
            form.save()
            return redirect('appointmentsList')  
        else:
            print('not valid')
            render(request, 'admin/appointments/bookAppointment.html', {'form': form,'where':"there is a problm"})
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'admin/appointments/bookAppointment.html', {'form': form,'where':where})

def updateAppointmentStatus(request, appointment_id, new_status):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = new_status
    appointment.save()
    return redirect('index')


def deleteAppointment(request, appointment_id):
    
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    return redirect('appointmentsList') 


def appointmentDetails(request, appointment_id):

    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render (request,'admin/appointments/appointmentDetails.html',{'appointment':appointment})


def appointments_json(request):
    appointments = Appointment.objects.all()
    events = []
    color='#116aef'

    for appointment in appointments:
       
        events.append({
            'title': f"{appointment.client_first_name} | {appointment.time.hour}h | {appointment.coiffeur}",
            'start': appointment.date.strftime('%Y-%m-%d'),  # Format date as YYYY-MM-DD
            'url': f"appointmentDetails/{appointment.id}",  # URL to appointment detail view
            'textColor': color,
            'color': '#ffffff',
            'borderColor': '#469ED8',
        })
        

    return JsonResponse(events, safe=False)

def calandar(request):
    return render(request,'admin/appointments/appointments.html',{})

def stufflist(request):
    staff= Account.objects.filter(is_staff=True)

    return render(request,'admin/staff/staffList.html',{'staff':staff})
