from django.contrib import admin
from library.models import Book, Category, Cart, CartItem

admin.site.register([Book, Category, Cart, CartItem])
