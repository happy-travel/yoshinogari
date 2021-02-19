import requests
from API.library.support.data import tr


def get_token(user_name, password):
    body = {
        'userName': user_name,
        'password': password
    }
    url = tr
    token = requests.post(
        url,
        json=body
    )
    return 'Bearer ' + token.text
