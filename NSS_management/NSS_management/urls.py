"""NSS_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url,include
from temp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('attendance/',include('attendance.url')),
    url('complaint/',include('complaint.url')),
    url('event/',include('event.url')),
    url('gallery/',include('gallery.url')),
    url('login/',include('login.url')),
    url('points/',include('points.url')),
    url('report/',include('report.url')),
    url('staff/',include('staff.url')),
    url('vgallery/',include('vgallery.url')),
    url('volunteer/',include('volunteer.url')),
    url('temp/',include('temp.url')),
    url('$', views.home)
]