import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:
    
    branding_api = boldsign.BrandingApi(api_client)
    
    list_brand_response = branding_api.brand_list()
    
    print(f"Brand list: {list_brand_response.result}")