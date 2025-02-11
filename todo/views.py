from django . shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO

def signup(request):
    if request.method=='POST':
     fname=request.POST.get('fname')
     emailid=request.POST.get('email')
     password=request.POST.get('password')
     print(fname,emailid,password)
     my_user=User.objects.create_user(fname,emailid,password )
     my_user.save()
     return redirect('/loginn')



    return render(request, 'signup.html')
    