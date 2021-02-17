import requests
from API.library.support.getToken import GetToken
from API.library.support.data import edo

def GetCurrentAgentInformation():
    token = GetToken()
    url = edo + '/en/api/1.0/agent'
    head = {'Authorization': token}
    currentAgentInformation = requests.get(url, headers=head)
    return currentAgentInformation

r = GetCurrentAgentInformation()
print(r.status_code)
print(r.text)