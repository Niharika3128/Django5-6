from django.shortcuts import render,redirect

def show(request):
    return render(request,"index.html")


def sendComment(request):
    email = request.POST.get("t1")
    comm = request.POST.get("t2")

    value = request.session.get("email","sathya")
    print(value)

    value1 = request.session["email"]
    print(value1)