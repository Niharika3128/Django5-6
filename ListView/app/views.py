from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from django.views.generic import ListView
from django.views.generic import DetailView

class Save(View):
    def post(self,request):
        id = request.POST.get("t1")
        na = request.POST.get("t2")
        sal = request.POST.get("t3")
        Employee(idno=id,name=na,salary=sal).save()
        return render(request,"index.html",{"message":"Saved"})


class ViewAll(ListView):
    model = Employee
    template_name = "all.html"


class ShowOne(DetailView):
    model = Employee
    template_name = "one.html"
