import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:

    contacts_api = boldsign.ContactsApi(api_client)

    delete_contact_response = contacts_api.delete_contacts(
        id="{your Document Id}"
    )