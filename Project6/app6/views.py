from django.shortcuts import render

def showindex(request):
    details = {"idno":101,"name":"Ravi","salary":125000.00}
    return render(request,"index.html",{"emp":details})