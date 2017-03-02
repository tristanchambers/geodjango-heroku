# Basic geodjango setup for heroku

## Local setup

``` sh
$ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile hellogis
$ git init
$ git add .
$ git commit -a -m "initial checkin"
```

Add this to settings.py:

``` python
DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
```

And comment out default settings about env settings:

``` python
# Update database configuration with $DATABASE_URL.
#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)
```

Add 'DATABASE_URL=postgres:///tristan' to .env

``` sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then

```
$ heroku local:run python manage.py startapp myapp
```

Add 'django.contrib.gis' app to settings.py

Add app to project settings.py


Edit myapp/models.py. Don't forget to import gis models:

```
from django.contrib.gis.db import models
```

And finally

```
$ heroku local:run python manage.py makemigrations
$ heroku local:run python manage.py migrate

$ heroku local:run python manage.py createsuperuser

$ heroku local web
```

## Remote setup
```
heroku create
heroku buildpacks:set https://github.com/cyberdelia/heroku-geo-buildpack.git
heroku buildpacks:add heroku/python
git push heroku master

heroku local:run python manage.py migrate
heroku local:run python manage.py createsuperuser
heroku open
```

# Heroku Django Starter Template

An utterly fantastic project starter template for Django 1.10.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment. 

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Using Python 2.7?

Just update `runtime.txt` to `python-2.7.13` (no trailing spaces or newlines!).


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
