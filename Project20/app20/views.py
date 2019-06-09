from django.shortcuts import render
from .forms import EmployeeForm
from .models import EmployeeModel
from django.http import HttpResponse
import csv

def showindex(request):
    ef = EmployeeForm()
    return render(request,"index.html",{"form":ef})


def saveDetails(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    sal = request.POST.get("salary")
    EmployeeModel(idno=idno,name=name,salary=sal).save()

    ef = EmployeeForm()
    return render(request, "index.html", {"form": ef})


def employeeDownload(request):
    qs = EmployeeModel.objects.all()
    res = HttpResponse(content_type="text/csv")
    res['Content-Disposition'] = 'attachment; filename="employee.csv'
    write = csv.writer(res)
    for x in qs:
        write.writerow([x.idno,x.name,x.salary])

    return res