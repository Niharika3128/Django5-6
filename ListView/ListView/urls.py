"""ListView URL Configuration

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
from django.views.generic import TemplateView
from django.views.generic import ListView
from app.models import Employee

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html")),
    path('save/',views.Save.as_view(),name="save"),
    path('viewall/',views.ViewAll.as_view(),name="viewall"),
    path('viewallids/',ListView.as_view(model=Employee,template_name="allids.html"),name="viewallids"),
    path('showone<int:pk>/',views.ShowOne.as_view())

]
