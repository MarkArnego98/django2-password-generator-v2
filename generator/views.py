from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    #return HttpResponse('Hello world!')
    return render(request, 'generator/home.html',)

def password(request):
    #return HttpResponse('<h1>Eggs are awesome!</h1>')

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('%$@^%!@&!(@*!@*)'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    length = int(request.GET.get('length',12))

    thePassword = ''
    for x in range(length):
        thePassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thePassword})

"""

Challenge #1

Create an about page and link it from the Home page

"""

def about(request):
    return render (request, 'generator/about.html')