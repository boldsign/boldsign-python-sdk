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

    ContactDetails = boldsign.ContactDetails(
        email="hankwhite@cubeflakes.com",
        name="HankWhite",
        phoneNumber= boldsign.PhoneNumber(
            countryCode="+91",
            number="8807799763"
        ),
        jobTitle= "Developer",
        companyName="Test"
    )

    updateContactResponse = contacts_api.update_contact(
        id="0a148566-57b7-4745-875d-8d98be0aa6e0c_YYG3c",
        contact_details=ContactDetails
    )