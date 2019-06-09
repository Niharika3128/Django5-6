from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product

def showProducts(request):
    pageno = request.GET.get("pageno")
    qs = Product.objects.all()
    p = Paginator(qs,3)
    if pageno == None:
        pa = p.page(1)
        return render(request,"index.html",{"data":pa})
    else:
        pa = p.page(pageno)
        return render(request,"index.html",{"data":pa})


