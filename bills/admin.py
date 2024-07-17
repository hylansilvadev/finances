from django.contrib import admin

from .models import Bills, Categories

# Register your models here.

admin.site.register(Bills)
admin.site.register(Categories)