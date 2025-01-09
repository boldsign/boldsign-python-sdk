import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:
    
    sender_identities_api = boldsign.SenderIdentitiesApi(api_client)
    
    list_sender_identities_response = sender_identities_api.list_sender_identities(
        page=1, page_size=10
    )
    
    print(f"Sender identities list:{list_sender_identities_response.result}")