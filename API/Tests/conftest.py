import pytest
from API.library.support.getToken import get_token
from API.library.support.data import agents


@pytest.fixture(scope="session")
def log_in():
    return Authorization()


class Authorization:

    def user(self, agent_status):
        agent = agents.get(agent_status)
        token = get_token(agent['user_name'], agent['password'])
        authorization = {'Authorization': token}
        return authorization
