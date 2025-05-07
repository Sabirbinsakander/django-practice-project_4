from django.http import HttpResponse

def home(request):
    return HttpResponse("This Home page")
def contacts(request):
    return HttpResponse("This is contact page")