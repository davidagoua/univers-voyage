from django.contrib import admin

from .models import Album, CategorieArticle, Article, TypeArticle, Capture


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(CategorieArticle)
class CategorieArticleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category','author','type','actif')


@admin.register(TypeArticle)
class TypeArticleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Capture)
class CaptureAdmin(admin.ModelAdmin):
    list_display = ('image','album')