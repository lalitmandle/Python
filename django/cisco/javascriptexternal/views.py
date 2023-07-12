from django.shortcuts import render

# Create your views here.
def sunderview(request):
    return render(request,'index.html')
def sunderview1(request):
    return render(request, 'youtube.html')
