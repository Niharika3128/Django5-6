from django.http import HttpResponse
from .models import Person


def showindex(request):
    p = Person(fname="Ravi", lname="kumar", contact=123456)
    p.save()
    return HttpResponse("Object is Created and Saved")

def readall(request):
    qs = Person.objects.all()
    print(qs)
    for x in qs:
        print(x.fname)
        print(x.lname)
        print(x.contact)
        print("----------------------")
    return HttpResponse("Reading all")

def updateone(request):
    Person.objects.filter(id=3).update(fname="Krishna")
    Person.objects.filter(id=4).update(contact=9052492329)
    return HttpResponse("updated")

def deleteone(request):
    t1 = Person.objects.filter(id=3).delete()
    if t1[0] == 0:
        print("no record is available")
    else:
        print("is deleted")

    return HttpResponse("deleted")


def readingall(request):
    qs = Person.objects.all()
    for x in qs:
        print(x.id,"--",x.fname,"--",x.lname,"--",x.contact)
    return HttpResponse("All")



def readone(request):
    qs = Person.objects.filter(id=555)
    for x in qs:
        print(x.id, "--", x.fname, "--", x.lname, "--", x.contact)
    return HttpResponse("One")


def readallexcept555(request):
    qs = Person.objects.exclude(id=555)
    for x in qs:
        print(x.id,"--",x.fname,"--",x.lname,"--",x.contact)
    return HttpResponse("All")

def read1stFive(request):
    qs = Person.objects.all()[:5]
    for x in qs:
        print(x.id,"--",x.fname,"--",x.lname,"--",x.contact)
    return HttpResponse("All")

def readMatchingNames(request):
    qs = Person.objects.filter(fname="AA")
    print(qs)
    for x in qs:
        print(x.id, "--", x.fname, "--", x.lname, "--", x.contact)
    return HttpResponse("AA")

def readId(request):
    obj = Person.objects.get(id=666)
    print(obj)
    print(obj.id, "--", obj.fname, "--", obj.lname, "--", obj.contact)
    return HttpResponse("666")
