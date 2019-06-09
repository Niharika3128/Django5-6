from django.shortcuts import render


def showIndex(request):
    return render(request,"index.html")


def showDetails(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    contact = request.POST.get("t3")

    d1 = {"na":name,"age":age,"cno":contact}

    return render(request,"details.html",{"data":d1})