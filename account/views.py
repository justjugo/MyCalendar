from django.shortcuts import render
from django.contrib.auth import login ,authenticate
from .forms import RegistrationForm



def signup(request):

    if request.method =="POST":
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =RegistrationForm()
    return render(request,'signup.html',{'form':form})