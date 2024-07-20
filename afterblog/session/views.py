from django.shortcuts import render

# session framework let's you store and retrieve arbitrary data on a per-site-visitor basis.
# it store data on the server side and abstracts the sending and receiving of cookies. Cookies contain a session Id not the data itself.
# be default, django stores sessions in your database
# as it stores sessions in database so it is mandatory to run makemigrations and migrate to use session. It will create required tables.

# by default the age of the session is 2 weeks even if we close the browser

# Methods in session
#   1. keys    2. lists      3. flush()     4. setdefault

# 5. {{request.session.get_session_cookie_age}} <br>
# 6. {{request.session.get_expiry_age}} <br>
# 7. {{request.session.get_expiry_date}} <br>
# 8. {{request.session.get_expire_at_browser_close}} <br>
#  you can also use this in the view.py 

# 9.  set_expiry(600)
# 10. clear_expired()
# 11. set_test_cookie() 
# 12. test_cookie_worked()
# 13. delete_test_cookie()

# Create your views here.

def setsession(request):
    request.session['name'] = 'Adarsh'
    request.session['lname'] = 'Raj'

    # used to set the expiry 
    request.session.set_expiry(600)
    # when set to 0 means that when browser close then the cookies will expire
    # request.session.set_expiry(0)
    return render(request,'session/setsession.html')


def getsession(request):
    # name = request.session['name']            # this is also a way
    name = request.session.get('name',default='Guest')
    lname = request.session.get('lname')

    keys = request.session.keys()
    items = request.session.items()

    # If the key 'age' already exists with a value, setdefault will return the existing value and not update it.
    # if not present age value then 21 will come
    age = request.session.setdefault('age','21')
    return render(request,'session/getsession.html',{'name':name,'lname':lname,'keys':keys,'items':items,'age':age})


def delsession(request):
    # # this will use for deleting a single key 
    # if 'name' in request.session:
    #     del request.session['name']

    # Django is used to completely clear out all session data for the current session.
    request.session.flush()

    # method used in Django to clear out expired sessions from the session store.
    # Regular maintenance to clean up old session data
    request.session.clear_expired()
    return render(request,'session/delsession.html')



# 
def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,'session/settestcookie.html')

def checktestcookie(request):
    print("ha main hoon")
    print(request.session.test_cookie_worked())
    return render(request,'session/checktestcookie.html')

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request,'session/deltestcookie.html')