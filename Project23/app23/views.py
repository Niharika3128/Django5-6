from django.shortcuts import render

def showindex(request):
    return render(request,"index.html")


def validate(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")

    if username == "admin" and password == "sathya":
        # Writing status to Session
        request.session["status"] = True
        return render(request,"welcome.html")
    else:
        return render(request,"index.html",{"message":"Invalid User"})


def logoutuser(request):
    request.session["status"] = False
    #del request.session["status"]
    return render(request, "index.html")


def sendmail(request):
    if request.session["status"]:
        print("Mail")
    else:
        print("Please Login")
    return render(request,"welcome.html")