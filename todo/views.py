from django . shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO
from django.contrib.auth import authenticate,login,logout

def signup(request):
    if request.method=='POST':
     fname=request.POST.get('fname')
     emailid=request.POST.get('email')
     password=request.POST.get('password')
     print(fname,emailid,password)
     my_user=User.objects.create_user(fname,emailid,password )
     my_user.save()
     return redirect('/login')

    return render(request, 'signup.html')


def user_login(request):
   if request.method=='POST':
      fname=request.POST.get('fname')
      password=request.POST.get('password')
      print(fname,password)
      users=authenticate(request,username=fname,password=password)
      if users is not None:
         login(request,users)
         return redirect('/todopage')
      else:
         return redirect('/login')
         
   return render(request,'login.html')

def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        object = models.TODOO(title=title, user=request.user)  # Fix: Change 'users' to 'user'
        object.save()
        res = models.TODOO.objects.filter(user=request.user).order_by('-date')  # Fix: Change 'users' to 'user'
        return redirect('/todopage')

    res = models.TODOO.objects.filter(user=request.user).order_by('-date')  # Fix: Change 'users' to 'user'
    return render(request, 'todo.html', {'res': res})

def edit_todo(request,srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        object = models.TODOO.objects.get(srno=srno)
        object.title=title
        object.save()
        user=request.user
        res = models.TODOO.objects.filter(user=request.user).order_by('-date')  # Fix: Change 'users' to 'user'
        return render(request, 'todo.html', {'res': res})


    object = models.TODOO.objects.get(srno=srno)
    res = models.TODOO.objects.filter(user=request.user).order_by('-date')  # Fix: Change 'users' to 'user'
    return render(request, 'todo.html')
