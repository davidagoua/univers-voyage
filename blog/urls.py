from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ArticleViewSet, CategorieArticleViewSet, TypeArticleViewSet


router = DefaultRouter()


router.register('articles', ArticleViewSet, basename="articles")
router.register('categories', CategorieArticleViewSet, basename="categories_articles")
router.register('types', TypeArticleViewSet, basename="types_articles")


urlpatterns = [
    path('api/', include(router.urls))
]