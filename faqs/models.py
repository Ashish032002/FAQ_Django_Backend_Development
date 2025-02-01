from django.db import models
from django.core.cache import cache
from ckeditor.fields import RichTextField
from googletrans import Translator


class FAQ(models.Model):
    question = models.TextField(
        help_text="Enter the question in English"
    )
    answer = RichTextField(
        help_text="Enter the answer in English"
    )
    question_hi = models.TextField(
        blank=True,
        verbose_name="Question (Hindi)"
    )
    answer_hi = RichTextField(
        blank=True,
        verbose_name="Answer (Hindi)"
    )
    question_bn = models.TextField(
        blank=True,
        verbose_name="Question (Bengali)"
    )
    answer_bn = RichTextField(
        blank=True,
        verbose_name="Answer (Bengali)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['-created_at']

    def __str__(self):
        return self.question[:50]

    def _translate_text(self, text, lang):
        """Helper method to translate text"""
        translator = Translator()
        try:
            translation = translator.translate(text, dest=lang)
            return translation.text
        except Exception as e:
            print(f"Translation error: {e}")
            return text

    def save(self, *args, **kwargs):
        """Override save to handle translations"""
        is_new = self.pk is None

        # Clear cache if updating
        if not is_new:
            cache.delete(f'faq_{self.pk}_hi')
            cache.delete(f'faq_{self.pk}_bn')

        # Handle translations for new objects or empty translations
        if is_new or not self.question_hi:
            self.question_hi = self._translate_text(self.question, 'hi')
        if is_new or not self.answer_hi:
            self.answer_hi = self._translate_text(self.answer, 'hi')
        if is_new or not self.question_bn:
            self.question_bn = self._translate_text(self.question, 'bn')
        if is_new or not self.answer_bn:
            self.answer_bn = self._translate_text(self.answer, 'bn')

        super().save(*args, **kwargs)

    def get_translation(self, lang):
        """Get translated content for specified language"""
        if lang not in ['hi', 'bn']:
            return {
                'question': self.question,
                'answer': self.answer
            }

        # Check cache first
        cache_key = f'faq_{self.pk}_{lang}'
        cached = cache.get(cache_key)
        if cached:
            return cached

        # Get translations based on language
        translations = {
            'hi': (self.question_hi, self.answer_hi),
            'bn': (self.question_bn, self.answer_bn)
        }

        question, answer = translations[lang]

        # If translation is empty, fall back to English
        if not question:
            question = self.question
        if not answer:
            answer = self.answer

        result = {
            'question': question,
            'answer': answer
        }

        # Cache the result
        cache.set(cache_key, result, timeout=86400)  # 24 hours
        return result
