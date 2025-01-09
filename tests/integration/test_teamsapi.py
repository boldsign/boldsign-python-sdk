import unittest
import pytest
import boldsign
import os
import time
from boldsign.rest import ApiException
from random import randint

APIKey = os.getenv('BoldSignAPIKey')
url = os.getenv('BoldSignURL')

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
        self.configuration = boldsign.Configuration(api_key=APIKey, host=url)
        self.api_client = boldsign.ApiClient(self.configuration)
        srting_value = self.random_numbers()
        TestUsersApi.team_Name = "sdktestingteam"+srting_value

    @pytest.mark.run(order=78)
    def test_create_teams_positive(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)
            
            # Define parameters for create team
            team_Name =  TestUsersApi.team_Name
            create_team_requests = boldsign.CreateTeamRequest(
                teamName=team_Name
            )   
            
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

    
    @pytest.mark.run(order=79)
    def test_create_teams_negative(self):
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
            
    @pytest.mark.run(order=80)
    def test_get_user_list_positive(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)

            # Define parameters for contact teams list
            Page =1
            Page_size = 20
            
                        
            teams_list_response = self.teams_api.list_teams(
                page=Page,
                page_size=Page_size
            )
            assert teams_list_response is not None
            assert teams_list_response.results is not None
            TeamsList = teams_list_response.results
            assert isinstance(teams_list_response, boldsign.TeamListResponse)

            for teams in TeamsList:
                if teams.team_name == TestUsersApi.team_Name:
                    TestUsersApi.team_id = teams.team_id

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"     
            
    @pytest.mark.run(order=81)
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
            
    @pytest.mark.run(order=82)
    def test_get_team_positive(self):
        try:
            self.teams_api = boldsign.TeamsApi(self.api_client)

            # Define parameters for get team
            teamId = TestUsersApi.team_id
                        
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
            
    @pytest.mark.run(order=83)
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

    @pytest.mark.run(order=84)
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
            
    @pytest.mark.run(order=85)
    def test_update_team_negative(self):
        try:           
            self.teams_api = boldsign.TeamsApi(self.api_client)
            
           # Define parameters for update team
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


if __name__ == '__main__':
    unittest.main()