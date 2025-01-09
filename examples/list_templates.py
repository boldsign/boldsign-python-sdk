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
    
    page = 1 
    
    page_size = 10 
    
    list_templates_response = template_api.list_templates(page=page, page_size=page_size)