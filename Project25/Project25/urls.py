"""Project25 URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Project25 import settings
from app25 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.showIndex,name="main"),
    path('storeincokkie/', views.storeInCokkie,name="storeincokkie"),
    path('showcookies/',views.showcookies,name="showcookies"),
    path('removecookie/',views.removecookie,name="remove"),
    path('loginuser/',views.showloginpage,name="loginuser"),
    path('logincheck/',views.logincheck,name="logincheck")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
