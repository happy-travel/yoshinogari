import json
from API.Agents.getCurrentAgentInformation import get_current_agent_information
from API.identity.getUserInfo import get_user_info
from API.library.support.data import active_user_name, active_password, active_agent_email, active_counterparty_name


class TestAccompaingMethods:

    def test_current_agent_information_request(self, log_in):
        agent = log_in.agent(active_user_name, active_password)
        response = get_current_agent_information(agent)
        body = json.loads(response.text)

        assert response.status_code == 200
        assert body['id'] == 236
        assert body['email'] == active_agent_email
        assert body['counterparties'][0]['name'] == active_counterparty_name

    def test_user_info(self, log_in):
        agent = log_in.agent(active_user_name, active_password)
        response = get_user_info(agent)
        body = json.loads(response.text)

        assert response.status_code == 200
        assert body['email'] == active_agent_email
        assert body['email_verified'] == True
