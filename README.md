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
~~~
## Functionalities implimented.
### 1. Login Page for user.

![alt text](https://github.com/vardhanshah138/django-inventory-management/blob/ecommerce/login.png?raw=true)

### 2. Adding New Products From Supplier that can be ordered.

![alt text](https://github.com/vardhanshah138/django-inventory-management/blob/ecommerce/addnewproduct.png?raw=true)

### 3. Display List of Products where product can be ordered for stocking up our Inventory.

![alt text](https://github.com/vardhanshah138/django-inventory-management/blob/ecommerce/productfromsupplier.png?raw=true)

### 4. To Change in any form field.

![alt text](https://github.com/vardhanshah138/django-inventory-management/blob/ecommerce/formfieldupdation.png?raw=true)

### 5. Adding Products to our inventory.

![alt text](https://github.com/vardhanshah138/django-inventory-management/blob/ecommerce/addproductsin_inventory.png?raw=true)

