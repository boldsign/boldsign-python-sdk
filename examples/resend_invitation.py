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
    
    resend_sender_identities_response = sender_identities_api.resend_invitation_sender_identities(
        email="luthercooper@cubeflakes.com",
    )
    
    print(f"Resend invitation sender identitie")