from django.contrib import admin
from .models import Category, Question



@admin.register(Category)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'answer_text' ,'category')
