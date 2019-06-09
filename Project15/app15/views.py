from django.shortcuts import render
from .models import Employee


def generateAutoEmployeeID():
    qs = Employee.objects.all()
    if qs:
        length = len(qs)
        return qs[length-1].idno + 1
    else:
        idno = 101
        return idno


def showIndex(request):
    idno = generateAutoEmployeeID()
    qs = Employee.objects.all()
    return render(request,"index.html",{"auto_idno":idno,"data":qs})


def saveDetails(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")

    Employee(idno=idno,name=name,salary=salary).save()
    idno = generateAutoEmployeeID()
    qs = Employee.objects.all()
    return render(request, "index.html", {"auto_idno": idno, "data": qs})


def deleteEmployee(request):
    id = request.GET.get("del_id")
    Employee.objects.filter(idno=id).delete()
    qs = Employee.objects.all()
    idno = generateAutoEmployeeID()
    return render(request,"index.html",{"auto_idno":idno,"data":qs})


def updateEmployee(request):
    id = request.POST.get("update_id")
    emp = Employee.objects.get(idno=id)
    return render(request,"update.html",{"data":emp})