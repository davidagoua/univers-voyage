from rest_framework import viewsets
from .serializers import ArticleSerializer, CategorieArticleSerializer, TypeArticleSerializer
from .models import Article, CategorieArticle, TypeArticle


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):

        if(self.kwargs.get('query', None) is not None):
            return Article.objects.filter(title__contains=self.kwargs['query'])

        return Article.objects.all()


class CategorieArticleViewSet(viewsets.ModelViewSet):
    serializer_class = CategorieArticleSerializer
    queryset = CategorieArticle.objects.all()



class TypeArticleViewSet(viewsets.ModelViewSet):
    serializer_class = TypeArticleSerializer
    queryset = TypeArticle.objects.all()