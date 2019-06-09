from django.shortcuts import render
from .models import Employee

def showindex(request):
    return render(request,"index.html")


def saveDetails(request):
    id = request.POST.get("t1")
    na = request.POST.get("t2")
    sal = request.POST.get("t3")
    exp = request.POST.get("t4")
    desg = request.POST.get("t5")

    e1 = Employee(idno=id,name=na,salary=sal,exp=exp,designation=desg)
    e1.save()

    return render(request,"index.html",{"message":"Employee Registered"})


def viewallEmployees(request):
    qs = Employee.objects.all()
    print(qs)
    return render(request,"viewall.html",{"data":qs})