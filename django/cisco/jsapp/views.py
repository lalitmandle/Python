from django.shortcuts import render

# Create your views here.
def jsview(request):
    return render(request,'js.html')