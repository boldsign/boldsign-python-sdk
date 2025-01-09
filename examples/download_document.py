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
    
    download_attachment_response = document_api.download_document(
        document_id="f3a20eac-0ea8-42d1-b2ca-589e478684ad"
    )
    
    print(f"Successfully document downloaded: {download_attachment_response}")