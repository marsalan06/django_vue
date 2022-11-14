# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CustomerCompanies(models.Model):
    company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'customer_companies'


class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(unique=True, max_length=50)
    login = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    company_id = models.ForeignKey(CustomerCompanies, on_delete = models.DO_NOTHING, blank=True, null=True)
    credit_cards = models.CharField(max_length=50)

    class Meta:
        db_table = 'customers'


class Deliveries(models.Model):
    id = models.AutoField(primary_key=True)
    order_item_id = models.ForeignKey('OrderItems', on_delete = models.CASCADE, blank=True, null=True)
    delivered_quantity = models.IntegerField()

    class Meta:
        db_table = 'deliveries'


class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey('Orders', on_delete = models.CASCADE, blank=True, null=True)
    price_per_unit = models.FloatField(null =True, default=0.0)
    quantity = models.IntegerField()
    product = models.CharField(max_length=50)

    class Meta:
        db_table = 'order_items'


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order_name = models.CharField(unique=True, max_length=50)
    customer_id = models.ForeignKey(Customers, on_delete = models.CASCADE, to_field='user_id', blank=True, null=True)

    class Meta:
        db_table = 'orders'
