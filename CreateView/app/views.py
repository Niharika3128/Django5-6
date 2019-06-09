from django.shortcuts import render
from django.views.generic import CreateView
from .models import Employee

class CreateNewEmployee(CreateView):
    model = Employee
    template_name = "index.html"
    fields = ('idno','name','salary')
    success_url = '/main/'
