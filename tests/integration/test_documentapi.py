import unittest
import pytest
import boldsign
import time
import os
import base64
from boldsign import FormField, DocumentSigner, EmbeddedDocumentRequest, EmbeddedSendCreated
from boldsign.models.document_created import DocumentCreated
from boldsign.models.document_info import DocumentInfo
from boldsign.models.reminder_settings import ReminderSettings
from boldsign.models.send_for_sign import SendForSign
from boldsign.rest import ApiException
from datetime import datetime, timedelta, timezone
from config import API_KEY, BASE_URL

@pytest.mark.integration
class TestDocumentApi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.created_document_id = None
        cls.created_document_id1 = None
        cls.created_document_id_textbox_field = None
        cls.sender_email = None
        cls.created_brand_id = None
        cls.send_document_onBehalf_id = None
    
    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=API_KEY, host=BASE_URL)
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
    def test_create_brand_with_combined_audit_trail_positive(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters for create brand
            brand_name = 'TestBrandAPI'
            brand_logo = 'tests/documents/input/logo.png'
            background_color = "#FFFFFF"
            button_color = "#000000"
            button_text_color = "#FFFFFF"
            combine_audit_trail = True
            
            create_branding_response = self.branding_api.create_brand(
                brand_name=brand_name,
                brand_logo=brand_logo,
                background_color=background_color,
                button_color=button_color,
                button_text_color=button_text_color,
                combine_audit_trail=combine_audit_trail
            )

            assert create_branding_response is not None
            assert create_branding_response.brand_id is not None
            assert isinstance(create_branding_response, boldsign.BrandCreated)
            TestDocumentApi.created_brand_id = create_branding_response.brand_id

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(10)

    @pytest.mark.run(order=3)
    def test_send_document_with_branding(self):
        try:
            document_api = boldsign.DocumentApi(self.api_client)

            form_fields = [
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
            document_signer = boldsign.DocumentSigner(
                name="Test Signer",
                emailAddress="girisankar.syncfusion@gmail.com",
                signerOrder=1,
                signerType="Signer",
                authenticationType="AccessCode",
                authenticationCode="123456",
                authenticationSettings=boldsign.AuthenticationSettings(
                    authenticationFrequency="EveryAccess"
                ),
                formFields=form_fields
            )
            reminder_settings = boldsign.ReminderSettings(
                reminderDays=3,
                reminderCount=5,
                enableAutoReminder=True
            )

            send_for_sign = boldsign.SendForSign(
                title="Document SDK API",
                document_title="SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=["tests/documents/input/doc_1.pdf"],
                signers=[document_signer],
                brandId=TestDocumentApi.created_brand_id,
                message="Please sign this document",
                enablePrintAndSign=True,
                AutoDetectFields=True,
                enableEmbeddedSigning=False,
                disableEmails=True,
                disableExpiryAlert=True,
                reminderSettings=reminder_settings,
                deliveryMode="Email",
                MetaData={
                "DocumentType": "new",
                "DocumentCategory": "Software",
                }
            )

            send_document_response = document_api.send_document(send_for_sign)
            TestDocumentApi.created_document_id1 = send_document_response.document_id

            assert send_document_response is not None, "No response received from API"
            assert isinstance(send_document_response, boldsign.DocumentCreated)
            assert send_document_response.document_id is not None, "Document ID is missing"
            print(f"Document sent successfully with ID: {send_document_response.document_id}")

        except boldsign.ApiException as e:
            print(f"Exception when calling BoldSign API: {e}")
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print(f"Unexpected exception occurred: {e}")
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=4)
    def test_send_document_positive(self):
        try:
            print("SenderEmail"+TestDocumentApi.sender_email)
            phone_number = boldsign.PhoneNumber(
                countryCode = "+91",
                number = "6381261236"
            )

            self.document_api = boldsign.DocumentApi(self.api_client)
            sendDocumentRequest = boldsign.SendForSign(
                title="Document SDK API",
                document_title = "SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=["tests/documents/input/doc_1.pdf"],
                enablePrintAndSign =True,
                hideDocumentId=True,
                enableReassign=False,

                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="girisankar.syncfusion@gmail.com",
                        signerOrder=1,
                        signerType="Signer",
                        authenticationType="AccessCode",
                        authenticationCode="123456",
                        authenticationSettings=boldsign.AuthenticationSettings(
                            authenticationFrequency="OncePerDocument"
                        ),
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
                        recipientNotificationSettings={
                        "signatureRequest": True,
                        "declined": True,
                        "revoked": True,
                        "signed": True,
                        "completed": True,
                        "expired": True,
                        "reassigned": True,
                        "deleted": True,
                        "reminders": True,
                        "editRecipient": True
                    }
                    ),

                    boldsign.DocumentSigner(
                        name="Test Reviewer",
                        emailAddress="girisankar.syncfusion+1@gmail.com",
                        signerOrder=2,
                        signerType="Reviewer",
                        authenticationType="SMSOTP",
                        authenticationSettings=boldsign.AuthenticationSettings(
                            authenticationFrequency="None"
                        ),
                        phoneNumber=phone_number,
                        privateMessage="This is private message for Reviewer",
                        deliveryMode="EmailAndSMS",
                    ),

                    boldsign.DocumentSigner(
                        name="Test In-Person Signer",
                        emailAddress="girisankar.syncfusion+2@gmail.com",
                        signerOrder=3,
                        signerType="InPersonSigner",
                        hostEmail= TestDocumentApi.sender_email,
                        authenticationType="EmailOTP",
                        authenticationSettings=boldsign.AuthenticationSettings(
                            authenticationFrequency="UntilSignCompleted"
                        ),
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

    @pytest.mark.run(order=9)
    def test_get_embedded_sign_link_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            signer_email = "girisankar.syncfusion+1@gmail.com"
            country_code = "+91"
            phone_number = "6381261236"

            sign_link_valid_till = datetime.utcnow() + timedelta(days=20)

            redirect_url = "https://www.syncfusion.com/"

            embedded_sign_link = self.document_api.get_embedded_sign_link(
                document_id=TestDocumentApi.created_document_id,
                signer_email=signer_email,
                country_code=country_code,
                phone_number=phone_number,
                sign_link_valid_till=sign_link_valid_till,
                redirect_url=redirect_url
            )

            assert embedded_sign_link is not None, "Embedded signing link is None"
            assert embedded_sign_link.sign_link is not None, "Sign link is None"

        except ApiException as e:
            print(f"\nException when calling BoldSign API: {e}")
            assert False, f"API Exception occurred: {e}"
        except Exception as e:
            print(f"\nUnexpected exception occurred: {e}")
            assert False, f"Unexpected exception occurred: {e}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=6)
    def test_get_embedded_sign_link_neagtive_invalid_document_id(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            signer_email = "girisankar.syncfusion+1@gmail.com"
            country_code = "+91"
            phone_number = "6381261236"

            sign_link_valid_till = datetime.utcnow() + timedelta(days=20)

            redirect_url = "https://www.syncfusion.com/"

            embedded_sign_link = self.document_api.get_embedded_sign_link(
                document_id="invalid_document_id",
                signer_email=signer_email,
                country_code=country_code,
                phone_number=phone_number,
                sign_link_valid_till=sign_link_valid_till,
                redirect_url=redirect_url
            )

            assert embedded_sign_link is  None

        except ApiException as e:
            assert e.status == 403
            print(f"Received expected API exception: {e}")
        except Exception as e:
            print(f"\nUnexpected exception occurred: {e}")
            assert False, f"Unexpected exception occurred: {e}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=17)
    def test_get_embedded_sign_link_missing_phone_number(self):
        self.document_api = boldsign.DocumentApi(self.api_client)

        signer_email = "girisankar.syncfusion+3@gmail.com"
        country_code = "+91"
        phone_number = ""
        sign_link_valid_till = datetime.utcnow() + timedelta(days=20)
        redirect_url = "https://www.syncfusion.com/"

        try:
            embedded_sign_link = self.document_api.get_embedded_sign_link(
                document_id=TestDocumentApi.created_document_id,
                signer_email=signer_email,
                country_code=country_code,
                phone_number=phone_number,
                sign_link_valid_till=sign_link_valid_till,
                redirect_url=redirect_url
            )
        
        except ApiException as e:
            assert e.status == 400
            print(f"Received expected API exception: {e}")
        except Exception as e:
            print(f"Unexpected exception occurred: {e}")
            assert False, f"Unexpected exception occurred: {e}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=8)
    def test_get_embedded_sign_link_invalid_email(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            invalid_email = "invalid-email-format"
            country_code = "+91"
            phone_number = "6381261236"
            sign_link_valid_till = datetime.utcnow() + timedelta(days=20)
            redirect_url = "https://www.syncfusion.com/"

            embedded_sign_link = self.document_api.get_embedded_sign_link(
                document_id=TestDocumentApi.created_document_id,
                signer_email=invalid_email,
                country_code=country_code,
                phone_number=phone_number,
                sign_link_valid_till=sign_link_valid_till,
                redirect_url=redirect_url
            )

        except ApiException as e:
            assert e.status == 400, f"Expected status code 400, but got {e.status}"
            print(f"Received expected API exception: {e}")
        except Exception as e:
            print(f"Unexpected exception occurred: {e}")
            assert False, f"Unexpected exception occurred: {e}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=5)
    def test_send_document_on_behalf(self):
        try:
            document_api = boldsign.DocumentApi(self.api_client)

            form_field = {
                "name": "Sign",
                "fieldType": "Signature",
                "pageNumber": 1,
                "bounds": {
                    "x": 50.0,
                    "y": 50.0,
                    "width": 200.0,
                    "height": 25.0,
                }
            }

            document_signer = {
                "name": "Test Signer",
                "emailAddress": "mohammedmushraf.abuthakir+400@syncfusion.com",
                "signerOrder": 1,
                "signerType": "Signer",
                "formFields": [form_field],
            }

            # Prepare reminder settings
            reminder_settings = {
                "reminderDays": 3,
                "reminderCount": 5,
                "enableAutoReminder": False
            }

            # Prepare the document send request (SendForSign)
            send_for_sign = {
                "title": "SDK Document Test case",
                "message": "Testing document from SDK integration test case",
                "files": ["tests/documents/input/doc_1.pdf"],
                "disableExpiryAlert": False,
                "reminderSettings": reminder_settings,
                "enableReassign": True,
                "signers": [document_signer],
                "enablePrintAndSign": False,
                "autoDetectFields": True, 
                "onBehalfOf": "mohammedmushraf.abuthakir+900@syncfusion.com",
                "enableSigningOrder": False,
                "useTextTags": False,
                "hideDocumentId": False,
                "disableEmails": False,
                "disableSMS": False
            }

            send_document_response = document_api.send_document(send_for_sign)

            print("API Response:", send_document_response)

            TestDocumentApi.send_document_onBehalf_id = send_document_response.document_id

            assert TestDocumentApi.send_document_onBehalf_id  is not None, "Document ID is missing in the response"
            print(f"Successfully sent document for signing. Document ID: {TestDocumentApi.send_document_onBehalf_id}")

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=10)
    def test_send_document_on_behalf_invalid_email(self):
        try:
            document_api = boldsign.DocumentApi(self.api_client)

            form_field = {
                "name": "Sign",
                "fieldType": "Signature",
                "pageNumber": 1,
                "bounds": {
                    "x": 50.0,
                    "y": 50.0,
                    "width": 200.0,
                    "height": 25.0
                }
            }
            
            document_signer = {
                "name": "Test Signer",
                "emailAddress": "mohammedmushraf.abuthakir+400@syncfusion.com",
                "signerOrder": 1,
                "signerType": "Signer",
                "formFields": [form_field],
            }
            
            reminder_settings = {
                "reminderDays": 3,
                "reminderCount": 5,
                "enableAutoReminder": False
            }
            
            send_for_sign = {
                "title": "SDK Document Test case",
                "message": "Testing document from SDK integration test case",
                "files": ["tests/documents/input/doc_1.pdf"],
                "disableExpiryAlert": False,
                "reminderSettings": reminder_settings,
                "enableReassign": True,
                "signers": [document_signer],
                "enablePrintAndSign": False,
                "autoDetectFields": False,
                "onBehalfOf": "invalid-email",
                "enableSigningOrder": False,
                "useTextTags": False,
                "hideDocumentId": False,
                "disableEmails": False,
                "disableSMS": False
            }

            send_document_response = document_api.send_document(send_for_sign)
            assert send_document_response is None

        except ApiException as e:
            print(e.body)
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=11)
    def test_download_on_behalf_document_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client) 
            print(TestDocumentApi.send_document_onBehalf_id)

            documentId = TestDocumentApi.send_document_onBehalf_id
            on_behalf_of_email = "mohammedmushraf.abuthakir+900@syncfusion.com"
            
            download_documents = self.document_api.download_document(
                document_id = documentId,
                on_behalf_of = on_behalf_of_email
            )

            assert download_documents is not None
            assert len(download_documents) > 0
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=12)
    def test_download_on_behalf_document_negative_invalid_documentId(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            documentId = "invalid_documentId"
            on_behalf_of_email = "mohammedmushraf.abuthakir+900@syncfusion.com"
            
            # Attempt to download the document using the invalid document ID
            download_documents = self.document_api.download_document(
                document_id=documentId,
                on_behalf_of=on_behalf_of_email
            )
            assert download_documents is None
        except ApiException as e:
            print(e.body)
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=13)
    def test_download_on_behalf_document_negative_invalid_onBehalf_email(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            print(TestDocumentApi.send_document_onBehalf_id)

            documentId = TestDocumentApi.send_document_onBehalf_id
            invalid_on_behalf_of_email = "invalid-email-format"
            
            self.document_api.download_document(
                document_id=documentId,
                on_behalf_of=invalid_on_behalf_of_email
                )

        except ApiException as e:
            print(e.body)
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=14)
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

    @pytest.mark.run(order=14)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=15)
    def test_extend_expiry_negative(self):

        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            new_expiry_date = (datetime.now(timezone.utc) + timedelta(days=90)).strftime("%Y-%m-%d")

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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=16)
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
            assert e is None
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert e is None
        finally:
            time.sleep(5)
    
    @pytest.mark.run(order=7)
    def test_document_list_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

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
            assert e is None
        finally:
            time.sleep(5)

    @pytest.mark.run(order=18)
    def test_document_list_negative_null_values(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            page = 0
            page_size = 0

            documents = self.document_api.list_documents(
                page=page,
                page_size=page_size,
            )
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert "Page number should be greater than 0" in e.body
            assert "Provide a valid page size between 1 and 100" in e.body
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert e is None
        finally:
            time.sleep(5)

    @pytest.mark.run(order=19)
    def test_team_document_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            page = 1
            page_size = 10
            team_documents = self.document_api.team_documents(
                page=page,
                page_size=page_size
            )
            assert team_documents is not None
            assert len(team_documents.result) >=0
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=20)
    def test_team_document_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=21)
    def test_team_document_negative_neagtiveValues(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            page = -2
            page_size = -9
            team_documents = self.document_api.team_documents(
                page=page,
                page_size=page_size
            )
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert "Page number should be greater than 0" in e.body
            assert "Provide a valid page size between 1 and 100" in e.body
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=22)
    def test_behalf_list_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            page = 1
            page_size = 10
            behalf_documents = self.document_api.behalf_documents(
                page=page,
                page_size=page_size
            )
            assert behalf_documents is not None
            assert len(behalf_documents.result)>=0

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=23)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=24)
    def test_document_properties_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            documentId =  TestDocumentApi.created_document_id
            document_properties = self.document_api.get_properties(
                document_id=documentId
            )
            assert document_properties is not None
            assert document_properties.document_id == TestDocumentApi.created_document_id

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=25)
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

    @pytest.mark.run(order=26)
    def test_document_properties_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Define parameters for properties
            documentId =  ""
            document_properties = self.document_api.get_properties(document_id=documentId)
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert "The documentId field is required." in e.body
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=27)
    def test_download_document_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Define parameters for download document
            documentId = TestDocumentApi.created_document_id1

            download_documents = self.document_api.download_document(
                document_id = documentId
            )

            assert download_documents is not None
            assert len(download_documents) >=0
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

    @pytest.mark.run(order=28)
    def test_download_document_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Define parameters for download document
            documentId =  "WrongDocumentId"

            download_documents = self.document_api.download_document(
                document_id = documentId
            )
            assert download_documents is None
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

    @pytest.mark.run(order=29)
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

            assert change_response is None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=30)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=31)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=32)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=33)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=34)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=35)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=36)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=37)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=38)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=39)
    def test_add_authentication_positive(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            documentId = TestDocumentApi.created_document_id

            #Define the add authentication
            add_authentication = boldsign.AccessCodeDetail(
                authenticationType="AccessCode",
                emailId="girisankar.syncfusion+new@gmail.com",
                accessCode="123456789",
                authenticationSettings=boldsign.AuthenticationSettings(
                    authenticationFrequency="EveryAccess"
                ),
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

    @pytest.mark.run(order=40)
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
            assert add_authentication_request is None
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"AccessCode\":[\"AccessCode cannot be null or empty when authentication type is AccessCode\"],")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=41)
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

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=42)
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

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=43)
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

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=44)
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

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=45)
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

    @pytest.mark.run(order=46)
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

    @pytest.mark.run(order=47)
    def test_send_document_text_field(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            
            sendDocumentRequest = boldsign.SendForSign(
                title="Document SDK API",
                document_title="SDK Document Test case",
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
                                value="12345",
                                font="TimesRoman",
                                fontsize="16",
                                fontcolor="#035efc",
                                pageNumber=1,
                                isReadOnly=True,
                                textDirection="RTL",
                                dataSyncTag="1",
                                validationType="NumbersOnly",
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                            ),
                            boldsign.FormField(
                                id="textValue1",
                                fieldType="TextBox",
                                value="12345",
                                font="TimesRoman",
                                fontsize="16",
                                fontcolor="#035efc",
                                pageNumber=1,
                                textDirection="RTL",
                                charecterLimit="10",
                                dataSyncTag="1",
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

    @pytest.mark.run(order=51)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=49)
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

            assert sendDocument.document_id is not None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=50)
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

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=48)
    def test_create_embedded_request_url_document(self):
        """Test creating an embedded request URL for a document"""

        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            rectangle = {
                "x": 50.0,
                "y": 50.0,
                "width": 200.0,
                "height": 30.0
            }

            # Create form field for signature
            form_field = FormField(
                field_type="Signature",
                page_number=1,
                bounds=rectangle
            )

            # Create document signer
            document_signer = DocumentSigner(
                name="Signer Name 1",
                email_address="mohammedmushraf.abuthakir+400@syncfusion.com",
                signer_order=1,
                signer_type="Signer",
                authenticationType="AccessCode",
                authenticationCode="123456",
                authenticationSettings=boldsign.AuthenticationSettings(
                    authenticationFrequency="EveryAccess"
                ),
                private_message="This is private message for signer",
                form_fields=[form_field],
                locale="EN"
            )

            # Create embedded document request
            embedded_document_request = EmbeddedDocumentRequest(
                files=["tests/documents/input/doc_1.pdf"],
                title="Sent from API Python SDK",
                show_toolbar=True,
                show_navigation_buttons=True,
                show_preview_button=True,
                show_send_button=False,
                show_save_button=True,
                send_view_option="PreparePage",
                locale="ES",
                show_tooltip=False,
                redirect_url="https://boldsign.dev/sign/redirect",
                message="This is document message sent from API Python SDK",
                enable_signing_order=False,
                signers=[document_signer]
            )

                # Call the API to create the embedded request URL
            response = self.document_api.create_embedded_request_url_document(embedded_document_request)

                # Validate the response
            self.assertIsInstance(response, EmbeddedSendCreated)
            self.assertIsNotNone(response.send_url, "Embedded document URL should not be null.")
            print(f"Embedded Document URL: {response.send_url}")

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=52)
    def test_create_embedded_request_url_document_negative(self):
        """Test creating an embedded request URL for a document with an invalid email"""

        try:
            # Initialize the Document API client
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Create rectangle for form field bounds
            rectangle = {
                "x": 50.0,
                "y": 50.0,
                "width": 200.0,
                "height": 30.0
            }

            # Create form field for signature
            form_field = FormField(
                field_type="Signature",
                page_number=1,
                bounds=rectangle
            )

            # Create document signer with an invalid email
            document_signer = DocumentSigner(
                name="Signer Name 1",
                email_address="invalid-email",
                signer_order=1,
                signer_type="Signer",
                authentication_code="1123",
                private_message="This is private message for signer",
                form_fields=[form_field],
                locale="EN"
            )

            # Create embedded document request
            embedded_document_request = EmbeddedDocumentRequest(
                files=["tests/documents/input/doc_1.pdf"],
                title="Sent from API Python SDK",
                show_toolbar=True,
                show_navigation_buttons=True,
                show_preview_button=True,
                show_send_button=True,
                show_save_button=True,
                send_view_option="PreparePage",
                locale="ES",
                show_tooltip=False,
                redirect_url="https://boldsign.dev/sign/redirect",
                message="This is document message sent from API Python SDK",
                enable_signing_order=False,
                signers=[document_signer]
            )

            # Call the API to create the embedded request URL
            response = self.document_api.create_embedded_request_url_document(embedded_document_request)
            assert response is None

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=53)
    def test_send_document_with_radio_buttons(self):
        """Test sending a document with radio buttons and form fields"""

        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            radio_button_field_1 = FormField(
                id="RadioButton1",
                name="RadioButton1",
                field_type="RadioButton",
                value="OFF",
                page_number=1,
                font="Helvetica",
                is_required=True,
                group_name="Group1",
                bounds={
                    "x": 50.0,
                    "y": 50.0,
                    "width": 100.0,
                    "height": 150.0
                }
            )

            radio_button_field_2 = FormField(
                id="RadioButton2",
                name="RadioButton2",
                field_type="RadioButton",
                value="ON",
                page_number=1,
                font="Helvetica",
                is_required=True,
                group_name="Group1",
                bounds={
                    "x": 50.0,
                    "y": 50.0,
                    "width": 100.0,
                    "height": 150.0
                }
            )

            signer = DocumentSigner(
                name="Mohammed Mushraf",
                email_address="mohammedmushraf.abuthakir+300@syncfusion.com",
                signer_type="Signer",
                form_fields=[radio_button_field_1, radio_button_field_2],
                locale="EN"
            )

            send_for_sign = SendForSign(
                files=["tests/documents/input/doc_1.pdf"],
                title="SDK Document Test case",
                message="Please sign this.",
                reminder_settings=ReminderSettings(
                    reminder_days=3,
                    reminder_count=5,
                    enable_auto_reminder=False
                ),
                disable_expiry_alert=False,
                enable_reassign=True,
                signers=[signer],
                enable_print_and_sign=False,
                disable_emails=False,
                disable_sms=False,
                auto_detect_fields=False,
                enable_signing_order=False,
                use_text_tags=False,
                hide_document_id=False
            )

            document_info = DocumentInfo(
                title="SDK Document Test case",
                description="Testing document from SDK integration test case",
                locale="EN"
            )

            send_for_sign.document_info = [document_info]

            send_document_response = self.document_api.send_document(send_for_sign)

            assert isinstance(send_document_response, DocumentCreated)
            assert send_document_response.document_id is not None, "Document ID is missing in the response"
            print(f"Successfully sent document for signing. Document ID: {send_document_response.document_id}")

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=54)
    def test_create_document_positive_with_many_signers(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            file_path = "tests/documents/input/doc_1.pdf"
            files = [file_path]  # Ensure the file exists at this path

            signature_field = boldsign.FormField(
                fieldType="Signature",
                page_number=1,
                bounds=boldsign.Rectangle(x=100, y=100, width=100, height=50)
            )

            signers = []
            for i in range(15):
                signer = boldsign.DocumentSigner(
                    name=f"Signer{i}",
                    email_address=f"mohammedmushraf.abuthakir+{i}@syncfusion.com",
                    formFields=[signature_field]
                )
                signers.append(signer)

            send_for_sign = boldsign.SendForSign(
                title="Agreement",
                files=files,
                signers=signers
            )

            document = self.document_api.send_document(send_for_sign)

            assert document is not None, "Document response is None"
            assert document.document_id is not None, "Document ID is None"

            print(f"Document ID: {document.document_id}")

        except ApiException as e:
            print(f"\nException when calling BoldSign API: {e}")
            assert False, f"API Exception occurred: {e}"
        except Exception as e:
            print(f"\nUnexpected exception occurred: {e}")
            assert False, f"Unexpected exception occurred: {e}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=55)
    def test_send_document_positive_with_multiple_files(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            file1_path = "tests/documents/input/doc_1.pdf"
            file2_path = "tests/documents/input/doc_1.pdf"
            file3_path = "tests/documents/input/nda-document.pdf"
            file4_path = "tests/documents/input/nda-document1.pdf"
            files = [file1_path, file2_path, file3_path, file4_path]

            signature_field = boldsign.FormField(
                fieldType="Signature",
                page_number=1,
                bounds=boldsign.Rectangle(x=100, y=100, width=100, height=50)
            )

            signers = [
                boldsign.DocumentSigner(
                    name="Signer1",
                    email_address="mushrafmohammed.abuthakir+1@syncfusion.com",
                    formFields=[signature_field]
                ),
                boldsign.DocumentSigner(
                    name="Signer2",
                    email_address="mushrafmohammed.abuthakir+2@syncfusion.com",
                    formFields=[signature_field]
                )
            ]

            send_for_sign = boldsign.SendForSign(
                title="Agreement with Multiple Files",
                files=files,
                signers=signers
            )

            document = self.document_api.send_document(send_for_sign)

            assert document is not None, "Document response is None"

            print(f"Document ID: {document.document_id}")

        except ApiException as e:
            print(f"\nException when calling BoldSign API: {e}")
            assert False, f"API Exception occurred: {e}"
        except Exception as e:
            print(f"\nUnexpected exception occurred: {e}")
            assert False, f"Unexpected exception occurred: {e}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=56)
    def test_create_document_negative_invalid_email(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            file_path = "tests/documents/input/doc_1.pdf"
            files = [file_path]

            signature_field = boldsign.FormField(
                fieldType="Signature",
                page_number=1,
                bounds=boldsign.Rectangle(x=100, y=100, width=100, height=50)
            )

            signer = boldsign.DocumentSigner(
                name="Signer",
                email_address="invalid_email",
                formFields=[signature_field]
            )

            send_for_sign = boldsign.SendForSign(
                title="Agreement",
                files=files,
                signers=[signer]
            )

            document = self.document_api.send_document(send_for_sign)

        except ApiException as e:
            assert e.status == 400
            print(f"Received expected API exception: {e}")

        except Exception as e:
            print(f"\nUnexpected exception occurred: {e}")
            assert False, f"Unexpected exception occurred: {e}"

        finally:
            time.sleep(5)

    @pytest.mark.run(order=57)
    def test_create_document_negative_missing_required_field_with_empty_title(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            file_path = "tests/documents/input/doc_1.pdf"
            files = [file_path]

            signature_field = boldsign.FormField(
                fieldType="Signature",
                page_number=1,
                bounds=boldsign.Rectangle(x=100, y=100, width=100, height=50)
            )

            signer = boldsign.DocumentSigner(
                name="Signer",
                email_address="mohammedmushraf.abuthakir+6@syncfusion.com",
                formFields=[signature_field]
            )

            send_for_sign = boldsign.SendForSign(
                title="",
                files=files,
                signers=[signer]
            )

            document = self.document_api.send_document(send_for_sign)
            pytest.fail(f"Expected exception for missing document title, but got: {document}")

        except ApiException as e:
            assert e.status == 400
            print(f"Received expected API exception: {e}")

        except Exception as e:
            print(f"\nUnexpected exception occurred: {e}")
            assert False, f"Unexpected exception occurred: {e}"

        finally:
            time.sleep(5)

    @pytest.mark.run(order=58)
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
        finally:
            time.sleep(5)
    
    @pytest.mark.run(order=59)
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
            assert revoke_response is not None
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"documentId\":[\"Provide valid document id.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=60)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=61)
    def test_delete_document_negative(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            # Use the created document ID from previous tests
            document_id = "WrongDocumentId"

            delete_response = self.document_api.delete_document(document_id=document_id)
            assert delete_response is not None

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"documentId\":[\"Provide valid document id.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"         
        finally:
            time.sleep(5)

    @pytest.mark.run(order=62)
    def test_document_list_positive_with_date_filter_type(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            # Parameters
            page = 1
            page_size = 10
            start_date = datetime.now() - timedelta(days=30)
            end_date = datetime.now()
            date_filter_type = "SentBetween"
            documents = self.document_api.list_documents(
                page=page,
                page_size=page_size,
                start_date=start_date,
                end_date=end_date,
                date_filter_type=date_filter_type
            )
            assert documents is not None
            assert len(documents.result) >= 0
        except ApiException as e:
            print("\nAPI Exception occurred:", e)
            assert False, f"API exception occurred: {str(e)}"
        except Exception as e:
            print("\nUnexpected exception occurred:", e)
            assert False, f"Unexpected exception: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=63)
    def test_document_list_negative_empty_date_filter_type(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            self.document_api.list_documents(
                page=1,
                page_size=10,
                start_date=datetime.now() - timedelta(days=30),
                end_date=datetime.now(),
                date_filter_type=""
            )
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"         
        finally:
            time.sleep(5)

    @pytest.mark.run(order=64)
    def test_document_list_negative_past_months(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)
            self.document_api.list_documents(
                page=1,
                page_size=10,
                start_date=datetime.now(),
                end_date=datetime.now() - timedelta(days=30),
                date_filter_type="SentBetween"
            )
            
        except ApiException as e:
            print("\nExpected ApiException occurred:", e)
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nUnexpected exception occurred:", e)
            assert False, f"Unexpected exception: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=65)
    def test_send_document_with_scheduled_time(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            scheduled_time = datetime.utcnow() + timedelta(days=1)
            scheduled_time_unix = int((scheduled_time - datetime(1970, 1, 1)).total_seconds())

            sendDocumentRequest = boldsign.SendForSign(
                title="Scheduled Document SDK API",
                document_title="SDK Scheduled Document Test Case - Single Signer",
                description="Testing scheduled send with only one signer",
                files=["tests/documents/input/doc_1.pdf"],
                enablePrintAndSign=True,
                hideDocumentId=True,
                enableReassign=False,

                scheduled_send_time=scheduled_time_unix,

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
                        privateMessage="This is a private message for the signer",
                        recipientNotificationSettings={
                            "signatureRequest": True,
                            "declined": True,
                            "revoked": True,
                            "signed": True,
                            "completed": True,
                            "expired": True,
                            "reassigned": True,
                            "deleted": True,
                            "reminders": True,
                            "editRecipient": True
                        }
                    )
                ],
            )

            sendDocument = self.document_api.send_document(sendDocumentRequest)
            assert sendDocument is not None

        except ApiException as e:
            print(f"\nException when calling BoldSign API: {e}")
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print(f"\nException when calling BoldSign: {e}")
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=66)
    def test_send_document_with_scheduled_time_negative_invalid_email(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            past_time = datetime.utcnow() - timedelta(days=1)
            past_time_unix = int((past_time - datetime(1970, 1, 1)).total_seconds())

            sendDocumentRequest = boldsign.SendForSign(
                title="Invalid Scheduled Document",
                document_title="Negative Test - Past Scheduled Time",
                description="Negative test: scheduled time is in the past",
                files=["tests/documents/input/doc_1.pdf"],
                enablePrintAndSign=True,
                hideDocumentId=True,
                enableReassign=False,

                scheduled_send_time=past_time_unix,

                signers=[
                    boldsign.DocumentSigner(
                        name="Test Signer",
                        emailAddress="invalid-email",
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
                        privateMessage="This is a test for invalid scheduled time"
                    )
                ],
            )

            self.document_api.send_document(sendDocumentRequest)
            assert False, "Expected ApiException due to invalid scheduled time was not raised"

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"         
        finally:
            time.sleep(5)

    @pytest.mark.run(order=67)
    def test_send_document_with_file_bytes(self):
        try:
            self.document_api = boldsign.DocumentApi(self.api_client)

            file_path = "tests/documents/input/doc_1.pdf"
            self.assertTrue(os.path.exists(file_path), f"File does not exist at: {file_path}")

            with open(file_path, "rb") as f:
                file_bytes = f.read()

            form_fields = [
                FormField(
                    id="Signature",
                    name="Signature",
                    fieldType="Signature",
                    pageNumber=1,
                    font="Helvetica",
                    bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150),
                    isRequired=True
                ),
                FormField(
                    id="Label",
                    name="Label",
                    fieldType="Label",
                    value="Label Field",
                    font="Helvetica",
                    pageNumber=1,
                    bounds=boldsign.Rectangle(x=150, y=250, width=200, height=25),
                    isRequired=True
                ),
            ]

            signer = DocumentSigner(
                name="David",
                emailAddress="david@cubeflakes.com",
                signerOrder=1,
                signerType="Signer",
                formFields=form_fields,
                locale="EN"
            )

            send_request = SendForSign(
                document_title="SDK Document Test case",
                description="Testing document from SDK integration test case",
                files=[file_bytes],
                disableExpiryAlert=False,
                reminderSettings=ReminderSettings(reminderDays=3, reminderCount=5, enableAutoReminder=False),
                enableReassign=True,
                message="Please sign this.",
                signers=[signer],
                expiryDays=10,
                enablePrintAndSign=False,
                AutoDetectFields=False,
                onBehalfOf="",
                enableSigningOrder=False,
                useTextTags=False,
                title="Document SDK API",
                hideDocumentId=False,
                enableEmbeddedSigning=False,
                expiryDateType="Days",
                expiryDate=60,
                disableEmails=False,
                disableSMS=False,
            )

            response = self.document_api.send_document(send_request)
            self.assertIsNotNone(response.document_id, "Document ID should not be None")
            print(f"Document sent successfully. ID: {response.document_id}")

        except boldsign.ApiException as e:
            self.fail(f"API exception occurred: {e}")
        except Exception as ex:
            self.fail(f"Unexpected exception: {ex}")
        finally:
            time.sleep(5)

if __name__ == '__main__':
    unittest.main()