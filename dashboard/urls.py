

from django.urls import path,include
from .views import index,appointmentsList,book_appointment,appointments_json,calandar,stufflist,editAppointment,updateAppointmentStatus,deleteAppointment,appointmentDetails


urlpatterns = [
    path('',index,name="index" ),
    path('appointments/appointmentsList/',appointmentsList,name="appointmentsList" ),
    path('appointments/bookAppointment/',book_appointment,name='bookAppointment'),
    path('appointment/edit/<int:appointment_id>/', editAppointment, name='editAppointment'),
    path('appointment/editStatus/<int:appointment_id>/<str:new_status>/', updateAppointmentStatus, name='editAppointmentStatus'),
    path('appointments/delete/<int:appointment_id>/', deleteAppointment, name='deleteAppointment'),
    path('appointments/calandar/appointmentDetails/<int:appointment_id>/', appointmentDetails, name='appointmentDetails'),


    path('appointments/calandar/appointments-json/', appointments_json, name='appointments-json'),
    path('appointments/calandar/', calandar, name='calandar'),
    path('staff/staffList/', stufflist, name='staffList'),
   
    
]
