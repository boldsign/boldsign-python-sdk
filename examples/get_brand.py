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
    
    brand_details_response = branding_api.get_brand(
        brand_id="a10f3ce5-03c1-4bf7-bc71-4a36cf97de0f"
    )
    
    print(f"Brand details: {brand_details_response}")