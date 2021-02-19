import requests
from API.library.support.data import edo


def get_current_agent_information(client):
    url = edo + '/en/api/1.0/agent'
    current_agent_information = requests.get(url, headers=client)

    return current_agent_information
