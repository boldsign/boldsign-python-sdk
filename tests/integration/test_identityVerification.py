import time
import unittest
from boldsign.models.embedded_file_details import EmbeddedFileDetails
import pytest
import boldsign
import base64
from boldsign.api_client import ApiClient
from boldsign.exceptions import ApiException
from config import API_KEY, BASE_URL


class TestIdentityVerificationApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.created_document_id = None

    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=API_KEY, host=BASE_URL)
        self.api_client = boldsign.ApiClient(self.configuration)
        self.identity_verification_api = boldsign.IdentityVerificationApi(self.api_client)

    def pdf_to_base64(self, pdf_file_path):
        pdf_file_path = "tests/documents/input/" + pdf_file_path
        with open(pdf_file_path, "rb") as png_file:
            pdf_content = png_file.read()
            base64_content = "data:application/pdf;base64," + base64.b64encode(pdf_content).decode('utf-8')
        return base64_content

    @pytest.mark.run(order=160)
    def test_send_document(self):
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
                authenticationType="IdVerification",
                formFields=form_fields
            )

            identity_verification_settings = boldsign.IdentityVerificationSettings(
                type='EveryAccess',
                maximumRetryCount=1
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
            TestIdentityVerificationApi.created_document_id = send_document_response.document_id

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
            time.sleep(60)

    @pytest.mark.run(order=161)
    def test_create_embedded_verification_url_negative(self):
        try:
            create_embedded_verification_url = EmbeddedFileDetails(
                emailId="girisankar.syncfusion@gmail.com",
                countryCode="+91",
                phoneNumber="87654345678",
                redirectUrl="https://www.boldsign.com",
                order=1
            )

            self.identity_verification_api.create_embedded_verification_url(TestIdentityVerificationApi.created_document_id, create_embedded_verification_url)

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=162)
    def test_get_identity_verification_report_negative(self):
        try:
            identity_verification_report = boldsign.VerificationDataRequest(
                emailId="girisankar.syncfusion@gmail.com",
                countryCode="+91",
                phoneNumber="87654345678",
                order=1
            )

            self.identity_verification_api.report(TestIdentityVerificationApi.created_document_id, identity_verification_report)

        except ApiException as e:
            assert e.status == 403
            assert e.reason == "Forbidden"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)


    @pytest.mark.run(order=163)
    def test_get_identity_verification_image_negative(self):
        try:
            identity_verification_image = boldsign.DownloadImageRequest(
                emailId="girisankar.syncfusion@gmail.com",
                countryCode="+91",
                phoneNumber="87654345678",
                fileId="invalid-file-id",
                order=1
            )

            image_response = self.identity_verification_api.image(
                self.created_document_id, identity_verification_image
            )

            self.assertIsNotNone(image_response)
            print("Identity verification image retrieved successfully.")
    
        except ApiException as e:
            assert e.status == 403
            assert e.reason == "Forbidden"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

if __name__ == '__main__':
    unittest.main()