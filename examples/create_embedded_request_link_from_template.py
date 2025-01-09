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
            is_required=True
        )
    ]

    template_role = boldsign.Role(
        roleIndex=2,
        signerRole="signer",
        signerName="Signer Name 1",
        signerEmail="signer1@boldsign.dev",
        formFields=form_fields
    )
    
    embedded_send_template_form_requests = boldsign.EmbeddedSendTemplateFormRequest(
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
        sendViewOption="PreparePage",
        locale="EN",
        showTooltip=False,
        enableSigningOrder=False,
        roleRemovalIndices=[1, 2],
        files=["D:/Github/22.10.2024/Examples/open-api-sdk/python/sdk/tests/documents/input/nda-document1.pdf"]
    )
    
    create_embedded_request_url_template_response = template_api.create_embedded_request_url_template(
        template_id="c7de007a-3a19-4f5d-bd37-994d2186a2b3",
        embedded_send_template_form_request=embedded_send_template_form_requests
    )
    
    print(f"Successfully created embedded template request url: {create_embedded_request_url_template_response}")