from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("HELLO DINGA")
    
def home(request):
    return HttpResponse("<h1>Welcome to Home Page<h1>")

def html_demo2(request):
    return render(request,"sample05.html")

def home1(request):
    return render(request,"directory/sample04.html")