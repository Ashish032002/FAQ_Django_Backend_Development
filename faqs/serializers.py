from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = [
            'id',
            'question',
            'answer',
            'created_at',
            'updated_at',
            'is_active'
        ]
        read_only_fields = ['created_at', 'updated_at']


class TranslatedFAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = [
            'id',
            'question',
            'answer',
            'created_at',
            'updated_at',
            'is_active'
        ]

    def get_question(self, obj):
        lang = self.context.get('lang', '')
        translation = obj.get_translation(lang)
        return translation['question']

    def get_answer(self, obj):
        lang = self.context.get('lang', '')
        translation = obj.get_translation(lang)
        return translation['answer']