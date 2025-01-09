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
    
    form_fields = [
        boldsign.FormField(
            id = "sign_id",
            name = "sign",
            fieldType="Signature",
            page_number=1,
            font="Helvetica",
            bounds=boldsign.Rectangle(
                x=50,
                y=100,
                width=100,
                height=60
            ),
            is_required=True,
            backgroundHexColor="string"
        )
    ]
    
    template_role = boldsign.TemplateRole(
        index=1,
        name="Manager"
    )
    
    embedded_create_template_request = boldsign.EmbeddedCreateTemplateRequest (
        title="API template",
        description="API template description",
        documentTitle="API document title",
        documentMessage="API document message description",
        allowMessageEditing=True,    
        roles=[template_role],        
        showToolbar=True,
        showNavigationButtons=True,
        showPreviewButton=True,
        showSendButton=True,
        showSaveButton=True,
        locale="EN",
        showTooltip=False,
        allowNewFiles=True,
        viewOption="PreparePage",
        files=["D:/Github/22.10.2024/Examples/open-api-sdk/python/sdk/tests/documents/input/nda-document.pdf"],
    )
    
    embedded_request_url_document_response = template_api.create_embedded_template_url(
        embedded_create_template_request=embedded_create_template_request
    )
    
    print(f"Successfully created embedded template request url: {embedded_request_url_document_response}")