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
            bounds=boldsign.Rectangle(
                x=100,
                y=100,
                width=100,
                height=50
            )
        ),
    ]

    role = boldsign.Role(
        role_index=50,
        signer_name="Richard",
        signer_order=1,
        signer_email="richard@cubeflakes.com",
        private_message="Please check and sign the document.",
        authentication_code="281028",
        enableEmailOTP=False,
        signerType='Signer',
        signerRole='Manager',
        formFields=form_fields,
        locale="EN"
    )

    template_id = "c7de007a-3a19-4f5d-bd37-994d2186a2b3"

    send_for_sign_from_template_form = boldsign.SendForSignFromTemplateForm(
        files=["D:/Github/22.10.2024/Examples/open-api-sdk/python/sdk/tests/documents/input/nda-document.pdf"],
        title="Invitation form",
        message="Kindly review and sign this.",
        roles=[role],
        labels=["Invitation"],
        disableEmails=False,
        disableSMS=False,
        hideDocumentId=True,
        reminderSettings=boldsign.ReminderSettings(
            reminderDays=3,
            reminderCount=5,
            enableAutoReminder=False
        ),
        expiryDays=180,
        expiryDateType="Days",
        expiryValue=60,
        disableExpiryAlert=True,
        enablePrintAndSign=True,
        enableReassign=True,
        enableSigningOrder=True,
        roleRemovalIndices=[1,2]
    )

    response = template_api.send_using_template(template_id, send_for_sign_from_template_form)

    print(f"Template sent successfully. Document ID: {response.document_id}")