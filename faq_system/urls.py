# faq_system/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from faqs.views import FAQViewSet
from faqs.views import test_redis

router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename='faq')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='api/', permanent=False)),
    path('test-redis/', test_redis, name='test-redis'),# Add this line
]