# example

## To create a virtual env
 - pip install virtualenv
 - virtualenv enviroment_Name
 
 ## Start Virtual Env
 for Linux
 - source enviroment_name/bin/activate
 
 for windows
 - enviroment_name\Scripts\activate
 
 ## Install Django to virtual env
  - pip install django
  
 ## Start Django Project
  - django-admin startproject project_name
  - cd project_name
  - python manage.py runserver
  
  To stop server
  - Ctrl + C
  
  To migrate
  - python manage.py migrate
  
 ## Start App
  - python manage.py startapp app_name
  - Add app in settings.py file under INSTALLED_APPS
