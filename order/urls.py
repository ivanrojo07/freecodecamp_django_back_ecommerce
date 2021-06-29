from django.urls import path
from order import views

urlpatterns=[
    path('checkout/',views.checkout, name='checkout'),
    path('myOrders/',views.OrderList.as_view())
]