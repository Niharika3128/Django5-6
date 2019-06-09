from django.shortcuts import render
from .models import Article

def showIndex(request):
    qs = Article.objects.all()
    return render(request,"index.html",{"data":qs})