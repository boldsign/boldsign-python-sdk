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
    
    reset_brand_response = branding_api.reset_default_brand(
        brand_id="YOUR_BRAND_ID"
    )
    
    print(f"Brand successfully reset default")