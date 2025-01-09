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
    
    delete_document_response = document_api.delete_document(
        document_id="3f6b8caa-b2ad-43e6-891f-a4711d243127"
    )
    
    print(f"Successfully document deleted")