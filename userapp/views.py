
from lib2to3.pgen2 import token
from tkinter import N
from urllib.request import proxy_bypass
from django.shortcuts import render, redirect
from . models import *
import uuid
from django.contrib import messages
from .emailmssg import send_forgetpass_mail

# Create your views here.


def funIndex(request):
    return render(request, 'index.html')


def funLogin(request):
    return render(request, 'login.html')


def funViews(request):
    try:
        if request.method == 'POST':
            username = request.POST['email']
            print('ooooo')
            password = request.POST['password']
            obj_log = RegisterTable.objects.get(
                email=username, password=password)
            request.session['user'] = obj_log.id
            obj_2 = RegisterTable.objects.get(id=obj_log.id)
            print(obj_log.id)
            print('working')
            return render(request, 'view.html', {'msg_log': obj_2}) 
        print('lllll')
    except Exception as e:
        print(e)
    return render(request, 'login.html', {'msg_log': 'invalid username or password'})


def funRegist(request):
    print('kkkk')
    try:
        if request.method == 'POST':
            email = request.POST['email']
            obj_2 = RegisterTable.objects.filter(email=email).exists()
            if(obj_2 == False):
                firstname = request.POST['name']
                phonenumber = request.POST['phonenumber']
                password = request.POST['pass']
                day = request.POST['day']
                print(day)
                month = request.POST['month']
                year = request.POST['year']
                dob = year+'-'+month+'-'+day
                gender = request.POST['gender']
                obj_1 = RegisterTable(firstname=firstname, phonenumber=phonenumber,
                                      email=email, password=password, dob=dob, gender=gender)
                obj_1.save()
                print(firstname, phonenumber)
                return render(request, 'register.html', {"msg2": 'create successfully and   loging user page'})
            else:
                return render(request, 'register.html', {'msg1': '*emali is already exists'})
    except Exception as e:
        print(e)
    return render(request, 'register.html')


# change password functio

def funChangePass(request, token):
    print('passChange')
    context = {}
    try:
        pro_pass = ProfileUser.objects.filter(forget_pass_token=token).first()
        
        if request.method=='POST':
            new_pass=request.POST['pass']
            con_pass=request.POST['conpass']
            user_id=request.POST['user_id']
            
            if user_id is None:
                messages.success(request, 'No user ID found')
                return redirect(f'/changepass/{token}/')
            
            
            if new_pass!=con_pass:
                messages.success(request, 'Passwords Not equal')
                return redirect(f'/changepass/{token}/')
                
            user_obj=RegisterTable.objects.get(id=user_id)
            user_obj.password=new_pass
            user_obj.save()
            return redirect('/viewspage/')
            
        context={'user_id':pro_pass.user.id}

    except Exception as e:
        print(e)
    return render(request, 'changepassword.html',context)


def funForgetPass(request):
    try:
        if request.method == 'POST':
            username = request.POST['email']
            print('forgetpass')

            if not RegisterTable.objects.filter(email=username).first():
                messages.success(request, 'Not user found with this email.')
                return redirect('/forgetpass/')
            user_obj = RegisterTable.objects.get(email=username)
            emails = [user_obj.email]
            print(user_obj.email)
            print('step3')
            token = str(uuid.uuid4())
            print(token)
            pro_pass = ProfileUser(user=user_obj)
            print('step4')
            pro_pass.forget_pass_token = token
            pro_pass.save()
            print('ste5')
            print(pro_pass.forget_pass_token)
            send_forgetpass_mail(emails, token)
            messages.success(request, 'An email is send.')
            return redirect('/forgetpass/')
    except Exception as e:
        print(e)
    return render(request, 'forgetpass.html')

#logout
def funLogout(request):
    del request.session['user']
    return render(request,'login.html')