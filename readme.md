#### Create virtual environment

```bash
python -m venv venv
```

#### Activate virtual environment

```bash
venv\Scripts\activate
```

#### Install Django

```bash
pip install django
```

#### Start project

```bash
django-admin startproject bazario
```

#### Access project

```bash
cd bazario
```

#### Start app main

```bash
python manage.py startapp main
```

#### Include main module in the INSTALLED_APPS list in settings.py

```bash
'main'
```

#### Add models to models.py

```bash
class Category(models.Model):
...

class Product(models.Model):
...
```

#### Create added models

```bash
python manage.py makemigrations
```

#### Migrate models to database

```bash
python manage.py migrate
```

#### Add destination for images in settings.py

```bash
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

#### Install module for images

```bash
python -m pip install Pillow
```

#### Register models in admin.py

```bash
@admin.register(Category)
@admin.register(Product)
```

#### Run server to check all is correct

```bash
python manage.py runserver
```

#### Create superuser

```bash
python manage.py createsuperuser
```

#### Include new url pattern

```bash
path('', include('main.urls', namespace='main')),
```

#### Add views

```bash
def home(request):
def product_details(request, slug):
```

#### Create urls.py in main app (folder) & add paths to views

```bash
app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.product_details, name='product_details')
]
```

#### Add path to static files in settings.py

```bash
STATICFILES_DIRS = [BASE_DIR / 'main' / 'static']
```

#### Add url patterns in urls

```bash
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

<!-- #### Install bootstrap5

```bash
pip install django-bootstrap-v5
```

#### Include bootstrap5 module in the INSTALLED_APPS list in settings.py

```bash
'bootstrap5'
```

#### Insert bootstrap into <head> in base.html

```bash
{% load bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}
``` -->

#### Add templates & styles

```bash
static / images
static / styles
```

```bash
templates / main
```

#### Add new view

```bash
def product_list(request, category_slug=None):
```

#### Update urlpatterns in urls.py for new views

```bash
path()
```

### CONFIGURE TAILWINDCSS FOR DJANGO

#### Install Tailwind for Django

```bash
python -m pip install django-tailwind
```

#### Add 'tailwind' to INSTALLED_APPS list in settings.py

```bash
'tailwind'
```

#### Initialize Tailwind

```bash
python manage.py tailwind init
```

#### app_name (theme):

Leave as is or add another app name
That creates a new folder 'theme'

#### Add 'theme' to INSTALLED_APPS list in settings.py

```bash
'theme'
```

#### Add tailwind app name in settings.py :

```bash
TAILWIND_APP_NAME = 'theme'
```

#### Check if node is installed and where

```bash
where npm
```

#### Copy the path and paste it to settings.py

For example

```bash
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
```

#### Launch Tailwind

```bash
python manage.py tailwind install
```

There will be a folder 'templates' with base.html created inside 'theme' folder
You can either 1. keep it and extend or 2. create your own templates in created apps

#### Insert tailwind into your own base.html

On top of the file

```bash
{% load static tailwind_tags %}
```

Into <head> tag:

```bash
{% tailwind_css %}
```

#### Configure hot reload

```bash
pip install django_browser_reload
```

#### Add it to INSTALLED_APPS list and also to MIDDLEWARE in settings.py

```bash
'django_browser_reload'
```

```bash
'django_browser_reload.middleware.BrowserReloadMiddleware'
```

#### Add path to reload to urlpatterns in root urls file

```bash
path('__reload__', include('django_browser_reload.urls'))
```

#### Add internal urls to settings.py

```bash
INTERNAL_IPS = [
    "127.0.0.1"
]
```

#### Run two commands simultaneously

```bash
python manage.py tailwind start
```

```bash
python manage.py runserver
```

### Add pagination to products list

#### Start app cart

```bash
python manage.py startapp cart
```

#### Include main module in the INSTALLED_APPS list in settings.py

```bash
'cart'
```
