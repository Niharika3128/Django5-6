"""Many2Many_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView, CreateView, ListView

from app2 import views
from app2.models import Course,Student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name="index.html")),
    path('addcourse/',CreateView.as_view(model=Course,template_name="addcourse.html",fields=("name",),success_url="/addcourse/")),
    path('addstudent/',CreateView.as_view(model=Student,template_name="addstudent.html",fields=("name","join_course"),success_url="/addstudent/")),
    path('allstudents/',ListView.as_view(model=Student,template_name="allstudents.html"))
]
