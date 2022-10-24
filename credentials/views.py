
from http.client import HTTPResponse
from pickle import NONE
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

#register fuctionality

def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pswd=request.POST['pswd']
        cpswd=request.POST['cpswd']

        if pswd==cpswd: 

                if User.objects.filter(username=uname).exists():
                    print('username already exist!!')
                    messages.info(request,"user already exists")
                    return  redirect('register')
                    
                else:

                    user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pswd)
                    user.save()
                    return  redirect('login')

        else:
            messages.info(request,"passwords didn't mach")
            return  redirect('register')

    return render(request,'register.html')


#login fuctionality
def login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pswd=request.POST['pswd']

        user=auth.authenticate(username=uname,password=pswd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return  render(request,'login.html')   

#logout functionality

def logout(request):
    auth.logout(request)
    return redirect('/')

   