from django.http import HttpResponse
def showDetails(request):
    code = "<html><body bgcolor=yellow><h1>Welcome to Djngo</h1><h3>Hello Django Students</h3></body></html>"
    return HttpResponse(code)
