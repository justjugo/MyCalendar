
from django.contrib.auth import views 
from django.urls import path
from .views import login,signup


urlpatterns = [
   
    path('signup/', signup,name='signup'),

   
]
