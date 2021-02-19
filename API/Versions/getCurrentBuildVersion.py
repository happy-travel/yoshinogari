import requests
from API.library.support.getToken import get_token
from API.library.support.data import edo


def get_current_version():
    token = get_token()
    url = edo + '/en/api/1.0/versions'
    head = {'Authorization': token}
    current_version = requests.get(url, headers=head)
    return current_version


r = get_current_version()
print(r.status_code)
print(r.text)
