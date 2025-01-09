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

    get_properties_response = document_api.get_properties(document_id="8f59295d-xxxx-xxxx-xxxx-e7dc88cfff2c")

    print(f"Document properties: {get_properties_response}")