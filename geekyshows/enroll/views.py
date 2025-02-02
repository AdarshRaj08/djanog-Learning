from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.models import User

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
    # request.user.is_authenticated: it will check if the user is logged in or not 
    if not request.user.is_authenticated:
        if request.method == "POST":
            # AuthenticationForm Needs request: Provides access to authentication backends.,Allows handling of request-specific context, which might be necessary for certain authentication processes.
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
    else:
        return HttpResponseRedirect('/profile/')


# Profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
            #  request.POST binds the submitted data to the form.
            # instance=request.user ties the form to the current user instance.
                fm = EditAdminProfileForm(request.POST,instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST,instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request,'Profile Updated !!!')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance = request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance = request.user)
                users = None
        return render(request,'enroll/profile.html',{'name':request.user.username,'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/login/')


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# change password with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # when we change password then we logged out 
                # update_session_auth_hash is essential when you want to keep the user logged in after they change their password. 
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request,'enroll/changepass.html',{'form':fm})

    else:
        return HttpResponseRedirect('/login/')


# change password without old password
def user_change_pass1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # when we change password then we logged out 
                # update_session_auth_hash is essential when you want to keep the user logged in after they change their password. 
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user = request.user)
        return render(request,'enroll/changepass1.html',{'form':fm})

    else:
        return HttpResponseRedirect('/login/')
    

def user_detail(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditUserProfileForm(instance=pi)
        return render(request,'enroll/userdetail.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')