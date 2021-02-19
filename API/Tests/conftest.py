import pytest
from API.library.support.getToken import get_token


@pytest.fixture(scope="session")
def log_in():
    return Authorization()


class Authorization:

    def agent(self, user_name, password):
        token = get_token(user_name, password)
        authorization = {'Authorization': token}
        return authorization
