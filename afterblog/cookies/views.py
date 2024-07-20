from django.shortcuts import render,HttpResponse
from datetime import datetime,timedelta
# Create your views here.

def setcookies(request):
    response = render(request,'cookies/setcookies.html')
    # max_age 60 means that after 60 seconds the cookie will delete
    # response.set_cookie('name','Adarsh',max_age=60)
    # here cookies will expire after 2 days even if we close the website
    response.set_cookie('name','Adarsh',expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookies(request):
    # let's say above cookies were not given then the by default it show Guest
    name = request.COOKIES.get('name',"Guest")
    return render(request,'cookies/getcookies.html',{'name':name})

def delcookies(request):
    response = render(request,'cookies/delcookies.html')
    response.delete_cookie('name')
    return response