from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

from app.models import Employee


class NewEmployee(CreateView):
    model = Employee
    template_name = "newemployee.html"
    fields = ('idno', 'name', 'age', 'contactno', 'email','doj')
    success_url = '/index/'


class DeleteEMP(DeleteView):
    model = Employee
    template_name = "deleteconform.html"
    success_url = '/viewall/'


class UpdateEMP(UpdateView):
    model = Employee
    template_name = "update.html"
    fields = ('name', 'age', 'contactno', 'email')
    success_url = '/viewall/'
