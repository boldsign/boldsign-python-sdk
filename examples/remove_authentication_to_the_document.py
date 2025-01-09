import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

#The following sample code snippet requests for the removal of authentication for a particular recipient in the document signing process.
with boldsign.ApiClient(configuration) as api_client:
    
    document_api = boldsign.DocumentApi(api_client)
    
    remove_authentication = boldsign.RemoveAuthentication(
        emailId="alexgayle@cubeflakes.com"
    )
    
    remove_authentication_response = document_api.remove_authentication(
        document_id="b50b87bb-0780-4671-a25c-06014bb91a0d",
        remove_authentication =remove_authentication
    )
    
    print(f"Authentication successfully removed to the document")

#If a document contains repeated signers with signing order, in that case, the recipient's signing order can be specified along with the signer's email in the remove authentication request, as shown in the following code snippet.      
with boldsign.ApiClient(configuration) as api_client:
    
    document_api = boldsign.DocumentApi(api_client)
    
    remove_authentication = boldsign.RemoveAuthentication(
        emailId="alexgayle@cubeflakes.com",
        zOrder=2

    )
    
    remove_authentication_response = document_api.remove_authentication(
        document_id="b50b87bb-0780-4671-a25c-06014bb91a0d",
        remove_authentication =remove_authentication
    )
    
    print(f"Authentication successfully removed to the document")