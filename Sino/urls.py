from django.urls import path 
from django.contrib import admin
from . import views



urlpatterns = [
    path('',views.index,name='home'),
    path('confirm', views.confirm),
    path('registration/',views.registrationpage,name='registartion'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('atm/',views.atmlogin, name= 'atm-page'),
    path('bluebox/',views.bluebox,name='bluebox'),
    path('Workschedule/',views.workSchedule,name='Workschedule'),
    path('Raise/',views.Raise,name='Raise'),
    path('home/',views.customer,name='customer'),
    path('createorder/',views.createOrder,name='order')

]



admin.site.site_header = 'Shop Admin'
