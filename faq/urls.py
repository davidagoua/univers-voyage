from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views, viewsets

router = DefaultRouter()

router.register('questions', viewsets.QuestionViewSet)


urlpatterns = [
    path('', views.QuetionListView.as_view(), name='index'),

    path('api/', include(router.urls))
]