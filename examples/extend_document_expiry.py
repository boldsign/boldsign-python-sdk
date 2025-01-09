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

    extend_expiry = boldsign.ExtendExpiry(
        newExpiryValue="2022-12-15",
        warnPrior=True
    )

    extend_expiry_response = document_api.extend_expiry(
        document_id="4a140c48-88fe-479a-9543-b23074234691",
        extend_expiry=extend_expiry
    )
    
    print(f"Successfully expiry date extended")