import os

from celery import Celery

# Set Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_predictor.settings')

# Initialize Celery
app = Celery('crypto_predictor')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks across installed Django apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

