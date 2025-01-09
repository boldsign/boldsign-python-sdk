import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)
#Use the following sample code snippet to change the access code for the signer who has already been authenticated.
with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)
    
    access_code_details = boldsign.AccessCodeDetails(
        accessCode="123456"
    )
    
    response = document_api.change_access_code(
        document_id="9b6e89e8-708e-4ee7-a37d-a604b552df46",
        access_code_details=access_code_details,
        email_id="alexgayle@cubeflakes.com"
    )
    
    print(f"Access code successfully changed")

#If a document contains a repeated signer with a signing order, in that case, the recipient's signing order can be specified along with the signer's email to change the access code, as shown in the following code snippet.   
with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)
    
    access_code_details = boldsign.AccessCodeDetails(
        accessCode="123456"
    )
    
    response = document_api.change_access_code(
        document_id="9b6e89e8-708e-4ee7-a37d-a604b552df46",
        access_code_details=access_code_details,
        email_id="alexgayle@cubeflakes.com",
        z_order=2
    )
    
    print(f"Access code successfully changed")