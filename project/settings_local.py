DEBUG = True

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'day1_1',
       'USER': 'postgres',
       'PASSWORD': 'test',
       'HOST': 'localhost',
       'PORT': '5432',
   },
}