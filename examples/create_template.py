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
    
    role = [
        boldsign.TemplateRole(
            index=1,
            name="Hr",
            defaultSignerName="Alex Gayle",
            defaultSignerEmail="alexgayle@boldsign.dev",
            signerOrder=1,
            signerType="Signer",
            locale="EN",
            imposeAuthentication="None",
            deliveryMode="Email",
            formFields=form_fields,
            allowRoleEdit=True,
            allowRoleDelete=True
        )
    ]
    # can only edit or delete the existing form field
    form_field_permission = boldsign.FormFieldPermission(
        can_add=False,
        can_modify=True,
        can_modify_default_value=False
    )

    
    create_template_request = boldsign.CreateTemplateRequest(
        enableReassign=True,
        allowNewRoles=True,
        enablePrintAndSign=False,
        documentMessage="document message for signers",
        enableSigningOrder=False,
        useTextTags=False,
        title="title of the template",
        allowMessageEditing=True,
        description="testingDescription",
        documentTitle= "title of the document",
        allowNewFiles=True,
        roles=role,
        form_field_permission = form_field_permission,
        files=["tests/documents/input/nda-document.pdf"]
    )

    create_template_response = template_api.create_template(create_template_request=create_template_request)

    print(f"Template created with ID: {create_template_response.template_id}")