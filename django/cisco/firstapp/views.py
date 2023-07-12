from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def sunder(request):
    return HttpResponse("Welcome to my first cisco django example")
def sunder1(request):
    return HttpResponse("<h1>welcome to python django class </h1>")