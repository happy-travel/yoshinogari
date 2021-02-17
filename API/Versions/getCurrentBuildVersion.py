import requests
from API.library.support.getToken import GetToken
from API.library.support.data import edo

def GetCurrentBuidVersion():
    token = GetToken()
    url = edo + '/en/api/1.0/versions'
    head = {'Authorization': token}
    buidVersion = requests.get(url, headers=head)
    return buidVersion

r = GetCurrentBuidVersion()
print(r.status_code)
print(r.text)