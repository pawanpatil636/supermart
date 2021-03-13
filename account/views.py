from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        username=request.POST['user_name']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        mobile_number=request.POST['mobile-number']
        DOB =request.POST['dateofbirth']
        gender=request.POST['gender']
        age=request.POST['age']
        password=request.POST['password']
        password1=request.POST['password1']

        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        user.save()
        account =Account(user=user,age=age,mobile_number=mobile_number, DOB=DOB, gender=gender)
        account.save()
        return redirect("/account/login/")

    return render(request,'account/register.html')

def logins(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            username=request.POST['user_name']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password) 
            if user is not None:
                login(request,user)
                if request.user.is_superuser:
                    return redirect('/bazzar/add-product') 
                else:
                    return redirect('/')
        return render(request,'account/login.html')
    else:
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect("/account/login/")


def account_view(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(id=pk)
        return render(request,'account/account.html',{'user':user})
    


