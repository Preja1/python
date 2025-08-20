Getting started in python 


Create a reoository (Git) and clone it locally

For installing project specific requirements create virtual environment 
python .m venv venv

Activite the virtual env
For window
vene/Scripts/activite

Now the setup is complete
Intall the requiremnet packages in virtual environment 
pip install Django==4.2

Create Django project
django-admin startproject core .

Run the django project
python manage.py runserver

Git Add/Commit/push commands
git add .
git commit -m "Your Commit message Here"
git push origin main

open xampp mysql start 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'python',     # your DB name
        'USER': 'root',
        'PASSWORD': '',       # fix spelling
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

python manage.py migrate
if migrate is not working then 
pip install mysqlclient

next day
venv/Scripts/activate   
python manage.py runserver
python manage.py startapp blog

add 'blog', in setting inside INSTALLED_APPS
pip install pillow

In models.py example:
class<ModelName>:
id=modelsUUUIDfield()
title=models(harfield)
subtitle=""

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
username=admin
email
password=1118

python manage.py runserver
bowser:localhost:8000/admin/

next day
python .\manage.py startapp product
add code in models.py and admin.py ma

python manage.py makemigrations if give option write:'default.jpg'
python manage.py migrate
 python .\manage.py runserver 


what we learn til now:
fuction view
generic view
url (Rev name)
Templates
model (ORM Table)

Blog CRUD

