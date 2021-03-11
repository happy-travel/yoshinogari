import requests
from API.library.support.data import edo


def get_current_version(client):
    url = edo + '/en/api/1.0/versions'
    current_version = requests.get(url, headers=client)
    return current_version
