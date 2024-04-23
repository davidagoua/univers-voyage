import json

from amadeus import ResponseError
from django.shortcuts import render
from rest_framework.views import APIView, Response

from reservation import utils


class SearchFlightOffers(APIView):

    def post(self, request):
        amadeus = utils.get_amadeus()
        data = json.loads(request.body)
        print(data)
        try:
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=data.get('originLocationCode', 'SFO'),
                destinationLocationCode=data.get('destinationLocationCode', 'NYC'),
                departureDate=data.get('departureDate', '2024-03-29'),
                adults=data.get('adults', 1),
            )
        except ResponseError as error:
            print("error: ", error)
            return Response(error)

        return Response({
            "data": response.data,
            "count": len(response.data)
        })


class SearchAirport(APIView):

    def get(self, request):
        amadeus = utils.get_amadeus()
        response = []
        if (query := request.GET.get('query', None)) is not None:
            try:
                response = amadeus.reference_data.locations.get(keyword=query, subType='AIRPORT')
            except ResponseError as error:
                raise error
        return Response({
            "data": response.data,
        })

