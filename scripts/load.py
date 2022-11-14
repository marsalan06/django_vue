import csv
import os
from backend.models import CustomerCompanies, Customers, Orders, OrderItems,Deliveries

dbs = [CustomerCompanies,Customers, Orders, OrderItems,Deliveries]

def run(db_no=4 , file_name='deliveries.csv'):
    data_file = open('/home/developer/Desktop/django_vue/scripts/test_data/'+file_name)
    read_data = csv.reader(data_file)

    row = 1

    for data in read_data:
        if row == 1:
            pass
        else:
            print(data)
            print("=============")

            #Customer companies
            # dbs[db_no].objects.create(company_id = data[0],company_name = data[1])
            
            #customers
            # dbs[db_no].objects.create(id = data[0],user_id = data[1],login = data[2],password = data[3],name = data[4],
            #                           credit_cards = data[6],company_id_id = data[5])

            #Orders
            #dbs[db_no].objects.create(id=data[0],created_at = data[1],order_name=data[2],customer_id_id=data[3])

            #OrderItems
            # if data[2] == '':
            #     data[2] = 0.0
            # dbs[db_no].objects.create(id=data[0],price_per_unit=data[2],quantity = data[3],product=data[4],order_id_id=data[1])

            #deliveries
            dbs[db_no].objects.create(id=data[0],delivered_quantity=data[2],order_item_id_id=data[1])


        row = row + 1
        


            