from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer, TranslatedFAQSerializer
from django.http import JsonResponse
from django.core.cache import cache

def test_redis(request):
    # Try to set a value in cache
    cache.set('test_key', 'Redis is working!', timeout=30)
    # Try to get the value back
    value = cache.get('test_key')
    return JsonResponse({'cache_test': value})


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.filter(is_active=True)

    def get_serializer_class(self):
        lang = self.request.query_params.get('lang', '')
        if lang in ['hi', 'bn']:
            return TranslatedFAQSerializer
        return FAQSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', '')
        return context

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', '')
        cache_key = f'faq_list_{lang}'

        # Try to get from cache
        cached_response = cache.get(cache_key)
        if cached_response:
            return Response(cached_response)

        # If not in cache, generate response
        response = super().list(request, *args, **kwargs)

        # Cache the response
        cache.set(cache_key, response.data, timeout=3600)  # 1 hour

        return response


