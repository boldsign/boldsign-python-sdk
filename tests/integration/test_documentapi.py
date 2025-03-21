import unittest

import pytest
import boldsign
import os
import time
import base64
from boldsign.rest import ApiException
from datetime import datetime, timedelta, timezone

APIKey = os.getenv('API_KEY')
url = os.getenv('HOST_URL')

@pytest.mark.integration
class TestDocumentApi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.created_document_id = None
        cls.created_document_id_textbox_field = None
        cls.sender_email = None
    
    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=APIKey, host=url)
        self.api_client = boldsign.ApiClient(self.configuration)

    def save_file(self, file_name, file_content):
        full_file_name = "tests/documents/output/" + file_name
        with open(full_file_name, "wb") as file:
            file.write(file_content)
        return full_file_name  # Return the full file name
       
    def pdf_to_base64(self, pdf_file_path):
        pdf_file_path = "tests/documents/input/" + pdf_file_path
        with open(pdf_file_path, "rb") as png_file:
            pdf_content = png_file.read()
            base64_content = "data:application/pdf;base64," + base64.b64encode(pdf_content).decode('utf-8')
        return base64_content
    

    def image_to_base64(self, image_path):
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            image_type = image_path.split('.')[-1]  # Extract the image type from the file extension
            return f"data:image/{image_type};base64,{encoded_image}"
        
    @pytest.mark.run(order=1)
    def test_get_sender_details(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Define parameters for listing documents
            page = 1
            page_size = 10

            documents = self.document_api.list_documents(
                page=page,
                page_size=page_size
            )
            assert documents is not None
            assert len(documents.result) > 0
            TestDocumentApi.sender_email=documents.result[0].sender_detail.email_address
            print("SenderEmail:"+TestDocumentApi.sender_email)

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        finally:
            time.sleep(5)
        
    @pytest.mark.run(order=2)
    def test_send_document_positive(self):
        try:
            print("SenderEmail"+TestDocumentApi.sender_email)
            phone_number = boldsign.PhoneNumber(
                countryCode = "+91",
                number = "9876543210"
            )

            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocumentRequest = boldsign.SendForSign(
                title="Document SDK API",
                document_title = "SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=["tests/documents/input/doc_1.pdf"],
                enablePrintAndSign =True,
                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="girisankar.syncfusion@gmail.com",
                        signerOrder=1,
                        signerType="Signer",
                        authenticationType="AccessCode",
                        authenticationCode="123456",
                        formFields=[
                            boldsign.FormField(
                                name="Sign",
                                fieldType="Signature",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            )
                        ],
                        privateMessage="This is private message for signer"
                    ),
                    
                    boldsign.DocumentSigner(
                        name="Test Reviewer",
                        emailAddress="girisankar.syncfusion+1@gmail.com",
                        signerOrder=2,
                        signerType="Reviewer",
                        authenticationType="SMSOTP",
                        phoneNumber=phone_number,
                        privateMessage="This is private message for Reviewer"
                    ),
                    
                    boldsign.DocumentSigner(
                        name="Test In-Person Signer",
                        emailAddress="girisankar.syncfusion+2@gmail.com",
                        signerOrder=3,
                        signerType="InPersonSigner",
                        hostEmail= TestDocumentApi.sender_email,
                        authenticationType="EmailOTP",
                        formFields=[
                            boldsign.FormField(
                                name="Sign",
                                fieldType="Signature",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            )
                        ]
                    )
                ],
            )

            sendDocument = self.document_api.send_document(sendDocumentRequest)
            assert sendDocument is not None
            assert isinstance(sendDocument, boldsign.DocumentCreated)
            assert sendDocument.document_id is not None
            TestDocumentApi.created_document_id = sendDocument.document_id
            print("test Doc ID:" + TestDocumentApi.created_document_id)  
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=3)
    def test_send_document_negative(self):
        try:

            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocument = self.document_api.send_document(boldsign.SendForSign())
            
            assert sendDocument is None
        except ApiException as e:          
            assert e.reason == "Bad Request"
            assert e.status == 400
            print(e.body)
            assert e.body is not None
            assert e.body.splitlines("{\"errors\":{\"Signers\":[\"Minimum one signer is needed to create a document\"]},\"type\":\"https://tools.ietf.org/html/rfc7231#section-6.5.1\",\"title\":\"One or more validation errors occurred.\",\"status\":400,")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=4)
    def test_extend_expiry_positive(self):       
        try:
            print("test Doc ID:" + TestDocumentApi.created_document_id)          
            self.document_api = boldsign.DocumentApi(self.api_client)             

            #Calculate new expiry date (3 months from now)
            new_expiry_date = (datetime.now(timezone.utc) + timedelta(days=90)).strftime("%Y-%m-%d")

            # Define parameters for listing documents
            documentId =  TestDocumentApi.created_document_id
            extendExpiry = boldsign.ExtendExpiry(
                newExpiryValue= new_expiry_date
            )

            extend_expiry = self.document_api.extend_expiry(
                document_id= documentId,
                extend_expiry= extendExpiry
            )
            assert extend_expiry is None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"    
    

    @pytest.mark.run(order=5)
    def test_extend_expiry_negative(self):
       
        try:          
            self.document_api = boldsign.DocumentApi(self.api_client)             

            #Calculate new expiry date (3 months from now)
            new_expiry_date = (datetime.now(timezone.utc) + timedelta(days=90)).strftime("%Y-%m-%d")

            # Define parameters for listing documents
            documentId =  "WrongDocumentId"
            extendExpiry = boldsign.ExtendExpiry(
                newExpiryValue= new_expiry_date
            )

            extend_expiry = self.document_api.extend_expiry(
                document_id= documentId,
                extend_expiry= extendExpiry
            )
        except ApiException as e:
             print(e.body)
             assert e.status == 404
             assert e.reason == "Not Found"
             assert e.body == '{"error":"Invalid Document ID"}'
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=6)
    def test_document_list_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Define parameters for listing documents
            page = 1
            page_size = 10

            documents = self.document_api.list_documents(
                page=page,
                page_size=page_size,
            )
            assert documents is not None
            assert len(documents.result) > 0
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
    
    @pytest.mark.run(order=7)
    def test_document_list_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Define parameters for listing documents
            page = 300
            page_size = 250

            documents = self.document_api.list_documents(
                page=page,
                page_size=page_size,
            )
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"PageSize\":[\"Provide a valid page size between 1 and 100\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    @pytest.mark.run(order=8)
    def test_team_document_positive(self):        
        try:          
            self.document_api = boldsign.DocumentApi(self.api_client) 

            # Define parameters for listing documents           
            page = 1
            page_size = 10
            team_documents = self.document_api.team_documents(
                page=page,
                page_size=page_size
            )
            assert team_documents is not None
            assert len(team_documents.result) > 0    
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=9)
    def test_team_document_negative(self):   
       
        try:          
            self.document_api = boldsign.DocumentApi(self.api_client) 

            # Define parameters for listing documents           
            page = 300
            page_size = 250
            team_documents = self.document_api.team_documents(
                page=page,
                page_size=page_size
            )
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"PageSize\":[\"Provide a valid page size between 1 and 100\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=10)
    def test_behalf_list_positive(self):
       
        try:          
            self.document_api = boldsign.DocumentApi(self.api_client) 

            # Define parameters for listing documents           
            page = 1
            page_size = 10
            behalf_documents = self.document_api.behalf_documents(
                page=page,
                page_size=page_size
            )
            assert behalf_documents is not None
            assert len(behalf_documents.result) == 0    
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=11)
    def test_behalf_list_negative(self):     
       
        try:          
            self.document_api = boldsign.DocumentApi(self.api_client) 

            # Define parameters for listing documents           
            page = 300
            page_size = 250
            behalf_documents = self.document_api.behalf_documents(
                page=page,
                page_size=page_size
            )
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"PageSize\":[\"Provide a valid page size between 1 and 100\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=12)
    def test_document_properties_positive(self):             
        try:          
            self.document_api = boldsign.DocumentApi(self.api_client) 

            # Define parameters for properties
            documentId =  TestDocumentApi.created_document_id
            document_properties = self.document_api.get_properties(
                document_id=documentId
            )
            assert document_properties is not None
            assert document_properties.document_id == TestDocumentApi.created_document_id
            # assert document_properties.title, "Document SDK API"
            # assert document_properties.document_title, "SDK Document Test case"
            # assert document_properties.description, "Testing document from SDK integration test case"
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
    

    @pytest.mark.run(order=13)
    def test_document_properties_negative(self):             
        try:          
            self.document_api = boldsign.DocumentApi(self.api_client) 

            # Define parameters for properties
            documentId =  "WrongDocumentId"
            document_properties = self.document_api.get_properties(document_id=documentId)
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body is not None
            assert e.body.startswith('{"errors":{"documentId":["Provide valid document id."]},')
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)
    
    @pytest.mark.run(order=14)
    def test_download_document_positive(self):        
        try:          
            self.document_api = boldsign.DocumentApi(self.api_client) 

            # Define parameters for download document         
            documentId = TestDocumentApi.created_document_id

            download_documents = self.document_api.download_document(
              document_id = documentId
            )

            assert download_documents is not None
            assert len(download_documents) > 0  
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
    
    @pytest.mark.run(order=15)
    def test_download_document_negative(self):        
        try:          
            self.document_api = boldsign.DocumentApi(self.api_client) 

            # Define parameters for download document         
            documentId =  "WrongDocumentId"

            download_documents = self.document_api.download_document(
              document_id = documentId
            )
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body is not None
            assert e.body.startswith('{"errors":{"documentId":["Provide valid document id."]},')
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"


    @pytest.mark.run(order=16)
    def test_change_access_code_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = TestDocumentApi.created_document_id      
           
            # Define the new access code
            change_access_code_request = boldsign.AccessCodeDetails(
                accessCode = "55555"
            )

            # Call the API to change the access code
            change_response = self.document_api.change_access_code(
                document_id = documentId,
                access_code_details = change_access_code_request,
                email_id= "girisankar.syncfusion@gmail.com"
            )

            assert change_response is None  # Assuming the response is None on success
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=17)
    def test_change_access_code_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = "WrongDocumentId"

            # Define the new access code
            change_access_code_request = boldsign.AccessCodeDetails(
                accessCode = "987654321",
            )
            # Call the API to change the access code
            change_response = self.document_api.change_access_code(
                document_id = documentId,
                access_code_details = change_access_code_request,
                email_id = "girisankar.syncfusion@gmail.com",
                z_order = 1
            )
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"DocumentId\":[\"The field DocumentId is invalid.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=18)
    def test_change_recipient_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = TestDocumentApi.created_document_id

            # Define the chage recipient request
            change_recipient_request = boldsign.ChangeRecipient(
                newSignerName="Test Signer",
                newSignerEmail = "girisankar.syncfusion+new@gmail.com",
                oldSignerEmail = "girisankar.syncfusion@gmail.com",
                reason="Test change recipient"
            )

            # Call the API to change the recipient
            change_response = self.document_api.change_recipient(
                document_id = documentId,
                change_recipient = change_recipient_request
            )
            assert change_response is None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=19)
    def test_change_recipient_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = "WrongDocumentId"

            # Define the chage recipient request
            change_recipient_request = boldsign.ChangeRecipient(
                newSignerName="Test Signer",
                newSignerEmail = "girisankar.syncfusion+new@gmail.com",
                oldSignerEmail = "girisankar.syncfusion@gmail.com",
                reason="Test change recipient"
            )

            # Call the API to change the recipient
            change_response = self.document_api.change_recipient(
                document_id = documentId,
                change_recipient = change_recipient_request
            )
            assert change_response is None
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"documentId\":[\"The field documentId is invalid.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"     

    @pytest.mark.run(order=20)
    def test_add_tags_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = TestDocumentApi.created_document_id

            #Define the document tags
            document_tags = boldsign.DocumentTags(
                documentId = documentId,
                tags = ["Test_Tag1", "Test_Tag2"]
            )

            #Define the add tag request
            add_tag_request = self.document_api.add_tag(
                document_tags = document_tags
            )
            assert add_tag_request is None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=21)
    def test_add_tags_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = "WrongDocumentId"

            #Define the document tags
            document_tags = boldsign.DocumentTags(
                documentId = documentId,
                tags = ["Test_Tag1", "Test_Tag2"]
            )

            #Define the add tag request
            add_tag_request = self.document_api.add_tag(
                document_tags = document_tags
            )
            assert add_tag_request is None
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"DocumentId\":[\"Provide valid document id.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"      

    @pytest.mark.run(order=22)
    def test_delete_tags_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = TestDocumentApi.created_document_id

            #Define the delete tags
            document_tags = boldsign.DocumentTags(
                documentId = documentId,
                tags = ["Test_Tag1", "Test_Tag2"]
            )

            #Define the delete tag request
            delete_tag_request = self.document_api.delete_tag(
                document_tags = document_tags
            )
            assert delete_tag_request is None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=23)
    def test_delete_tags_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = "WrongDocumentId"

            #Define the delete tags
            document_tags = boldsign.DocumentTags(
                documentId = documentId,
                tags = ["Test_Tag1", "Test_Tag2"]
            )

            #Define the delete tag request
            delete_tag_request = self.document_api.delete_tag(
                document_tags = document_tags
            )
            assert delete_tag_request is None
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"DocumentId\":[\"Provide valid document id.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"   

    @pytest.mark.run(order=24)
    def test_remove_authentication_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = TestDocumentApi.created_document_id

            #Define the remove authentication
            remove_authentication = boldsign.RemoveAuthentication(
                emailId="girisankar.syncfusion+new@gmail.com"
            )

            #Define the remove authentication request
            remove_authentication_request = self.document_api.remove_authentication(
                document_id=documentId,
                remove_authentication=remove_authentication
            )
            assert remove_authentication_request is None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=25)
    def test_remove_authentication_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = "WrongDocumentId"

            #Define the remove authentication
            remove_authentication = boldsign.RemoveAuthentication(
                emailId="girisankar.syncfusion+new@gmail.com"
            )

            remove_authentication_request = self.document_api.remove_authentication(
                document_id=documentId,
                remove_authentication=remove_authentication
            )
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"DocumentId\":[\"The field DocumentId is invalid.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"   

    @pytest.mark.run(order=26)
    def test_add_authentication_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = TestDocumentApi.created_document_id

            #Define the add authentication
            add_authentication = boldsign.AccessCodeDetail(
                authenticationType="AccessCode",
                emailId="girisankar.syncfusion+new@gmail.com",
                accessCode="123456789"
            )

            #Define the add authentication request
            add_authentication_request = self.document_api.add_authentication(
                document_id=documentId,
                access_code_detail = add_authentication
            )
            assert add_authentication_request is None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=27)
    def test_add__authentication_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = "WrongDocumentId"

            #Define the add authentication
            add_authentication = boldsign.AccessCodeDetail(
                authenticationType="AccessCode",
                emailId="girisankar.syncfusion+new@gmail.com"
            )

            add_authentication_request = self.document_api.add_authentication(
                document_id=documentId,
                access_code_detail=add_authentication
            )
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"AccessCode\":[\"AccessCode cannot be null or empty when authentication type is AccessCode\"],")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=28)
    def test_revoke_document_positive(self):
        try:
           
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = TestDocumentApi.created_document_id

            # Revoke the document
            revoke_request = boldsign.RevokeDocument(
                message="Testing revoke document API"
            )
            revoke_response = self.document_api.revoke_document(
                document_id=documentId,
                revoke_document=revoke_request
            )

            assert revoke_response is None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
    
    @pytest.mark.run(order=29)
    def test_revoke_document_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            document_id = "WrongDocumentId"

            # Revoke the document
            revoke_request = boldsign.RevokeDocument(
                message="Testing revoke document API"
            )
            revoke_response = self.document_api.revoke_document(
                document_id=document_id,
                revoke_document=revoke_request
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"documentId\":[\"Provide valid document id.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"


    @pytest.mark.run(order=30)
    def test_delete_document_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            document_id = TestDocumentApi.created_document_id

            # Delete the document
            delete_response = self.document_api.delete_document(document_id=document_id)

            assert delete_response is None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=31)
    def test_delete_document_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            document_id = "WrongDocumentId"

            # Delete the document
            delete_response = self.document_api.delete_document(document_id=document_id)

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"documentId\":[\"Provide valid document id.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"          
         
    
    @pytest.mark.run(order=32)
    def test_send_document_with_image_field(self):
        try:
            image_path = "tests\documents\input\logo.png" 
            base64_image = self.image_to_base64(image_path)

            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocumentRequest = boldsign.SendForSign(
                title="Document SDK API",
                document_title = "SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=["tests/documents/input/nda-document.pdf"],
                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="girisankar.syncfusion@gmail.com",
                        signerOrder=1,
                        signerType="Signer",
                        authenticationType="AccessCode",
                        authenticationCode="123456",
                        formFields=[
                            boldsign.FormField(
                                name="image_Test",
                                fieldType="Image",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                value=base64_image,
                                imageInfo=boldsign.ImageInfo(
                                    title="Image Test",
                                   allowedFileExtensions=".png",
                                   description="Image for testing"
                                ),
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            )
                        ],
                        privateMessage="This is private message for signer"
                    ),
                ],
            )

            sendDocument = self.document_api.send_document(sendDocumentRequest)
            assert sendDocument is not None
            assert isinstance(sendDocument, boldsign.DocumentCreated)
            assert sendDocument.document_id is not None
            TestDocumentApi.created_document_id = sendDocument.document_id
            print("test Doc ID:" + TestDocumentApi.created_document_id)  
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)                     
         
    
    @pytest.mark.run(order=33)
    def test_send_document_with_file_url(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocumentRequest = boldsign.SendForSign(
                title="Document SDK API",
                document_title = "SDK Document Test case",
                description="Testing document from SDK integration test case",
                fileUrls=["https://fir-demo-html.web.app/BasicTags1.pdf", "https://fir-demo-html.web.app/test-document1.pdf"],
                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="girisankar.syncfusion@gmail.com",
                        signerOrder=1,
                        signerType="Signer",
                        authenticationType="AccessCode",
                        authenticationCode="123456",
                        formFields=[
                            boldsign.FormField(
                                name="Sign",
                                fieldType="Signature",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            )
                        ],
                        privateMessage="This is private message for signer"
                    ),
                ],
            )

            sendDocument = self.document_api.send_document(sendDocumentRequest)
            assert sendDocument is not None
            assert isinstance(sendDocument, boldsign.DocumentCreated)
            assert sendDocument.document_id is not None
            TestDocumentApi.created_document_id = sendDocument.document_id
            print("test Doc ID:" + TestDocumentApi.created_document_id)  
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)
        
    #How to set a checkbox field to checked and read-only by default when sending documents using API?
    @pytest.mark.run(order=34)
    def test_send_document_checkbox_field_to_checked_and_read_only(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocumentRequest = boldsign.SendForSign(
                title="Document SDK API",
                document_title = "SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=["tests/documents/input/doc_1.pdf"],
                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="girisankar.syncfusion@gmail.com",
                        signerOrder=1,
                        signerType="Signer",
                        authenticationType="AccessCode",
                        authenticationCode="123456",
                        formFields=[
                            boldsign.FormField(
                                id="CheckBox",
                                name="CheckBox",
                                fieldType="CheckBox",
                                font="Helvetica",
                                value="on",
                                pageNumber=1,
                                isReadOnly=True,
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            )
                        ],
                        privateMessage="This is private message for signer"
                    )
                ],
            )

            sendDocument = self.document_api.send_document(sendDocumentRequest)
            assert sendDocument is not None
            assert isinstance(sendDocument, boldsign.DocumentCreated)
            assert sendDocument.document_id is not None
            TestDocumentApi.created_document_id = sendDocument.document_id
            print("test Doc ID:" + TestDocumentApi.created_document_id)  
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)
        
    #How to add group checkboxes to the document using BoldSign API?
    @pytest.mark.run(order=35)
    def test_send_document_add_group_checkboxes(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocumentRequest = boldsign.SendForSign(
                title="Document SDK API",
                document_title = "SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=["tests/documents/input/doc_1.pdf"],
                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="girisankar.syncfusion@gmail.com",
                        signerOrder=1,
                        signerType="Signer",
                        authenticationType="AccessCode",
                        authenticationCode="123456",
                        formFields=[
                            boldsign.FormField(
                                id="CheckBox1",
                                name="CheckBox1",
                                fieldType="CheckBox",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            ),
                            boldsign.FormField(
                                id="CheckBox2",
                                name="CheckBox2",
                                fieldType="CheckBox",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                bounds=boldsign.Rectangle(x=100, y=100, width=100, height=150)
                            ),
                            boldsign.FormField(
                                id="CheckBox3",
                                name="CheckBox3",
                                fieldType="CheckBox",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                bounds=boldsign.Rectangle(x=150, y=200, width=100, height=150)
                            ),
                            boldsign.FormField(
                                id="CheckBox4",
                                name="CheckBox4",
                                fieldType="CheckBox",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                bounds=boldsign.Rectangle(x=200, y=200, width=100, height=150)
                            ),
                        ]
                    )
                ]
            )

            sendDocument = self.document_api.send_document(sendDocumentRequest)
            assert sendDocument is not None
            assert isinstance(sendDocument, boldsign.DocumentCreated)
            assert sendDocument.document_id is not None
            TestDocumentApi.created_document_id = sendDocument.document_id
            print("test Doc ID:" + TestDocumentApi.created_document_id)  
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)               
         
    #How to replace fillable fields with BoldSign form fields via API?
    @pytest.mark.run(order=36)
    def test_replace_fillable_fields(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocumentRequest = boldsign.SendForSign(
                title="Document SDK API",
                document_title = "SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=["tests/documents/input/doc_1.pdf"],
                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="girisankar.syncfusion@gmail.com",
                        signerOrder=1,
                        signerType="Signer",
                        authenticationType="AccessCode",
                        authenticationCode="123456",
                        formFields=[
                            boldsign.FormField(
                                name="Sign",
                                fieldType="Signature",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            )
                        ],
                        privateMessage="This is private message for signer"
                    ),
                ],
                AutoDetectFields=True
            )

            sendDocument = self.document_api.send_document(sendDocumentRequest)
            assert sendDocument is not None
            assert isinstance(sendDocument, boldsign.DocumentCreated)
            assert sendDocument.document_id is not None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)                   
         
    #How to configure recipient notifications in BoldSign using API requests?
    @pytest.mark.run(order=37)
    def test_recipient_notifications(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocumentRequest = boldsign.SendForSign( 
                title="Document SDK API",
                document_title = "SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=["tests/documents/input/doc_1.pdf"],
                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="girisankar.syncfusion@gmail.com",
                        signerOrder=1,
                        signerType="Signer",
                        authenticationType="AccessCode",
                        authenticationCode="123456",
                        formFields=[
                            boldsign.FormField(
                                name="Sign",
                                fieldType="Signature",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            )
                        ],
                        privateMessage="This is private message for signer",
                        recipientNotificationSettings= boldsign.RecipientNotificationSettings(
                            viewed=True,
                            completed=True,
                            declined=True,
                            expired=True,
                            reassigned=True,
                            reminders=True,
                            revoked=True,
                            sent=True,
                            signed=True
                        )
                        
                    ),
                ],
                AutoDetectFields=True
            )

            sendDocument = self.document_api.send_document(sendDocumentRequest)
            assert sendDocument is not None
            assert isinstance(sendDocument, boldsign.DocumentCreated)
            assert sendDocument.document_id is not None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)                    
         
    #How to get signatures by prefilling readonly form fields?    
    @pytest.mark.run(order=37)
    def test_send_document_text_field(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocumentRequest = boldsign.SendForSign(
                title="Document SDK API",
                document_title = "SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=["tests/documents/input/doc_1.pdf"],
                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="girisankar.syncfusion@gmail.com",
                        signerOrder=1,
                        signerType="Signer",
                        formFields=[
                            boldsign.FormField(
                                id="textValue",
                                fieldType="TextBox",
                                font="Helvetica",
                                pageNumber=1,
                                isReadOnly=True,
                                validationType="NumbersOnly",
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            )
                        ]
                    ),
                ]
            )

            sendDocument = self.document_api.send_document(sendDocumentRequest)
            assert sendDocument is not None
            assert isinstance(sendDocument, boldsign.DocumentCreated)
            TestDocumentApi.created_document_id_textbox_field = sendDocument.document_id
            assert sendDocument.document_id is not None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)  

    #How to get signatures by prefilling readonly form fields?   
    @pytest.mark.run(order=38)
    def test_prefilling_readonly_fields(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            prefill_field_requests = boldsign.PrefillFieldRequest(
                fields=[
                    boldsign.PrefillField(
                    id="textValue",
                    value="123456789"
                )
                ]
            )
            documentId = TestDocumentApi.created_document_id_textbox_field

            prefillFields = self.document_api.prefill_fields(
                document_id=documentId,
                prefill_field_request=prefill_field_requests                
            )
            assert prefillFields is  None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"                  
         
    #How to request the signatures without email notifications using BoldSign API?
    @pytest.mark.run(order=39)
    def test_send_document_disable_email(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocumentRequest = boldsign.SendForSign(
                title="Document SDK API",
                document_title = "SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=["tests/documents/input/doc_1.pdf"],
                disableEmails=True,
                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="girisankar.syncfusion@gmail.com",
                        signerOrder=1,
                        signerType="Signer",
                        formFields=[
                            boldsign.FormField(
                                id="textValue",
                                fieldType="TextBox",
                                font="Helvetica",
                                pageNumber=1,
                                isReadOnly=True,
                                validationType="NumbersOnly",
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            )
                        ]
                    ),
                ]
            )

            sendDocument = self.document_api.send_document(sendDocumentRequest)
            assert sendDocument is not None
            assert isinstance(sendDocument, boldsign.DocumentCreated)
            TestDocumentApi.created_document_id_textbox_field = sendDocument.document_id
            assert sendDocument.document_id is not None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)                  
         
    #How to set multiple CCs for signers using BoldSign API?
    @pytest.mark.run(order=40)
    def test_send_document_multiple_CC(self):
        try:

            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocumentRequest = boldsign.SendForSign(
                title="Document SDK API",
                document_title = "SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=["tests/documents/input/doc_1.pdf"],
                cc=[
                    boldsign.DocumentCC(
                        emailAddress="DianaDavid@gmail.com"
                    ),
                    boldsign.DocumentCC(
                        emailAddress="testsdk123@gmail.com"                        
                    ),
                    boldsign.DocumentCC(
                        emailAddress="ClaraThomas@gmail.com"                        
                    )
                ],
                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="girisankar.syncfusion@gmail.com",
                        signerOrder=1,
                        signerType="Signer",
                        formFields=[
                            boldsign.FormField(
                                id="textValue",
                                fieldType="TextBox",
                                font="Helvetica",
                                pageNumber=1,
                                isReadOnly=True,
                                validationType="NumbersOnly",
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            )
                        ]
                    ),
                ]
            )

            sendDocument = self.document_api.send_document(sendDocumentRequest)
            assert sendDocument is not None
            assert isinstance(sendDocument, boldsign.DocumentCreated)
            TestDocumentApi.created_document_id_textbox_field = sendDocument.document_id
            assert sendDocument.document_id is not None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)  

if __name__ == '__main__':
    unittest.main()