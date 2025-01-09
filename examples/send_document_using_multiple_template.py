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
            fieldType="Signature",
            pageNumber=1,
            font="Helvetica",
            bounds=boldsign.Rectangle(
                x=100,
                y=100,
                width=100,
                height=50
            ),
            isRequired=True
        ),
    ]

    role = boldsign.Role(
        signerRole="NewRole",
        roleIndex=4,
        signerName="David",
        signerEmail="david@cubeflakes.com",
        formFields=form_fields,
        locale="EN"
    )

    merge_and_send_for_sign_form = boldsign.MergeAndSendForSignForm(
        templateIds=["fedd5fd3-ae2c-4696-aadc-d5665c7f9e53", "c7de007a-3a19-4f5d-bd37-994d2186a2b3"],
        roles=[role]
    )

    merge_and_send_response = template_api.merge_and_send(merge_and_send_for_sign_form)

    print(f"Template sent successfully. Document ID: {merge_and_send_response.document_id}")