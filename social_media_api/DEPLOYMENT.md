# DEPLOYMENT.md

## Project: Social Media API
**Framework:** Django REST Framework  
**Hosting Platform:** Render  

---

### 1. Overview
This document outlines the steps to deploy the Django Social Media API project to Render, including configuration and testing after deployment.

---

### 2. Environment Setup

#### Requirements
- Python 3.10+
- pip
- Gunicorn
- dj-database-url
- python-decouple
- whitenoise

# Install dependencies:
```bash
pip install -r requirements.txt


# Environment Variables

Create a .env file in the project root and add the following variables:

SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://<your_internal_render_db_url>
ALLOWED_HOSTS=your-render-app-name.onrender.com,localhost,127.0.0.1

# Django Settings for Production

In settings.py:

from decouple import config
import dj_database_url
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='fallback-secret-key')
DEBUG = config('DEBUG', cast=bool, default=False)  

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'social_media_db_m2g7',
        'USER': 'social_media_db_m2g7_user',
        'PASSWORD': 'o1kzn2RHsreXe0sDFvT8kNPipXovYsUJ',
        'HOST': 'dpg-d3lqt2mmcj7s73a5u2ag-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Render Deployment

Push your code to GitHub:

git add .
git commit -m "Prepare for Render deployment"
git push origin main


Go to https://render.com
 → New Web Service

Connect your GitHub repository.

Set up the service:

Build Command:

pip install -r requirements.txt && python manage.py collectstatic --noinput


Start Command:

gunicorn social_media_api.wsgi:application


Add the environment variables from your .env file.

# Database Migration

After deployment, open the Render shell and run:

python manage.py migrate

#  Test Your App

Visit:

https://your-render-app-name.onrender.com/admin/
https://your-render-app-name.onrender.com/api/accounts/
https://your-render-app-name.onrender.com/api/posts/

# Deployment Complete

Your Django REST API is now live on Render 🎉
Example:

https://your-render-app-name.onrender.com