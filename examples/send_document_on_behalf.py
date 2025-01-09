import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)

    form_field = [
        boldsign.FormField(
            id="string",
            name="string",
            fieldType="Signature",
            font="Helvetica",
            pageNumber=1,
            bounds=boldsign.Rectangle(
                x=50,
                y=50,
                width=200,
                height=25
            ),
            isRequired=True
        )
    ]

    signer = boldsign.DocumentSigner(
        name="David",
        emailAddress="david@cubeflakes.com",
        signerOrder=1,
        signerType="Signer",
        formFields=form_field,
        locale="EN"
    )

    send_for_sign = boldsign.SendForSign(
        document_title = "SDK Document Test case",
        description="Testing document from SDK integration test case",
        files=["D:/Github/22.10.2024/Examples/open-api-sdk/python/sdk/tests/documents/input/nda-document.pdf"],
        disableExpiryAlert=False,
        reminderSettings=boldsign.ReminderSettings(
            reminderDays=3,
            reminderCount=5,
            enableAutoReminder=False
        ),
        enableReassign=True,
        message='Please sign this.', 
        signers=[signer],
        expiryDays=10,
        enablePrintAndSign=False,
        AutoDetectFields=False,
        onBehalfOf="luthercooper@cubeflakes.com",
        enableSigningOrder=False,
        useTextTags=False,
        title="Agreement",
        hideDocumentId=False,
        enableEmbeddedSigning=False,
        expiryDateType='Days',
        expiryDate=60,
        disableEmails=False,
        disableSMS=False,
    )

    send_document_response = document_api.send_document(send_for_sign)

    print(f"Document sent successfully. Document ID: {send_document_response.document_id}")