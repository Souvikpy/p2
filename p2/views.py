from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("HELLO DINGA")
    
def home(request):
    return HttpResponse("<h1>Welcome to Home Page<h1>")

def html_demo2(request):
    return render(request,"sample05.html")

def sample1(request):
    return render(request,"directory/sample01.html", context={'data':"Souvik",'name':"Sumon"})

def sample2(request):
    fruits = ['apple','mango','grape','banana']
    return render(request,"directory/sample02.html",{'fruits':fruits})

def sample3(request):
    return render(request,"directory/sample03.html",{'a':10,'b':20})

def sample4(request):
    return render(request,"directory/sample04.html")
