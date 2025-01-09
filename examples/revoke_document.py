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

    revoke_document = boldsign.RevokeDocument(
        message="This is document revoke message"
    )
    
    revoke_document_response = document_api.revoke_document(
        document_id="4a140c48-88fe-479a-9543-b23074234691",
        revoke_document=revoke_document
    )
    
    print(f"Successfully document revoked")