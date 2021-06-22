from django.urls import path, include
from .views import LatestProductList

urlpatterns = [
    path('latest-products/', LatestProductList.as_view()),
]