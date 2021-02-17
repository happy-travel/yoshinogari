import requests
from API.library.support.getToken import GetToken
from API.library.support.data import identity

def GetUserInfo():
    token = GetToken()
    url = identity + '/connect/userinfo'
    head = {'Authorization': token}
    userInfo = requests.get(url, headers=head)
    return userInfo

r = GetUserInfo()
print(r.status_code)
print(r.text)