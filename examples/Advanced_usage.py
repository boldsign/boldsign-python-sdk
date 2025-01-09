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

    form_fields = [
        boldsign.FormField(
            id="Signature",
            name="Signature",
            fieldType="Signature",
            pageNumber=1,
            font="Helvetica",
            bounds=boldsign.Rectangle(
                x=50,
                y=50,
                width=200,
                height=25
            ),
            isRequired=True
        ),
        boldsign.FormField(
            id="Label",
            name="Label",
            fieldType="Label",
            value="Label Field",
            font="Helvetica",
            pageNumber=1,
            bounds=boldsign.Rectangle(
                x=150,
                y=250,
                width=200,
                height=25
            ),
            isRequired=True
        ),
    ]

    document_signer = boldsign.DocumentSigner(
        name="David",
        emailAddress="david@cubeflakes.com",
        signerOrder=1,
        signerType="Signer",
        formFields=form_fields,
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
        signers=[document_signer],
        expiryDays=10,
        enablePrintAndSign=False,
        AutoDetectFields=False,
        onBehalfOf='',
        enableSigningOrder=False,
        title="Document SDK API",
        hideDocumentId=False,
        enableEmbeddedSigning=False,
        expiryDateType='Days',
        expiryDate=60,
        disableEmails=False,
        disableSMS=False,
        useTextTags=True,
        textTagDefinitions= [
            boldsign.TextTagDefinition(
                definitionId="tag1",
                type="TextBox",
                signerIndex=1,
                isRequired=True,
                label="Email field",
                font=boldsign.Font(
                    name="Helvetica",
                    size=20,
                    style="Italic"
                ),
                fieldId="axq12367",
                size=boldsign.Size(
                    width=500,
                    height=50
                ),
                placeholder="Enter your email here",
                validation=boldsign.Validation(
                    type="Email"
                ),
                offset= boldsign.TextTagOffset(
                    offsetX=0,
                    offsetY=0
                )
            )
        ]
    )

    send_document_response = document_api.send_document(send_for_sign)