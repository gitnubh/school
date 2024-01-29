from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('credentials:login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username Already Exists")
            return redirect('credentials:register')
        elif password!=confirm_password:
            messages.info(request,"Password is not matching")
            return redirect('credentials:register')
        else:
            user = User.objects.create_user(username=username,password=password)
            user.save()
            return redirect('credentials:login')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')