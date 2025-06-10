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
