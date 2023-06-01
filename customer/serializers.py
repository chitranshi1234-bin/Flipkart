from rest_framework import serializers
from customer.models import *

class GetCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = "__all__"

class GetCustomerAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAddress
        fields = "__all__"


class CustomerDetailsAddressSerializer(serializers.ModelSerializer):
    customer_address = GetCustomerAddressSerializer(many=True)
    
    class Meta:
        model = Customers
        fields = ('first_name','last_name','mobile','age','city','pin_code','dob')
        