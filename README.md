# Final project graphs
This project aims to implement an application that finds the way with the lowest rates to switch from one currency to another.

```bash
  
  # DEPENDENCE
  $ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
  
  # CONSOLE
  $ sudo su - postgres
  $ psql
  
  # DATABASE
  $ CREATE DATABASE django_cars;

  # USER
  $ CREATE USER django_cars_user WITH PASSWORD 'password';
  $ ALTER ROLE django_cars_user SET client_encoding TO 'utf8';
  $ ALTER ROLE django_cars_user SET default_transaction_isolation TO 'read committed';
  $ ALTER ROLE django_cars_user SET timezone TO 'UTC';
  $ GRANT ALL PRIVILEGES ON DATABASE django_cars TO django_cars_user;

  $ \q
  $ exit
  ```
  
  ```bash
  $ pip install django psycopg2
  ```

  Open the settings.py

  ```
  # REMOVE THIS PART
  . . .
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      }
  }
  . . .
  ```

  ```
  # ADD THIS
  . . .
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'django_cars',
          'USER': 'django_cars_user',
          'PASSWORD': 'password',
          'HOST': 'localhost',
          'PORT': '',
      }
  }

  . . .
  ```
  
  ```bash
  $ python manage.py shell < load_database.py 
  ```