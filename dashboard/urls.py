

from django.urls import path,include
from .views import index,appointmentsList,book_appointment,appointments_json,calandar

urlpatterns = [
    path('',index,name="index" ),
    path('appointmentsList/',appointmentsList,name="appointmentsList" ),
    path('bookAppointment/',book_appointment,name='bookAppointment'),
    path('calandar/appointments-json/', appointments_json, name='appointments-json'),
    path('calandar/', calandar, name='calandar'),
    
]
