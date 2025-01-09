import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:
    
    user_api = boldsign.UserApi(api_client)
    
    cancel_invitation_response = user_api.cancel_invitation(
        user_id="0f6d64c3-54b6-49c8-a933-149cbe0b8cc0"
    )
    
    print(f"User invitation successfully cancel")