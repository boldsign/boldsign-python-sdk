import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:
    
    teams_api = boldsign.TeamsApi(api_client)
    
    create_team_request = boldsign.CreateTeamRequest(
        teamName="HR"                
    )
    
    create_team_response = teams_api.create_team(
        create_team_request=create_team_request
    )
    
    print(f"Team successfully created")