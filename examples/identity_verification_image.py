import sys
import os

import boldsign.api_client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:
    identity_verification_api = boldsign.IdentityVerificationApi(api_client)
    identity_verification_image = boldsign.DownloadImageRequest(
       emailId="sivaramani.sivaraj@syncfusion.com",
       countryCode="+91",
       phoneNumber="87654345678",
       fileId="YOUR_FILE_ID",
       order=1
    )
    document_id = "YOUR_DOCUMENT_ID" 
    image_response = identity_verification_api.image(document_id, identity_verification_image)
    print("Image resposne : " ,image_response)