# Django Program

-------------------------- Configuration --------------------------
To install: pip3 install django

Create a new django projct named 'pyshop' in the current directory
a. python3 -m django startproject pyshop .

Start development server in django and it will give the url
b. python3 manage.py runserver

--------------------------------------------------------------------

------------------------ Creating a new path -----------------------
A. Ensure the path to the app is defined inside the urls.py in the root folder and that the url to the app is valid
i.e. "path('products/', include('products.urls'))," tells django that any url with 'products/' is sent to the 'url' module in the 'products' app

B. Once inside the 'urls' module for the app go to 'urlpatterns' list. There define a path function to guide
the request where to go.
i.e. "path('new/',views.new)," from the path root/new/ it will return the output from the new function in view.

C. Ensure a views module is defined. There define a function
to for the specific request you wanted. In our example we would need to define a "def new(request) ... " function.

--------------------------------------------------------------------

-------------------------- Concepts/Ideas --------------------------
Difference between root folder versus other folders in the project:

In a Django project the root folder has the same name as the project
itself.
Other folders in the Django project is a Django app inside the
project. An app encapsulates a specific functionality of your project
and are orgainized aroudn a specific feature. 

--------------------------------------------------------------------
