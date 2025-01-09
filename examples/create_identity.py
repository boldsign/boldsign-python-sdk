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
    
    create_sender_identity_requests = boldsign.CreateSenderIdentityRequest(
        name="Luther Cooper",
        email="luthercooper@cubeflakes.com",
        notificationSettings=notification_settings,
        redirectUrl="https://boldsign.com"
    )
    
    create_sender_identities_response = sender_identities_api.create_sender_identities(
        create_sender_identity_request=create_sender_identity_requests
    )

    print(f"Sender identities successfully created")