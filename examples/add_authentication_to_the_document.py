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
    
    access_code_detail = boldsign.AccessCodeDetail(
        authenticationType="EmailOTP",
        emailId="david@example.com"
    )
    
    add_authentication_response = document_api.add_authentication(
        document_id="0d5535e0-abc3-4ac1-ae95-4a64b84cded2",
        access_code_detail=access_code_detail
    )
    
    print(f"EmailOTP authentication successfully added to the document")

#The following sample code snippet requests the AccessCode authentication to be added to one of the document's recipients.   
with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)
    
    
    access_code_detail = boldsign.AccessCodeDetail(
        authenticationType="AccessCode",
        accessCode="123456",
        emailId="david@example.com"
    )
    
    response = document_api.add_authentication(
        document_id="55a9f1ad-e46b-4e25-abe0-6d944d10374f",
        access_code_detail=access_code_detail
    )
    
    print(f"AccessCode authentication successfully added to the document")

#The following code sample snippet requests the SMS OTP authentication to be added to one of the document's recipients.
with boldsign.ApiClient(configuration) as api_client:
    
    document_api = boldsign.DocumentApi(api_client)
    
    phoneNumber = boldsign.PhoneNumber(
        country_code="+91",
        number="6381261236"
    )
    
    access_code_detail = boldsign.AccessCodeDetail(
        authenticationType="SMSOTP",
        phone_number=phoneNumber,
        emailId="prakash.viswanathan+signer@syncfusion.com"
    )
    
    response = document_api.add_authentication(
        document_id="b50b87bb-0780-4671-a25c-06014bb91a0d",
        access_code_detail=access_code_detail
    )
    
    print(f"SMSOTP authentication successfully added to the document")

#If a document contains repeated signers with signing order, in that case the recipient's signing order can be specified along with the signer's email to add the EmailOTP authentication request, as shown in the following code snippet.        
with boldsign.ApiClient(configuration) as api_client:
    
    document_api = boldsign.DocumentApi(api_client)
    
    access_code_details = boldsign.AccessCodeDetail(
        authenticationType="EmailOTP",
        emailId="girisankar.syncfusion@gmail.com",
        order=1
    )
    
    response = document_api.add_authentication(
        document_id="48d03b85-f23b-4000-8fa7-c34dfd153526",
        access_code_detail=access_code_details
    )
    
    print(f"EmailOTP with order authentication successfully added to the document")