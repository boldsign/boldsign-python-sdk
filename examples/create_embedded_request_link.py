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
            id="Sign",
            fieldType="Signature",
            pageNumber=1,
            font="Helvetica",
            bounds=boldsign.Rectangle(
                x=50,
                y=50,
                width=200,
                height=30
            ),
            isRequired=True
        )
    ] 
    
    document_signer = boldsign.DocumentSigner(
        name="Signer Name 1",
        emailAddress="signer1@boldsign.dev",
        signerOrder=1,
        signerType="Signer",
        authenticationCode="1123",
        privateMessage="This is private message for signer",
        formFields=form_fields,
        locale="EN"
    )
    
    embedded_document_request = boldsign.EmbeddedDocumentRequest(
        title="Sent from API Python SDK",
        showToolbar=True,
        showNavigationButtons=True,
        showPreviewButton=True,
        showSendButton=True,
        showSaveButton=True,
        sendViewOption="FillingPage",
        locale="EN",
        # sendLinkValidTill="2022-10-21T06:37:57.424Z",
        showTooltip=False,
        redirectUrl="https://boldsign.dev/sign/redirect",
        message="This is document message sent from API Python SDK",
        enableSigningOrder=False,
        signers=[document_signer],
        files=["D:/Github/22.10.2024/Examples/open-api-sdk/python/sdk/tests/documents/input/nda-document.pdf"],           
    )
    
    embedded_request_url_document_response = document_api.create_embedded_request_url_document(
        embedded_document_request=embedded_document_request
    )

    print(f"Successfully created embedded request url document: {embedded_request_url_document_response.document_id}")