# faqs/tests/test_models.py
import pytest
from django.core.cache import cache
from faqs.models import FAQ

@pytest.mark.django_db
class TestFAQModel:
    def test_faq_creation(self):
        faq = FAQ.objects.create(
            question="Test Question?",
            answer="Test Answer"
        )
        assert faq.question == "Test Question?"
        assert faq.answer == "Test Answer"
        assert faq.is_active == True

    def test_translation_generation(self):
        faq = FAQ.objects.create(
            question="Hello",
            answer="World"
        )
        assert faq.question_hi != ""
        assert faq.question_bn != ""

    def test_get_translation(self):
        faq = FAQ.objects.create(
            question="Hello",
            answer="World"
        )
        translation = faq.get_translation('hi')
        assert 'question' in translation
        assert 'answer' in translation