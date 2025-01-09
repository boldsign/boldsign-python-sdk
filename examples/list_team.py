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
    
    team_list_response = teams_api.list_teams(
        page_size=10, page=1
    )
    
    print(f"Teams list:{team_list_response.results}")