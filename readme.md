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

#### Create urls.py in main app (folder) & add paths to views

```bash
app_name = 'main'

urlpatterns = [
    path('', views.featured_products, name='featured_products'),
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

#### Install bootstrap5

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
```

#### Add templates & styles

```bash
static / images
static / styles
```

```bash
templates / main
```
