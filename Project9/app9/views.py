from django.shortcuts import render

def showindex(request):
    return render(request,"index.html")

def saveStudentDetails(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    contact = request.POST.get("t3")
    gender = request.POST.get("rb")
    langs = request.POST.getlist("cb")
    if langs == []:
        langs = "Please select 1 Language"
    else:
        if len(langs)== 1 and langs[0] == "Core Python":
            langs = "Core Python is Free Select Other than That"

    faculty = request.POST.get("fa")

    d1 = {"name": name, "age": age, "contact": contact, "gen": gender, "languages": langs,"faculty":faculty}

    return render(request,"details.html",{"data":d1})