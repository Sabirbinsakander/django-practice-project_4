from django.shortcuts import render
#from django.http import HttpResponse

#/Users/user/django/project_2/templates
def index(request):
    return render(request,'index.html')