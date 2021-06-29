from .models import Order, OrderItem
from django.contrib import admin

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)