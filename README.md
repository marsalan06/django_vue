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
change the lines as 
  def run(db_no=<no_of_table> , file_name=<name_of_csv_file>):
the list of database_no  start from 0-4 corresponding to dbs = [CustomerCompanies,Customers, Orders, OrderItems,Deliveries]
and in the run function uncomment the line required
