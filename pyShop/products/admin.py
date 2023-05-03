from django.contrib import admin
from .models import Product
from .models import Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')

# Tells Django that we want to manage our
# Product in the admin area
# Takes Two args: first arg is the module
# you want to manage and 2nd arg is the
# list order you want it to be displayed
admin.site.register(Product, ProductAdmin)

admin.site.register(Offer, OfferAdmin)

