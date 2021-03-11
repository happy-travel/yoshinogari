import json
import pytest
from API.Agents.getCurrentAgentInformation import get_current_agent_information
from API.identity.getUserInfo import get_user_info
from API.library.support.data import agents
from API.Versions.getCurrentBuildVersion import get_current_version


class TestAccompaingMethods:

    @pytest.mark.parametrize("test_input, expectations", [('active', 200), ('inactive', 400)])
    def test_current_agent_information_request(self, log_in, test_input, expectations):
        agent = log_in.user(test_input)
        response = get_current_agent_information(agent)
        body = json.loads(response.text)

        assert response.status_code == expectations
        if response.status_code == 200:
            assert body['id'] == agents[test_input]['agent_id']
            assert body['email'] == agents[test_input]['email']
            assert body['counterparties'][0]['name'] == agents[test_input]['counterparty_name']
        elif response.status_code == 400:
            assert body['detail'] == "Could not get agent data"

    @pytest.mark.parametrize("test_input, expectations", [('active', 200)])
    def test_user_info(self, log_in, test_input, expectations):
        agent = log_in.user(test_input)
        response = get_user_info(agent)
        body = json.loads(response.text)

        assert response.status_code == expectations
        assert body['email'] == agents[test_input]['email']
        assert body['email_verified'] == True

    @pytest.mark.parametrize("test_input, expectations", [('active', 200)])
    def test_current_app_version_request(self, log_in, test_input, expectations):
        agent = log_in.user(test_input)
        response = get_current_version(agent)

        assert response.status_code == expectations
