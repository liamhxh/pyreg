from django.shortcuts import render, redirect
from models import *
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    return render (request, 'registerandlogin/index.html')

def reg(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            User.objects.create(
                fname = request.POST['fname'], 
                lname = request.POST['lname'], 
                email = request.POST['email'], 
                password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()),
                cpassword = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()),
                )
            return redirect('/successfulReg')

def successfulReg(request):
    return render(request, 'registerandlogin/successfulReg.html')

def login(request):
    return redirect('/successfulLog')

def successfulLog(request):
    return render(request, 'registerandlogin/successfulLog.html')
