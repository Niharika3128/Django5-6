from django.shortcuts import render
from .models import Usermodel


def showIndex(request):
    qs = Usermodel.objects.all()
    return render(request,"index.html",{"data":qs})


def savedetails(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    photo = request.FILES["photo"]

    Usermodel(idno=idno,name=name,photo=photo).save()

    qs = Usermodel.objects.all()
    return render(request, "index.html", {"data": qs})
