from django.shortcuts import redirect
from django.views.generic import RedirectView

def openFB(request):
    return redirect("http://www.facebook.com")

class MyGoogle(RedirectView):
    url = "http://www.google.com"