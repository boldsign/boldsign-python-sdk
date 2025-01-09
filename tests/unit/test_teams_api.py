import unittest
from unittest.mock import patch, MagicMock
import pytest
import boldsign
from boldsign.models.create_team_request import CreateTeamRequest
from boldsign.models.team_created import TeamCreated
from boldsign.rest import ApiException
from pydantic import ValidationError

class TestTeamsApi(unittest.TestCase):

    @patch('boldsign.TeamsApi')
    @pytest.mark.unit
    def test_create_team_positive(self, mock_teams_api):
        mock_teams_api_instance = mock_teams_api.return_value
        mock_response = TeamCreated(team_id="team123")
        mock_teams_api_instance.create_team.return_value = mock_response

        create_team_request = CreateTeamRequest(team_name="New Team")

        response = mock_teams_api_instance.create_team(create_team_request)

        self.assertIsNotNone(response)
        self.assertEqual(response.team_id, "team123")
        mock_teams_api_instance.create_team.assert_called_once_with(create_team_request)

    @patch('boldsign.TeamsApi')
    @pytest.mark.unit
    def test_create_team_missing_name(self, mock_teams_api):
        mock_teams_api_instance = mock_teams_api.return_value
        mock_teams_api_instance.create_team.side_effect = ApiException(status=400, reason="Bad Request: Missing team name")

        create_team_request = CreateTeamRequest(team_name="")

        with self.assertRaises(ApiException) as context:
            mock_teams_api_instance.create_team(create_team_request)

        self.assertEqual(context.exception.status, 400)
        self.assertEqual(context.exception.reason, "Bad Request: Missing team name")
        mock_teams_api_instance.create_team.assert_called_once_with(create_team_request)

    @patch('boldsign.TeamsApi')
    @pytest.mark.unit
    def test_create_team_invalid_name_length(self, mock_teams_api):
        with self.assertRaises(ValidationError) as context:
            CreateTeamRequest(team_name="A" * 256)

        self.assertIn('String should have at most 255 characters', str(context.exception))

    @patch('boldsign.TeamsApi')
    @pytest.mark.unit
    def test_create_team_api_exception(self, mock_teams_api):
        mock_teams_api_instance = mock_teams_api.return_value
        mock_teams_api_instance.create_team.side_effect = ApiException(status=500, reason="Internal Server Error")

        create_team_request = CreateTeamRequest(team_name="New Team")

        with self.assertRaises(ApiException) as context:
            mock_teams_api_instance.create_team(create_team_request)

        self.assertEqual(context.exception.status, 500)
        self.assertEqual(context.exception.reason, "Internal Server Error")
        mock_teams_api_instance.create_team.assert_called_once_with(create_team_request)

if __name__ == '__main__':
    unittest.main()
