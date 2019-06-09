
from django.shortcuts import render,redirect
import app25
from .models import Product,LoginDetails
from django.contrib import messages


def showIndex(request):
    qs = Product.objects.all()
    return render(request,"index.html",{"data":qs,"c_len":len(request.COOKIES)})


def storeInCokkie(request):
    pid = request.GET.get("pid")
    pname = request.GET.get("pname")
    response = redirect('/index/')
    #response = render(request,"index.html",{"data":qs,"c_len":len(request.COOKIES)})
    response.set_cookie(pid,pname)
    return response


def showcookies(request):
    keys = []
    for x in request.COOKIES.keys():
        keys.append(int(x))

    qs = Product.objects.all()

    return render(request,"cartitems.html",{"data":qs,"keys":keys})


def removecookie(request):
    id = request.GET.get("idno")

    response = redirect('/showcookies/')

    response.delete_cookie(id)
    return response


def showloginpage(request):
    return render(request,"login.html")


def logincheck(request):
    un = request.POST.get("t1")
    up = request.POST.get("t2")
    try:
        result = LoginDetails.objects.get(username=un,password=up)

        #request.session["1"] = un

        return redirect('main')

    except app25.models.LoginDetails.DoesNotExist:
        messages.error(request,"Invalid User")
        return redirect('loginuser')