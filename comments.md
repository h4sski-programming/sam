# App Desription

Purposue of this app is to allow access to modules of SAM project/robot and display some selected data. Idea is to have it done as web app.


### To run application locally:
- go to folder `sam-01-django` where is located file `manage.py`
- run venv by typing in terminal `source venv/bin/activate`
- type in terminal `python3 manage.py runserver`


------------------------------
# Version

Name | Version
---- | -------
python | 3.10
Django | 4.2.1


------------------------------
# App layout

    sam-01-django/
        sam/
            sam/
                __pycache__/
                __init__.py
                asgi.py
                settings.py
                urls.py
                wsgi.py
            sam_app/
                migrations/
                __init__.py
                admin.py
                apps.py
                models.py
                tests.py
                urls.py
                views.py
        db.sqlite3
        manage.py
    venv/
    comments.md


------------------------------
# Database

### DB management / migrations

Following https://docs.djangoproject.com/en/4.2/intro/tutorial02/
- create class in `models.py`
- add setting into `settings.py` by adding value into list `INSTALLED_APPS`
    - check class name in `sam_app/apps.py` => `SamAppConfig`
    - add dotted path as string => `'sam_app.apps.SamAppConfig'`
- run command `python manage.py makemigrations sam_app`
- run command `python manage.py migrate`

Now all tables were created in DB. Can be accessed via `/admin/` subpage when server is running.

### Create superuser

    python manage.py createsuperuser

username:   h4sski
email:      h4sski.programming@gmail.com
password:   h4sski

Now run server and go to `/admin` subpage and login. `python manage.py runserver`


## Models

```python
class Module(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField()
```


------------------------------
# Testing

To start tests type:

    python3 ./manage.py test

You must be in folder where `manage.py` file is located.


------------------------------
# Links

### During develepment below links were used

- https://docs.djangoproject.com/en/4.2/
- https://getbootstrap.com/docs/4.0/
- https://www.jetbrains.com/help/pycharm/completion-and-navigation-for-named-url-tags-in-django-templates.html - url used in django templates


------------------------------
# Process of development and istallation envioremnt and packages

1. establish venv

    sudo apt install python3.10-venv
    
    python3 -m venv venv

To run/open venv type:

    source venv/bin/activate

2. Installation of Django

    pip install django

In this app it's used Django version 4.2.1

3. Creating django project

    django-admin startproject sam

To check if it work, go to created folder `sam`, by command `cd sam`. Then run server.
    
    python3 manage.py runserver

Go to http://127.0.0.1:8000/ and check if Django startup page pop up.

4. Start `sam_app`

To create app itself inside folder `sam`:

    python3 manage.py startapp sam_app

5. Done, application has beed created