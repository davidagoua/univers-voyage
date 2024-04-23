from rest_framework import viewsets

from faq.models import Question
from faq.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):

        if(self.kwargs.get('query', None) is not None):
            return Question.objects.filter(question_text__contains=self.kwargs['query'])

        return Question.objects.all()
