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

    behalf_documents_response = document_api.behalf_documents(page_size=10, page=1)
    
    print(f"Behalf Document List: {behalf_documents_response}")