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

    listContactResponse = contacts_api.contact_user_list(
        page_size=10,
        page=1
    )