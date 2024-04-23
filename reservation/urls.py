from django.urls import path

from reservation import views

urlpatterns = [
    path('search-offers/', views.SearchFlightOffers.as_view(), name='search'),
    path('search-airports/', views.SearchAirport.as_view(), name='search'),
]