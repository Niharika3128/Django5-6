from django.shortcuts import render

def showIndex(request):
    d1 = {
    101:{"name":"Ravi","salary":125000.00},
    102:{"name":"kumar","salary":185000.00},
    103:{"name":"Mohan","salary":100000.00}
    }

    return render(request,"index.html",{"data":d1})
