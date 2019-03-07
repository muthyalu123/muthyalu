from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
def home(request):
    return render(request,'home.html')
def photos(request):
    return render(request,"photos.html")
def templeplan(request):
    return render(request,"temple-plan.html")
def programs(request):
    return render(request,"programs.html")
def contactus(request):
    return render(request,"contactUs.html")
def register(request):
    return render(request,"form.html")
def submit(request):
    t1=request.GET['FirstName']
    contest={'raju': t1}
    return render(request,"form1.html", contest)
# Create your views here.
