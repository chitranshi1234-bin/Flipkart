from django.contrib import admin
from django.urls import path,include
from customer.views import *

urlpatterns = [
    path('get-customers',GetCustomerView.as_view()),
    path('get-customeraddress',GetCustomerAddress.as_view())


   
]
