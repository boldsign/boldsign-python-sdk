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
    
    edit_brand_response = branding_api.edit_brand(
        brand_id="a10f3ce5-03c1-4bf7-bc71-4a36cf97de0f",
        brand_name="BoldSign",
        background_color="red",
        button_color="green",
        button_text_color="white",
        email_display_name="SenderName from BoldSign",
        redirect_url="https://www.boldsign-dev.com/",
        is_default=True,
        can_hide_tag_line=True,
        combine_audit_trail=True,
        document_time_zone="+05:30",
        email_signed_document="1",
        hide_decline=False,
        hide_save=False,
        brand_logo='D:/Github/22.10.2024/Examples/open-api-sdk/python/sdk/tests/documents/input/logo.png'
    )
    
    print(f"Brand successfully updated")