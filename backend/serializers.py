from rest_framework import serializers
from .models import Customers, OrderItems, Orders , CustomerCompanies, Deliveries



class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class CustomerCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCompanies
        fields = '__all__'

class DeliveriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliveries
        fields = '__all__'