import csv
import os
from backend.models import CustomerCompanies, Customers, Orders, OrderItems,Deliveries

dbs = [CustomerCompanies,Customers, Orders, OrderItems,Deliveries]

def run(db_no=4 , file_name='deliveries.csv'):

    row = 1
    print("Select Data Table to load data: ")
    print("0) CustomerCompanies, 1) Customers, 2) Orders, 3) OrderItems, 4) Deliveries")
    db_no = int(input("Enter DB Number: "))
    if db_no > 4 or db_no < 0:
        print("Wrong DB selected")
        pass
    else:
        print(db_no)
        print("Enter file name in test_data folder: ")
        file_name = str(input("File Name: "))
        print(file_name)
    
    try:
        data_file = open('/home/developer/Desktop/django_vue/scripts/test_data/'+file_name)
        read_data = csv.reader(data_file)
        for data in read_data:
            if row == 1:
                pass

            else:

                #Customer companies
                if db_no == 0:
                    dbs[db_no].objects.create(company_id = data[0],company_name = data[1])
                
                #customers
                elif db_no == 1:
                    dbs[db_no].objects.create(id = data[0],user_id = data[1],login = data[2],password = data[3],name = data[4],
                                        credit_cards = data[6],company_id_id = data[5])

                #Orders
                elif db_no == 2:
                    dbs[db_no].objects.create(id=data[0],created_at = data[1],order_name=data[2],customer_id_id=data[3])

                #OrderItems
                elif db_no == 3:
                    if data[2] == '':
                        data[2] = 0.0
                    dbs[db_no].objects.create(id=data[0],price_per_unit=data[2],quantity = data[3],product=data[4],order_id_id=data[1])

                #deliveries
                elif db_no == 4:
                    dbs[db_no].objects.create(id=data[0],delivered_quantity=data[2],order_item_id_id=data[1])
            
            row = row + 1
    except Exception as e:
        print(e)
        


            