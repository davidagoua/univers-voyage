from django.shortcuts import render
from django.views import generic

from faq.models import Question, Category


class QuetionListView(generic.ListView):
    template_name = 'faq/question_list.html'
    context_object_name = 'questions'
    queryset = Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
