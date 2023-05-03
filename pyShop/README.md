# Django Program

-------------------------- Configuration --------------------------
To install: pip3 install django

Create a new django projct named 'pyshop' in the current directory
a. python3 -m django startproject pyshop .

Start development server in django and it will give the url
b. python3 manage.py runserver

--------------------------------------------------------------------

----------------------- Creating a new path ------------------------
A. Ensure the path to the app is defined inside the urls.py in the 
root folder and that the url to the app is valid
i.e. "path('products/', include('products.urls'))," tells django that 
any url with 'products/' is sent to the 'url' module in the 'products' app

B. Once inside the 'urls' module for the app go to 'urlpatterns' list. 
There define a path function to guide the request where to go.
i.e. "path('new/',views.new)," from the path root/new/ it will return 
the output from the new function in view.

C. Ensure a views module is defined. There define a function
to for the specific request you wanted. In our example we would need 
to define a "def new(request) ... " function.

--------------------------------------------------------------------

----------------------- Web Developement ---------------------------
In web development a database table (Model) is used to store and 
mangage data for an application.

Model: A representation of a real world object
Why use them? Used to make predictions or generate insights based on
data

Why create a database table with a model?
-Allows developers to work with data in Python rather than complicated
SQL queries
-Easier to modify database schema as changes can be automatically 
applied to the database through migrations

How are database tables used in web development?
Data is retrieved from a database table using queries and then
displayed to the user. (Storing and retreiving data)

So creating a database table with a model creates an easy way to work
with data in web development

--------------------------------------------------------------------

--------------- Create database table with a model -----------------

Models represent real life object
Create the model inside the app that is responsible for the functionality
it represents.

A.  In the models.py in the respective app. Create a class with the
real life object you want to represent.
I.E.
class Product(models.Model):
    // Saves text data
    name = models.CharField()
    // Saves integer data
    number = models.IntegerField()
    // Saves decimal data
    price = models.FloatField()

2A. Ensure that you've added the module to the settings.py 
configuration. Only need to do this once per additional
package

    2A. In the root folder in settings.py go to Installed_apps. Add your 
    model to the list of strings.
    I.E.
    Installed_apps = [
        ...
        'ourPackage.ourModule.ProductsConfig'
        or
        products.apps.ProductsConfig
    ]

B. Run the command to make the migrations
"python3 manage.py makemigrations"
then
"python3 manage.py migrate"

--------------------------------------------------------------------

-------------------------- Concepts/Ideas --------------------------
Difference between root folder versus other folders in the project:

In a Django project the root folder has the same name as the project
itself.
Other folders in the Django project is a Django app inside the
project. An app encapsulates a specific functionality of your project
and are orgainized around a specific feature. 

--------------------------------------------------------------------
