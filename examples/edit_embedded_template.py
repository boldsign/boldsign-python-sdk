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
    
    embedded_template_edit_requests = boldsign.EmbeddedTemplateEditRequest(
        showTooltip=True,
        viewOption="PreparePage",
        showSaveButton=True,
        showCreateButton=True,
        showPreviewButton=True,
        showNavigationButtons=True,
        showToolbar=False
    )
    
    templateId = "c7de007a-3a19-4f5d-bd37-994d2186a2b3"
       
    get_embedded_template_edit_url_response = template_api.get_embedded_template_edit_url(
        template_id=templateId,
        embedded_template_edit_request=embedded_template_edit_requests
    )
    
    print(f"Successfully edit embedded template url: {get_embedded_template_edit_url_response}")