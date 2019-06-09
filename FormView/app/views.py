from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import EmployeeForm

class MainPage(FormView):
    form_class = EmployeeForm
    template_name = "index.html"

    def form_valid(self, form):
       
        return super().form_invalid(form)


# def saveDB(request):
#     id = request.POST.get("idno")
#     na = request.POST.get("name")
#     sal = request.POST.get("salary")
#     uname = request.POST.get("username")
#     upass = request.POST.get("password")
#
#     print(id,na,sal,uname,upass)
#     return redirect('/index/')