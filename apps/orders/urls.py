from django.urls import path
from apps.orders.views import create_order

urlpatterns = [
    path('create-orders/', create_order, name='create_order'),
]