import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:

    template_api = boldsign.TemplateApi(api_client)
    
    template_id = "c7de007a-3a19-4f5d-bd37-994d2186a2b3"
    
    template_properties_response = template_api.get_properties(template_id)

    print(f"Template ID: {template_properties_response.template_id}")
    print(f"Title: {template_properties_response.title}")
    print(f"Description: {template_properties_response.description}")
    print(f"Document Title: {template_properties_response.document_title}")