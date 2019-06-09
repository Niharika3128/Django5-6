"""one2one URL Configuration

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
from app.models import Hotel,Place
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name="index.html")),
    path('addplace/',CreateView.as_view(model=Place,template_name="addplace.html",fields=('name','address'),success_url="/index/")),
    path('addhotel/',CreateView.as_view(model=Hotel,template_name="addhotel.html",fields=('place','serves_hot_dogs','serves_pizza'),success_url="/index/")),
    path('viewhotel/',ListView.as_view(template_name="viewhotel.html",model=Hotel)),
    path('viewplace/',ListView.as_view(template_name="viewplace.html",model=Place))
]
