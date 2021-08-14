# django-inventory-management
Developed an Inventory management website using Django Framework having MySQL Database. Where Admin can easily manage inventory stocks and update regular products.
## Skills Used
Django,SQL,HTML,CSS,JS,Bootstrap.

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
