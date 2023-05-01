
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Tells django that any url that start with
    # products/ send them to the url module in the
    # products app
    path('products/', include('products.urls')),
]
