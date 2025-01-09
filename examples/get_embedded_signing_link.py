import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:
    
    document_api = boldsign.DocumentApi(api_client)
    
    documentId = "5be9383f-c6de-4f58-8175-5fc663725481"
    signingEmail = "girisankar.syncfusion@gmail.com"
    redirectUrl= "https://www.syncfusion.com/"
    signLinkValidTill=11/14/2024
    
    get_embedded_sign_link_response = document_api.get_embedded_sign_link(
        document_id=documentId,
        signer_email=signingEmail,
        redirect_url=redirectUrl,
        sign_link_valid_till=signLinkValidTill
    )
    
    print(f"Embedded sign link: {get_embedded_sign_link_response.sign_link}")