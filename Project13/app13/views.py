from django.shortcuts import render
from .forms import EmployeeForm
from .models import EmployeeModel

def showindex(request):
    ef = EmployeeForm()
    return render(request,"index.html",{"form":ef})


def saveDetails(request):
    id = request.POST.get("idno")
    na = request.POST.get("name")
    sal = request.POST.get("salary")

    res = EmployeeModel.objects.filter(idno=id)
    if res:
        return render(request,"index.html",{"message":"IDNO is available","form":EmployeeForm()})
    else:
        EmployeeModel(idno=id,name=na,salary=sal).save()
        qs = EmployeeModel.objects.all()
        return render(request,"details.html",{"data":qs})


