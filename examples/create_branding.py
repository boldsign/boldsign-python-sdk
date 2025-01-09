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
    
    create_brand_response = branding_api.create_brand(
        brand_name="Syncfusion",
        background_color="red",
        button_color="green",
        button_text_color="white",
        email_display_name="{SenderName} from Syncfusion",
        redirect_url="https://www.syncfusion.com/",
        is_default=True,
        can_hide_tag_line=True,
        combine_audit_trail=True,
        document_time_zone="+05:30",
        email_signed_document="1",
        hide_decline=False,
        hide_save=False,
        brand_logo="D:/Github/22.10.2024/Examples/open-api-sdk/python/sdk/tests/documents/input/logo.png"
    )
    
    print(f"Brand successfully created")