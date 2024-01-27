from django.shortcuts import render, redirect
from .import models

# Create your views here.
def home(request):
    return render(request,'VotingApp/home.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        userprofile=models.UserProfile.objects.filter(emailid=email,password=password).values()
        if userprofile==None:
            return render(request,'VotingApp/login.html')
        else:
            context={'email':email}
            return render(request,'VotingApp/home.html',context=context)
    else:
        return render(request,'VotingApp/login.html')

def  registration(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        dob=request.POST['dob']
        gender=request.POST['gender']
        location=request.POST['location']

        userprofile=models.UserProfile(username=name,emailid=email,password=password, dob=dob,gender=gender, location=location)
        userprofile.save()
        return redirect('login')
    else:
        return render(request,'VotingApp/registration.html')

def  vote(request):
    return render(request,'VotingApp/vote.html')

def  can(request):
    return render(request,'VotingApp/can.html')

from .import models
def  result(request):
    return render(request,'VotingApp/result.html')

'''def signup(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        dob=request.POST['dob']
        gender=request.POST['gender']
        location=request.POST['location']
        userprofile=models.UserProfile(username=name,emailid=email,dob=dob,gender=gender, location=location)
        userprofile.save()
        return redirect('login')'''



