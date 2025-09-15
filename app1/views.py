from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


def SignupPage(request):
    if request.method=='POST':
        fullName=request.POST.get('fullName')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(fullName,email,phone,pass1,pass2)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        fullName=request.POST.get('fullName')
        pass1=request.POST.get('pass')
        user=authenticate(request,fullName=fullName,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("fullName or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')