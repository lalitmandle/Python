"""cisco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp.views import sunder,sunder1
from jsapp.views import jsview
from javascriptexternal.views import sunderview,sunderview1

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('homepage/',sunder),
    # path('homepage/',sunder1)
    path('jshome',jsview),
    path('javahome',sunderview),
    path('sunder',sunderview1)
]
