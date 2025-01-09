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
    
    notification_settings = boldsign.NotificationSettings(
        viewed=True,
        sent=False,
        deliveryFailed=True,
        declined=True,
        revoked=True,
        reassigned=True,
        completed=True,
        signed=True,
        expired=True,
        authenticationFailed=True,
        reminders=True
    )
    
    edit_sender_identity_requests = boldsign.EditSenderIdentityRequest(
        name="Luther",
        notificationSettings=notification_settings,
        redirectUrl="https://boldsign-dev.com"
    )
    
    update_sender_identities_response = sender_identities_api.update_sender_identities(
        email="luthercooper@cubeflakes.com",
        edit_sender_identity_request=edit_sender_identity_requests
    )
    
    print(f"Sender identities successfully updated")