from django.shortcuts import render
from .forms import EmployeeForm
from .models import EmployeeModel
from Project19 import settings

from django.core.mail import send_mail

def showindex(request):
    form = EmployeeForm()
    return render(request,"index.html",{"form":form})


def saveDetails(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    email = request.POST.get("email")

    send_mail("Registration Mail",
              "Hello User "+name+" Your Account is Created\n"
                                 "For More Information Please call us on 9052492329",
              settings.EMAIL_HOST_USER,
              [email])


    EmployeeModel(idno=idno,name=name,email=email).save()
    form = EmployeeForm()
    return render(request,"index.html",{"form":form})