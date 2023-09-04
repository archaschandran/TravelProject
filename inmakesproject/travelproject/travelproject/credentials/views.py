from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password) #here user is a variable

        if user is not None:
            auth.login(request,user) #login to user
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method == "POST":
        user_name=request.POST['username']
        first=request.POST['first_name']
        last=request.POST['last_name']
        email=request.POST['email']
        password = request.POST['password']
        cpassword= request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=user_name).exists(): #to check whether given username already exist
                messages.info(request,"username already taken") #to give message
                return redirect('register') # redirect to registration page

            elif User.objects.filter(email=email).exists(): #to check whether given username already exist
                messages.info(request,"email already taken") #to give message
                return redirect('register') # redirect to registration page
            else:
                user = User.objects.create_user(username=user_name, password=password, first_name=first, last_name=last,
                                                email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/') # return to home page
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
