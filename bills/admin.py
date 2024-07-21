from django.contrib import admin

from .models import Bills, Categories, CreditCardBill

# Register your models here.

admin.site.register(Bills)
admin.site.register(Categories)
admin.site.register(CreditCardBill)