# django-inventory-management
A basic Inventory management project in Django

Steps to Run
------------
Setup and activate a Virtualenv

~~~
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
~~~

In case of some OperationalError try the following
~~~
Delete the db.sqlite3 file 
python manage.py createsuperuser
Repeat from makemigrations
