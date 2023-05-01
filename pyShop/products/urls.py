from django.urls import path
from . import views

# 127.0.0.1:8000/products/...

# products is the root folder


# maps the root url to the view function
urlpatterns = [
    # path() function:
    # takes 2 args
    # 1st arg: URL pattern to match
    # 2nd arg: the view function

    # Note: list more specific urls first

    path('new/',views.new),
    # Makes is so when a user visits the
    # root of our app, Django will call the
    # views.index function
    path('',views.index)
]