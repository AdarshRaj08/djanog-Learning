from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('student/<int:my_id>/',views.showformdata,name='student'),
] 
