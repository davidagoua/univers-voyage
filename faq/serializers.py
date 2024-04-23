from rest_framework import serializers

from faq.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Question
        fields = '__all__'