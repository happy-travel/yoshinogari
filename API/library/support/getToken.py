import requests
from API.library.support.data import reciever

def GetToken():
    body = {
        'userName': '',
        'password': ''
    }

    url = reciever

    token = requests.post(
        url,
        json = body
    )

    return 'Bearer ' + token.text