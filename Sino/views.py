from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
import datetime 
from django.contrib.auth.models import Group
from .forms import CreateUserForm , OrderForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user, admin_only
# from openpyxl import Workbook
# from openpyxl.utils import get_column_letter
# from openpyxl.styles import Font


# @unauthenticated_user

@login_required(login_url='login')
@admin_only
def index(request):
    products=Person.objects.all()
    dat=datetime.datetime.now()
    usr=request.POST.get('userna')
    pword=request.POST.get('passwo')
    pf=request.POST.get('pw1')
    params = {'products':products, 'date':dat, 'name':usr, 'pass':pf}
    return render(request,'index.html',params)

@login_required(login_url='login')
def atmlogin(request):
    dat=datetime.datetime.now()
    params = {'date':dat,}
    return render(request,'ATM.html',params)

@login_required(login_url='login')
def bluebox(request):
    dat=datetime.datetime.now()
    params = {'date':dat,}
    return render(request,"Bluebox.html",params)

@login_required(login_url='login')
def workSchedule(request):
    dat=datetime.datetime.now()
    params = {'date':dat,}
    return render(request, 'Workschedule.html',params)

@login_required(login_url='login')
def Raise(request):
    dat=datetime.datetime.now()
    params = {'date':dat,}
    return render(request,'Raise.html',params) 

@login_required(login_url='login')
def customer(request):
    return render (request,'customer.html')

def createOrder(request):
    form = OrderForm()
    context= {'form':form}
    if request.method=='POST':
        
       form = OrderForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/')
    return render(request, 'createorderform.html',context)    

    # engine =pyttsx3.init()
    # p = engine.say('HELLO SIR')
    # hel=engine.runAndWait()



    
    

def confirm(request):
    pword=request.POST.get('passwo')
    pf=request.POST.get('pw1')
    usr=request.POST.get('userna')
    dat=datetime.datetime.now()
    if pword==pf:
        params = {'date':dat, 'name':usr, 'pass':pword}
        return render(request,'confirm.html',params)
    else:
        return HttpResponse ('''ERROR-404-NOT-FOUND''') 
# Create your views here.
# wb = Workbook()
# ws = wb.active
# ws.title ="New Data"
# headings = ['Name'] + list(products.keys())
# ws.append(headings)
# for person in products:
#     grades = list(products[person].values())
# ws.append([person] + grades)
# for col in range(2,len(products["Joe"])+2):
#     char = get_column_letter(col)
#     ws[char+"7"] = f"=SUM({char+'2'}:{char+'6'})/{len(products)}"
# wb.save("NewAutom.xlsx")


def loginpage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'INCORRECT USERNAME OR PASSWORD! TRY AGAIN')

            
    context = {}
    return render(request, 'login.html', context)


def registrationpage(request):
    form = CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get('username')
            
            group =Group.objects.get(name="Customer")
            user.groups.add(group)
            messages.success(request, 'Account Created Successfully for ' + username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')