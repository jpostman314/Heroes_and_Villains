# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4ll5#ya7ee%*a2wm4zhz^)vo04c)99e)a00^b+t3d(^97uq%=%'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'supers_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Iamgroot314'
    }
}

