from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()



class TypeArticle(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class CategorieArticle(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class ActifArticle(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(actif=True)


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(CategorieArticle, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeArticle, on_delete=models.SET_NULL, null=True)
    actif = models.BooleanField(default=True)

    # managers
    objects = models.Manager()
    actif_objects = ActifArticle()

    def __str__(self):
        return self.title


class Album(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField

    def __str__(self):
        return self.name


class Capture(models.Model):
    image = models.ImageField(upload_to='galerie/')
    caption = models.CharField(null=True, blank=True, max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
