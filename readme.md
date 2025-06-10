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
