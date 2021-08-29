from django.http import HttpResponse
from django.shortcuts import render, redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            view_func(request,*args, **kwargs)
        return wrapper_func

def allowed_user(allowed_roles=['']):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            group = None 
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse('''<h1> Oops!! LOOKS LIKE YOU ARE NOT AUTHORIZED TO VIEW THIS PAGE</h1> <br> <h3> TRY Login With Different Account</h3>  <br><h2> <a href = '/logout/'><b>Log Out</b></a></h2>''')
        return wrapper_func
    return decorator
    
def admin_only(view_func):
    def wrapper_function(request,*args, **kwargs):
        group = None 
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group=='Atm':
            return redirect('atm-page')
        if group=="Raise":
            return redirect('Raise')
        if group=='Works':
            return redirect('Workschedule')
        if group=='Bluebox':
            return redirect('bluebox')
        if group=='Customer':
            return redirect('customer')
        if group=='Admin':
            return view_func(request,*args, **kwargs)
        
        
        if group==None:
            return HttpResponse('''<h1> Oops!! LOOKS LIKE YOU ARE NOT AUTHORIZED TO VIEW THIS PAGE</h1> <br> <h3> TRY Login With Different Account</h3>  <br><h2> <a href = '/logout/'><b>Log Out</b></a></h2>''')
    return wrapper_function


