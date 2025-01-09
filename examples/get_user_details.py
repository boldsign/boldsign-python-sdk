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
    
    user_details_response = user_api.get_user(
        user_id="0a148566-57b7-4745-875d-8d98be0aa6e0"
    )
    
    print(f"User details:{user_details_response}")