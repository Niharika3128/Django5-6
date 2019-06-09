from django.shortcuts import render
from .forms import EmployeeForm

def showindex(request):
    return render(request,"index.html",{"form":EmployeeForm()})