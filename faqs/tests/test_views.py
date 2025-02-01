# faqs/tests/test_views.py
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from faqs.models import FAQ

@pytest.mark.django_db
class TestFAQAPI:
    def setup_method(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="Test Question?",
            answer="Test Answer"
        )

    def test_list_faqs(self):
        url = reverse('faq-list')
        response = self.client.get(url)
        assert response.status_code == 200
        assert len(response.data['results']) > 0

    def test_list_faqs_with_language(self):
        url = reverse('faq-list')
        response = self.client.get(f"{url}?lang=hi")
        assert response.status_code == 200
        assert len(response.data['results']) > 0