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
    
    team_update_requests = boldsign.TeamUpdateRequest(
        teamId="8b637de3-27db-4603-a7d7-6a4fdd0124b8",
        teamName="Sales"                
    )  
    
    update_team_response = teams_api.update_team(
        team_update_request=team_update_requests
    )
    
    print(f"Team successfully updated")