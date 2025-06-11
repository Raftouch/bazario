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

#### Add models to models.py

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

#### Add templates & styles
