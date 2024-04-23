from django.shortcuts import render
from rest_framework.views import APIView, Response

import utils


class BookingView(APIView):
    def get(self, request):
        return render(request, 'booking/index.html')

    def post(self, request):
        originLocationCode = request.POST.get('originLocationCode', None)
        destinationLocationCode = request.POST.get('destinationLocationCode', None)
        departureDate = request.POST.get('departureDate', None)

        amadeus = utils.get_amadeus()
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=originLocationCode,
            destinationLocationCode=destinationLocationCode,
            departureDate=departureDate,
            adults=1
        )
        return Response({
            "data": response.data
        })
