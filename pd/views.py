from django.shortcuts import render
from django.http import HttpResponse

def say(request):
    return HttpResponse('hello')

def first(request):
    return render(request, 'first.html')
