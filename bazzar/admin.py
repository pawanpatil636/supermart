from django.contrib import admin
from .models import Product
from .models import Address
from .models import Order 
from .models import Payment

admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Payment)

# Register your models here.
