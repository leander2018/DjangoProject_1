
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,logout,login
from .  models import Profile
from django.contrib import messages
# Create your views here.

def register(request):
    # return HttpResponse('registered')
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        Username=request.POST['Username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        Phone_no = request.POST['Phone_no']
        email = request.POST['email']
        about = request.POST['about']
        gender = request.POST['gender']

        # username=first_name.capitalize()+' '+last_name[0].upper()

        if password1==password2:
            if User.objects.filter(username=Username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email exists')
                return redirect('register')
            elif Profile.objects.filter(Phone=Phone_no).exists():
                messages.info(request, 'mobile number exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=Username,password=password1,email=email,first_name=first_name,
                                      last_name=last_name)
                user.save()

                user = authenticate(request,username=Username, password=password1)
                if user is not None:
                    login(request,user)
                    p=Profile(user_id=request.user.id,about=about,Phone=Phone_no,email=email,gender=gender,)
                    p.save()
                    logout(request)
                    return redirect('login')

        else:
            messages.info(request,'password not matching')
            return redirect(register)
    else:
        return render(request,'register.html',)


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        # if User.objects.filter(username=username).exists() and User.objects.filter(password=password).exists():
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            # return HttpResponse('''logged in <a href='http://127.0.0.1:8000/accounts/logout'>logout</a>''')
            return redirect('''http://127.0.0.1:8000/''')
        else:
            messages.info(request,'Incorrect Username or Password')
            return  redirect(user_login)
                # return HttpResponse('not logged in')
    else:
        return render(request,'login.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(user_login)
    else:
        return HttpResponse('''already logged out<br> <a href=http://127.0.0.1:8000/accounts/login>click here</a> to
        login''')
        # return HttpResponse('''< meta http - equiv = "Refresh" content = "0; url='https://www.w3docs.com'" / >''')
