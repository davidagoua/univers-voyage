import functools

from amadeus import Client, ResponseError


@functools.lru_cache
def get_amadeus():
    amadeus = Client(
        client_id='8FQIhcyfuElz4A8SZ0SQLOTm4zE5mM0g',
        client_secret='8I3UEDAIH07ORkdE',
    )

    return amadeus