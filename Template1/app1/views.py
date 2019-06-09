from django.shortcuts import render


def showIndex(request):
    a = 100
    name = "Sathya"
    marks = [5,8,-1,45,14,59,45,6,2,-20]
    emp = {"idno":101,"name":"Ravi","salary":125000.00}
    return render(request,"index.html",{
        "data1":a,
        "data2":name,
        "data3":marks,
        "data4":emp})


def showIndex1(request):
    fname = None  # None means False
    lname = "Ravi Kumar"
    return render(request,"index1.html",
                  {"data1":fname,
                   "data2":lname})


def showIndex2(request):
    names = ["Ravi","kumar","mohan","krishna","Prasad"]

    return render(request,"index3.html",
                  {"data1":names})







