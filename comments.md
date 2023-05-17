# App Desription

Purposue of this app is to allow access to modules of SAM project/robot and display some selected data. Idea is to have it done as web app.


### To run application locally:
- go to folder `sam-01-django` where is located file `manage.py`
- run venv by typing in terminal `source venv/bin/activate`
- type in terminal `python3 manage.py runserver`


# Version

Name | Version
---- | -------
python | 3.10
Django | 4.2.1


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
                views.py
        db.sqlite3
        manage.py
    venv/
    comments.md


# Process of development and istallation envioremnt and packages

## 1. establish venv

    sudo apt install python3.10-venv
    
    python3 -m venv venv

To run/open venv type:

    source venv/bin/activate

## 2. Installation of Django

    pip install django

In this app it's used Django version 4.2.1

## 3. Creating django project

    django-admin startproject sam

To check if it work, go to created folder `sam`, by command `cd sam`. Then run server.
    
    python3 manage.py runserver

Go to http://127.0.0.1:8000/ and check if Django startup page pop up.

## 4. Start `sam_app`

To create app itself inside folder `sam`:

    python3 manage.py startapp sam_app

