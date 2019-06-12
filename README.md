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
  
 ## Media files
 
  - When dealing with media files copy and paste following code at the bottom of your settings.py
   
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    
    MEDIA_URL = '/media/'
    
   - To make media files available to access on a local system. Add following at the bottom of the urls.py
   
    if settings.DEBUG:
   
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     
   - Also add import statements in urls.py file
   
    from django.conf import settings
    from django.conf.urls.static import static
    
  
  ## Deployment on heroku
   - Install heroku on System
   
     https://devcenter.heroku.com/articles/heroku-cli
   
   - Install django-heroku
   
    pip install django-heroku
   
   - import django_heroku in settings.py file
   
   - at bottom of settings.py file add 
   
    django_heroku.settings(locals())
   
   - Now install gunicorn
   
    pip install gunicorn
    
   - Now add all the dependences to requirements.txt file by
    
    pip freeze > requirements.txt
    
   - In the root directory create *Procfile*. Make sure spelling is same, there should be no change in cases and file should not have any extention.
   
   - After creating the file write the following:
   
    web: gunicorn project_name.wsgi
    
   - Login to Heroku. On terminal write
   
    heroku login

   - Create Heroku Application
   
    heroku create *app_name*
    
   - Add heroku path to git remote.
   
    heroku git:remote -a *app_name*
   
   - can confirm it using git remote -v
   
   - To Push all the files run
   
    git push heroku master
    
    
