Installation
============

This template will set up a Django project with frontend libraries (Foundation, jQuery) and a ready-to-use frontend toolchain based on Gulp.

* Create a new virtual environment for the new project:
    ```
    mkvirtualenv --python=/usr/bin/python3 <virtualenv_name>
    ```

* Install Django:
    ```
    (env)$ pip install Django
    ```
    
* Create a new project using this template:
    ```
    (env)$ django-admin startproject --template https://github.com/CDE-UNIBE/cde-django-template/archive/master.zip --extension py,md,ini,json <project_name>
    ```

* Go to project directory:
    ```
    (env)$ cd <project_name>
    ```
    
* Add `apps` directory to virtual environment:
    ```
    (env)$ add2virtualenv apps
    ```

* Create necessary env variables
    ```
    (env)$ make
    ```


Backend
=======

* Install requirements:
    ```
    (env)$ pip install -r requirements/development.txt
    ```
    You may want to freeze the requirements: `(env)$ pip freeze`

* Update the environment variables in `envs` directory, namely:
    * `DATABASE_URL`
    * `DJANGO_CONFIGURATION` (DevConfig [default] or ProdConfig)

* Apply database migrations:
    ```
    (env)$ python manage.py migrate
    ```
    
    
Frontend
========

* Install frontend requirements:
    ```
    (env)$ npm install
    ```
    Possibly freeze the requirements?
    
* Eventually customize gulp file (e.g. remove jQuery/jQueryUI)

* Build frontend files:
    ```
    (env)$ gulp
    ```

* Run server:
    ```
    (env)$ python manage.py runserver
    ```

* Visit `localhost:8000` in your browser.


Project structure
=================

    ├── apps                                        <- Create your Django apps in the apps folder
    │   ├── __init__.py
    │   └── [project_name]
    │       ├── config
    │       │   ├── __init__.py
    │       │   ├── common.py                       <- Common Django settings
    │       │   └── mixins.py                       <- Settings mixins
    │       ├── __init__.py
    │       ├── settings.py
    │       ├── templates
    │       │   ├── base.html                       <- The (initial) base template
    │       │   └── partials                        <- Helper template snippets
    │       │       ├── messages.html
    │       │       └── pagination.html
    │       ├── templatetags
    │       │   ├── __init__.py
    │       │   ├── helpers.py                      <- Helper template tags
    │       │   └── svg.py                          <- Template tags to use SVG icons
    │       ├── urls.py                             <- The base URLs
    │       └── wsgi.py
    ├── envs                                        <- Environment variables
    │   ├── DATABASE_URL
    │   ├── DJANGO_ALLOWED_HOSTS
    │   ├── DJANGO_CONFIGURATION
    │   ├── DJANGO_DEBUG
    │   ├── DJANGO_SECRET_KEY
    │   └── DJANGO_SETTINGS_MODULE
    ├── fabfile.py                                  <- Used for deployment
    ├── frontend
    │   ├── icons                                   <- Place your SVG icons in this folder
    │   ├── js
    │   │   └── main.js                             <- (empty) file for JS scripts
    │   ├── libraries
    │   │   └── svg4everybody
    │   │       └── svg4everybody.min.js
    │   └── scss
    │       ├── app.scss                            <- Add modules or activate Foundation components
    │       ├── layout
    │       │   └── _content.scss
    │       ├── module
    │       │   ├── _button.scss
    │       │   └── _icon.scss
    │       └── _settings.scss                      <- Basic settings for Foundation and your site
    ├── requirements
    │   ├── base.txt
    │   ├── development.txt
    │   └── production.txt
    ├── gulpfile.js                                 <- Frontend toolchain
    ├── manage.py
    ├── package.json
    ├── pytest.ini
    └── README.md


Icons
=====

How to add new icons (using https://icomoon.io/app/ as an example):
* Select icon(s)
* Click "Generate SVG & More" (bottom left)
* Click \<code> next to the icon and copy the symbol definition
* Create a new svg file in frontend/icons/ (the filename will be used as id of 
    the icon) and paste the symbol definition
* Modify the symbol definition as follows:
    * Create a new \<svg> tag around the entire definition
    * Copy the viewBox attribute of \<symbol> to the \<svg> tag
    * Delete the \<symbol> attribute

Before:
```html
<symbol id="icon-plus" viewBox="0 0 16 16">
<title>plus</title>
<path d="..."></path>
</symbol>
```

After:
```html
<svg viewBox="0 0 16 16">
<title>plus</title>
<path d="..."></path>
</svg>
```

* Let gulp to the thing (gulp svgstore), this creates a sprite of all svg icons 
in frontend/static/svg/icons.svg
* Use the icon as follows: ```<svg class="icon is-inline"><use xlink:href="static/svg/icons.svg#list"></use></svg>```
* Or use the templatetag svg.svg_icon (see documentation of template tag for 
    further information):
    
```djangotemplate
{% comment %}  <- Do not include this in your template
{% load svg %}
{% svg_icon 'plus' %}
{% endcomment %} <- Do not include this in your template.
```


Run tests
=========

```
envdir envs/ pytest
```


TODO
====

* Add shippable.yml
* Add functional test basics
