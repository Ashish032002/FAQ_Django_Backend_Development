import os
import django
from django.core.cache import cache

# Manually set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'faq_system.settings')

# Initialize Django
django.setup()

# Test Redis connection
cache.set('test_key', 'Redis is connected!', timeout=30)
value = cache.get('test_key')
print(value)  # Expected output: "Redis is connected!"

