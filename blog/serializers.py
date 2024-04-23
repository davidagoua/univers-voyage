from rest_framework import serializers
from .models import Article, CategorieArticle, TypeArticle



class CategorieArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieArticle
        fields = '__all__'


class TypeArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeArticle
        fields = '__all__'



class ArticleSerializer(serializers.ModelSerializer):
    category = CategorieArticleSerializer()
    type = TypeArticleSerializer()
    class Meta:
        model = Article
        fields = '__all__'