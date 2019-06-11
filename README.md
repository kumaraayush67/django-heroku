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
  
  
  ## Deployment on heroku
   - Install heroku on System
   
   - Install heroku-django
   
    pip install heroku-django
   
   - import heroku-django in settings.py file
   
   - at bottom of settings file add 
   
    django_heroku.settings(locals())
   
   - Now install gunicorn
   
    pip install gunicorn
    
   - Now add all the dependences to requirements.txt file by
    
    pip freeze > requirements.txt
    
   - In the root directory create *Procfile*. Make sure spelling is same, there should be no change in cases and file should not have any extention.
   
   - After creating the file write the following:
   
    web: gunicorn project_name.wsgi

   - Create Heroku Application
   
    heroku create *app_name*
    
   - Add heroku path to git remote. can confirm it using git remote -v
   
   - To Push all the files run
   
    git push heroku master
    
    
