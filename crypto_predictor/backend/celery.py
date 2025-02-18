import os
from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_predictor.settings')

app = Celery('crypto_predictor')

# Load config from Django settings, using CELERY_ as prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from installed Django apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
