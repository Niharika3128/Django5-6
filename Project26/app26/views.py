from django.http import HttpResponse
from django.shortcuts import render


def showindex(request):
    return render(request,"index.html")

def openSend(request):
    if request.method == "POST":
        return HttpResponse("Clicked Post Button")
    if request.method == "GET":
        return HttpResponse("Clicked Get Button")