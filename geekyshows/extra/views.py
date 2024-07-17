from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.


# Dynamic initial values
#   - used to declare the initial value of form fields at runtime.

def home(request):
    return render(request,'extra/home.html')


def showformdata(request,my_id):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
    else:
        fm = StudentRegistration()
    go = {'form':fm,'my_id':my_id}
    return render(request, 'extra/form.html',go)