import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host = os.getenv('BoldSignApiUrl')
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
        )
    ]
    role1 = boldsign.Role(
        roleIndex=1,
        signerEmail="john.doe@domain.com",
        signerName="John Doe",
        message="Please sign the document",
        signerRole="Manager",
        signerOrder=1,
        signerType="Signer"
    )
    role2 = boldsign.Role(
        roleIndex=2,
        signerEmail="sivaramani.sivaraj@syncfusion.com",
        signerName="Siva Ramani",
        message="Please sign the document",
        signerRole="Engineer",
        signerOrder=2,
        signerType="Signer",
        formFields=form_fields
    )
    embedded_merge_create_template_request = boldsign.EmbeddedMergeTemplateFormRequest(
        files=["tests/documents/input/doc_1.pdf","tests/documents/input/nda-document.pdf"],
        title="API template",
        description="API template description",
        templateIds=["YOUR_TEMPLATE_ID1","YOUR_TEMPLATE_ID2"],
        roles=[role1,role2]
        
    )
    embedded_merge_template_url = template_api.merge_create_embedded_request_url_template(embedded_merge_template_form_request=embedded_merge_create_template_request)
    print("Embedded Merge Template URL:", embedded_merge_template_url)