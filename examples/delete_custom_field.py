import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:
    
    custom_field_api = boldsign.CustomFieldApi(api_client)
    
    delete_custom_fields_response = custom_field_api.delete_custom_field(
        custom_field_id="YOUR_BRAND_ID"
    )
    
    print(f"custom fields successfully deleted:{delete_custom_fields_response.message}")