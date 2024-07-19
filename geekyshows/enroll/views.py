from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.


# here it is for sign_up
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully !!')
            fm = SignUpForm()


    else:
        fm = SignUpForm()
    return render(request,'enroll/signup.html',{'form':fm})


# here it is for Login View
def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in successfully !!')
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request, 'enroll/login.html',{'form':fm})

def user_profile(request):
    return render(request,'enroll/profile.html')

def home(request):
    return HttpResponse('hii this is home')