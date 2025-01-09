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
    
    team_details_response = teams_api.get_team(
        team_id="a5016cef-7bcd-4a60-b8bf-98fed2183b5c"
    )
    
    print(f"Team details:{team_details_response}")