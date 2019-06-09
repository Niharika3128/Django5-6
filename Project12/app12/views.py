from django.shortcuts import render
from .forms import EmployeeForm

def showIndex(request):
    form = EmployeeForm()
    return render(request,"index.html",{"form":form})