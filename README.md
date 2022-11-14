# django_vue
Django Vue Integration


Steps to get the project running
a) create venv for python 3.7+
b) pip install -r requirements.txt
d) edit the settings.py file for database connection as per your user
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME' : '<your_database_name>',
        'USER': <your_own_user>,
        'PASSWORD':<your_user's_password>,
        'HOST':'localhost'
    }
c) python manage.py runserver, will give you migrate warning
d) python manage.py migrate

To upload data to database the scripts folder load.py file,

a) place the csv files in ~/scripts/test_data folder
b) In terminal use the command python manage.py runscript load
c) It will ask the input to select the data table as 

    Select Data Table to load data: 
    0) CustomerCompanies, 1) Customers, 2) Orders, 3) OrderItems, 4) Deliveries

d) Then it will ask for file name, enter file name with extension i.e csv

    Enter file name in test_data folder: 
    File Name: customer_companies.csv

e) If file is uploaded code will exit or any exception will be printed.


