from django.http import HttpResponse
from django.shortcuts import render

# /products -> index

# Created a view function
def index(request):
    return HttpResponse('Hello World')

def new(request):
    return HttpResponse('New window')