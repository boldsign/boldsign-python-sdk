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
    contactDetails = [
        boldsign.ContactDetails(
            email="luthercooper1@cubeflakes.com",
            name="LutherCooper1",
            phoneNumber= boldsign.PhoneNumber(
                countryCode="+91",
                number="6381261236"
            ),
            jobTitle= "Developer",
            companyName="CubeFlakes"
        ),
        boldsign.ContactDetails(
            email="hankwhite1@cubeflakes.com",
            name="HankWhite1",
            phoneNumber=boldsign.PhoneNumber(
                countryCode="+91",
                number="8807799764"
            ),
            jobTitle= "Manager",
            companyName="CubeFlakes"           
        ),
    ]
    CreateContactResponse = contacts_api.create_contact(
        contact_details=contactDetails
    )