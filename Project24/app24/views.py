from django.shortcuts import render
from django.http import HttpResponse


def showindex(request):
    return render(request,"index.html")


def setCookie(request):
    res = HttpResponse("Cookie Set")
    res.set_cookie("k1","This is Naveen")
    return res


def getCookie(request):
    val = request.COOKIES["k1"]
    return HttpResponse(val)