
from django.shortcuts import render

def showindex(request):
    return render(request,"mian_page.html",{"name":"Sathya Tech"})