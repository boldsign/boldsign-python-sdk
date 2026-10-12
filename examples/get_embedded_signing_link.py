import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign
from datetime import datetime, timezone

configuration = boldsign.Configuration(
    api_key = "ZjVjNTczMGEtOTljNC00OTliLWEwYjMtNjc4MjAyMTFlZTY0",
    host="https://staging-api.boldsign.com"
)
with boldsign.ApiClient(configuration) as api_client:
    
    document_api = boldsign.DocumentApi(api_client)
    
    documentId = "d784e65a-2e12-4c6d-92c9-081d001a8d10"
    signingEmail = "hankwhite@cubeflakes.com"
    redirectUrl= "https://www.syncfusion.com/"
    signLinkValidTill=datetime(2026, 10, 9, 8, 49, 0, tzinfo=timezone.utc)
    
    get_embedded_sign_link_response = document_api.get_embedded_sign_link(
        document_id=documentId,
        signer_email=signingEmail,
        redirect_url=redirectUrl,
        sign_link_valid_till=signLinkValidTill
    )
    
    print(f"Embedded sign link: {get_embedded_sign_link_response.sign_link}")