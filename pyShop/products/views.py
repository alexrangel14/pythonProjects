# views.py: handles incoming HTTP requests and returns HTTP resonses
# Functions defined here return the type of view you want the screen to 
# have. Given power by their request.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /products -> index

# Only returns the words "new window", when called 
def new(request):
    return HttpResponse('New window')

# More complicated screen return, where it goes to another file in this case
# an html file where what the screen will display depends on that html

# Renders the contents of an HTML template 'index.html' and returns is an an
# HTML response

# request: Instance of the 'HttpResquest' provided by Django.
# contains information about the current HTTP request including the request
# method (GET, POST, etc.), headers, and query parameters
def index(request):
    # products: retrieves all 'Product' objects from the database
    products = Product.objects.all()
    # render: returns an HttpResponse object containing the rendered HTML
    # content. As args it takes the passed in 'request' object, the name of the
    # HTML template to use 'index.html', and a dictionary that contains the
    # data to be passed to the template 'index.html
    return render(request, 'index.html',{'products':products})


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')


def cart(request):
    return render(request,'cart.html')

