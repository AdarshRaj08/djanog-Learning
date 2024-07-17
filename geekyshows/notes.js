/*
# Dynamic initial values
#   - used to declare the initial value of form fields at runtime.

def showformdata(request):
    fm = StudentRegistration(label_suffix=' ',initial={'name':'Adarsh','email':'adarshraj2122@gmail.com'})
    
    # by this you can give manual order to the fields
    fm.order_fields(field_order=['email','name'])
    return render(request, 'extra/form.html',{'form':fm})

*/


