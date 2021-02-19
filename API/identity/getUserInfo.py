import requests
from API.library.support.data import identity


def get_user_info(client):
    url = identity + '/connect/userinfo'
    user_info = requests.get(url, headers=client)

    return user_info
