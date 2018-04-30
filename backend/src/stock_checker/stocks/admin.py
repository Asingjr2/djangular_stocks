from django.contrib import admin
from .models import Stock, Favorites

# Register your models here.
admin.site.register(Stock)
admin.site.register(Favorites)