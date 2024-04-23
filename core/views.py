from django.shortcuts import render
from django.views import generic

from faq.models import Category, Question


class IndexView(generic.TemplateView):

    template_name = 'front/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['questions'] = Question.objects.all()
        return context
