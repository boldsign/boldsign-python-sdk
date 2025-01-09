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
            id = "Signature1",
            fieldType="Signature",
            page_number=1,  
            bounds=boldsign.Rectangle(
                x=50,
                y=100,
                width=100,
                height=60
            ),
            is_required=True
        )
    ]
    
    role = boldsign.TemplateRole(
        index=1,
        name="Manager",
        defaultSignerName="Alex Gayle",
        defaultSignerEmail="alexgayle@boldsign.dev",
        signerOrder=1,
        signerType="Signer",
        formFields=form_fields
    )
    
    template_id = "YOUR_TEMPLATE_ID"
    
    edit_template_request = boldsign.EditTemplateRequest(   
        title="A new title for template",
        enableSigningOrder=False,
        roles=role
    )
    
    edit_template_response = template_api.edit_template(template_id, edit_template_request)
    
    print(f"Template with ID {template_id} has been edited successfully.")