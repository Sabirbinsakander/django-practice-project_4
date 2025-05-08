from django.shortcuts import render
import datetime 

# Create your views here.


def home(request):
    d = {'author' : 'Rahim', 'Age' : 15, 'list' : ['python', 'is', 'best'], 'birthday' : datetime.datetime.now() , 'courses' : [
        {
            'id' : 1,
            'name':'Python',
            'fee' : 10000
        },
        {
            'id' : 2,
            'name':'Python Django',
            'fee' : 10000
        },
        {
            'id' : 3,
            'name':'C',
            'fee' : 10000
        },
        {
            'id' : 4,
            'name':'Cpp',
            'fee' : 10000

        },
        {
            'id' : 5,
            'name':'Web Development',
            'fee' : 10000

        },
    ]}
    return render(request, 'home.html', d)
