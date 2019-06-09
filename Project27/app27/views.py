from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

class OpenSend(View):
    def post(self,request):
        return HttpResponse("Post is Clicked")
    def get(self,request):
        return HttpResponse("Get is Clicked")


def openindex(request):
    return render(request,"index.html")