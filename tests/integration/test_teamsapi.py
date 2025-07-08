import unittest
from boldsign.api.teams_api import TeamsApi
from boldsign.models.team_list_response import TeamListResponse
import pytest
import boldsign
import time
from boldsign.rest import ApiException
from random import randint
from config import API_KEY, BASE_URL

@pytest.mark.integration
class TestUsersApi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.team_Name = None
        cls.team_id = None

    def random_numbers(self):
        range_start = 10**(3-1)
        range_end = (10**3)-1
        return str(randint(range_start, range_end))
    
    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=API_KEY, host=BASE_URL)
        self.api_client = boldsign.ApiClient(self.configuration)
        srting_value = self.random_numbers()
        TestUsersApi.team_Name = "sdktestingteam"+srting_value

    @pytest.mark.run(order=191)
    def test_create_teams_positive(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)
            
            # Define parameters for create team
            team_Name =  TestUsersApi.team_Name
            create_team_requests = boldsign.CreateTeamRequest(
                teamName=team_Name
            )
            print(team_Name)
            create_team_response = self.teams_api.create_team(
                create_team_request= create_team_requests
            )
            assert create_team_response is not None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(10)

    @pytest.mark.run(order=192)
    def test_create_teams_negative_duplicate_name(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)
            
            # Define parameters for create team
            team_Name = TestUsersApi.team_Name
            create_team_requests = boldsign.CreateTeamRequest(
                teamName=team_Name
            )
            
            create_team_response = self.teams_api.create_team(
                create_team_request= create_team_requests
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"error\":\"Team Name already exists\"}")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}" 
        finally:
            time.sleep(5)

    @pytest.mark.run(order=193)
    def test_create_team_negative_empty_name(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)

            # Empty team name
            create_team_request = boldsign.CreateTeamRequest(
                teamName=""
            )

            response = self.teams_api.create_team(
                create_team_request=create_team_request
            )
            assert False, "Expected failure due to empty team name."
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"TeamName\":[\"The TeamName field is required.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"  
        finally:
            time.sleep(5)

    @pytest.mark.run(order=194)
    def test_get_team_list_positive(self):
        try:
            # Initialize the Teams API client
            self.teams_api = TeamsApi(self.api_client)

            # Define parameters for contact teams list
            Page = 1
            Page_size = 100

            # Make the API call to retrieve the teams list
            teams_list_response = self.teams_api.list_teams(
                page=Page,
                page_size=Page_size
            )

            # Assert that the response is not None
            assert teams_list_response is not None, "Response is None"

            # Assert that the response contains results
            assert teams_list_response.results is not None, "Results are None"

            # Store the list of teams
            TeamsList = teams_list_response.results

            # Assert that the response is of type TeamListResponse
            assert isinstance(teams_list_response, TeamListResponse), \
                "Response is not of type TeamListResponse"

            # Log the list of team names to help with debugging
            print(f"Teams List: {[team.team_name for team in TeamsList]}")

            # Initialize created_team_id as None
            created_team_id = None

            # Loop through the teams list to find the team by name
            for team in TeamsList:
                if team.team_name == TestUsersApi.team_Name:
                    created_team_id = team.team_id
                    TestUsersApi.team_id = created_team_id
                    print(f"Found team with ID: {created_team_id}")
                    break

            # If created_team_id is still None, log an error and raise an exception
            if created_team_id is None:
                raise ValueError(f"Team with name {TestUsersApi.team_Name} not found in the list.")

            # Assert that the team ID was found
            assert created_team_id is not None, "Created team ID was not found."

            # Print the team ID for verification
            print(f"Team ID: {created_team_id}")

        except ApiException as e:
            # Catch BoldSign API exceptions
            print(f"\nException when calling BoldSign API: {e}")
            assert False, f"API Exception occurred: {str(e)}"

        except Exception as e:
            # Catch all other exceptions
            print(f"\nException when calling BoldSign: {e}")
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=195)
    def test_get_team_list_negative(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)

            # Define parameters for contact team list
            Page =250
            Page_size = 250
            
                        
            team_list_response = self.teams_api.list_teams(
                page=Page,
                page_size=Page_size
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"PageSize\":[\"Provide a valid page size between 1 and 100\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=196)
    def test_get_team_list_negative_with_null_values(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)

            # Define parameters for contact team list
            Page =0
            Page_size =0
            
            team_list_response = self.teams_api.list_teams(
                page=Page,
                page_size=Page_size
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert "Page number should be greater than 0" in e.body
            assert "Provide a valid page size between 1 and 100" in e.body
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=197)
    def test_get_team_positive(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)
            
            # Define parameters for get team
            teamId = TestUsersApi.team_id
            print(f"teamid: {teamId}")

            get_team_response = self.teams_api.get_team(
                team_id=teamId
            )
            assert get_team_response is not None
            assert get_team_response.team_name is not None
            assert get_team_response.team_name == TestUsersApi.team_Name
            assert isinstance(get_team_response, boldsign.TeamResponse)

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=198)
    def test_get_team_negative(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)

            # Define parameters for get team
            teamId = "wrongTeamId"
                        
            get_team_response = self.teams_api.get_team(
                team_id=teamId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"teamId\":[\"Please provide valid team ID\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"          
        finally:
            time.sleep(5)

    @pytest.mark.run(order=199)
    def test_get_team_negative_empty_teamid(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)

            # Define parameters for get team
            teamId = ""

            get_team_response = self.teams_api.get_team(
                team_id=teamId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"teamId\":[\"The teamId field is required.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=200)
    def test_update_team_negative_duplicate_name(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)
            
            # Define parameters for update team
            team_Id = TestUsersApi.team_id
            update_team_request = boldsign.TeamUpdateRequest(
                teamId= team_Id,
                teamName=TestUsersApi.team_Name
            )
            
            update_team_response = self.teams_api.update_team(
                team_update_request=update_team_request
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert "Team Name already exists" in e.body
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"  
        finally:
            time.sleep(5)

    @pytest.mark.run(order=201)
    def test_update_team_positive(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)
            
            # Define parameters for update team
            team_Id = TestUsersApi.team_id
            team_Name = TestUsersApi.team_Name
            update_team_request = boldsign.TeamUpdateRequest(
                teamId= team_Id,
                teamName="Update"+team_Name
            )
            
            update_team_response = self.teams_api.update_team(
                team_update_request=update_team_request
            )
            assert update_team_response is None  

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"     
        finally:
            time.sleep(5)

    @pytest.mark.run(order=202)
    def test_update_team_negative_invalid_teamid(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)
            
            team_Id = "WrongTeamId"
            update_team_request = boldsign.TeamUpdateRequest(
                teamId= team_Id,
                teamName="Update sdk testing team"
            )
            
            update_team_response = self.teams_api.update_team(
                team_update_request=update_team_request
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"TeamId\":[\"Please provide valid team ID\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"  
        finally:
            time.sleep(5)

    @pytest.mark.run(order=203)
    def test_update_team_negative_empty_teamName(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)
            
            team_Id = TestUsersApi.team_id
            update_team_request = boldsign.TeamUpdateRequest(
                teamId= team_Id,
                teamName=""
            )
            
            update_team_response = self.teams_api.update_team(
                team_update_request=update_team_request
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"TeamName\":[\"The TeamName field is required.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"  
        finally:
            time.sleep(5)

if __name__ == '__main__':
    unittest.main()