# Database PostgreSQL

* https://docs.djangoproject.com/en/1.9/ref/settings/#databases

```
$ sudo su - postgres
$ psql
psql (9.3.12)
Type "help" for help.

postgres=# CREATE DATABASE dbname;
CREATE DATABASE
postgres=# CREATE USER dbuser WITH PASSWORD '1';
postgres=# GRANT ALL PRIVILEGES ON DATABASE dbname TO dbuser;
GRANT
postgres=#
```

* **`settings.py`**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbname',
        'USER': 'dbuser',
        'PASSWORD': 'dbpasword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
