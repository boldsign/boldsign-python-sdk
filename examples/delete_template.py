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
    
    template_id = "f58bfd58-6210-467f-9623-d917ddc8eb76" 
    
    delete_template_response=template_api.delete_template(template_id)
    
    print(f"Template with ID {template_id} has been deleted successfully.")