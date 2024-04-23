from functools import lru_cache
from amadeus import Client, ResponseError
from django.conf import settings



@lru_cache
def get_amadeus():
    amadeus = Client(
        client_id=settings.AMADEUS_API_KEY,
        client_secret=settings.AMADEUS_API_SECRET,
    )

    return amadeus