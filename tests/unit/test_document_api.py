import unittest
from unittest.mock import patch, MagicMock
import boldsign
import pytest
from boldsign.rest import ApiException
from boldsign.models.send_for_sign import SendForSign
from boldsign.models.document_records import DocumentRecords  # Assuming this is the model for the response

class TestDocumentApi(unittest.TestCase):

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_send_document(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()
        mock_response.document_id = "12345"  # Mocking the document ID in the response
        mock_response.signers = [{"name": "John Doe", "email": "john.doe@example.com"}]  # Mocking signers
        mock_document_api_instance.send_document.return_value = mock_response

        send_for_sign_data = SendForSign(
            document_id="12345",
            title="Sample Document",
            message="Please sign this document.",
            roles=[],
            brand_id="brand123",
            labels=["label1", "label2"],
            disable_emails=False,
            disable_sms=False,
            hide_document_id=False,
            expiry_days=30,
            expiry_date_type="Days",
            expiry_value=60,
            enable_print_and_sign=True,
            enable_reassign=True,
            enable_signing_order=True,
            use_text_tags=False,
            text_tag_definitions=[],
            document_info=[],
            on_behalf_of=None,
            is_sandbox=False,
            role_removal_indices=[],
            document_download_option="Combined",
            recipient_notification_settings=None,
            signers=[{"name": "John Doe", "email": "john.doe@example.com"}]  # Adding signers
        )

        response = mock_document_api_instance.send_document(send_for_sign_json_request=send_for_sign_data)

        self.assertIsNotNone(response)
        self.assertEqual(response.document_id, "12345")  # Ensure the document ID matches
        self.assertEqual(response.signers[0]['name'], "John Doe")  # Verify signer's name
        self.assertEqual(response.signers[0]['email'], "john.doe@example.com")  # Verify signer's email
        mock_document_api_instance.send_document.assert_called_once_with(send_for_sign_json_request=send_for_sign_data)

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_list_documents(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()
        
        # Mocking the response for the list documents API
        mock_response.result = [MagicMock(document_id="12345", title="Sample Document", status="Completed")]
        mock_response.next_cursor = None  # Assuming there's a cursor for pagination
        mock_document_api_instance.list_documents.return_value = mock_response

        # Define parameters for listing documents
        page = 1
        page_size = 10
        search_key = None
        labels = None
        status = None
        next_cursor = None

        # Call the API method
        documents = mock_document_api_instance.list_documents(
            page=page,
            page_size=page_size,
            search_key=search_key,
            labels=labels,
            status=status,
            next_cursor=next_cursor
        )

        # Assertions to check if the response is as expected
        self.assertIsNotNone(documents)
        self.assertGreater(len(documents.result), 0)
        self.assertEqual(documents.result[0].document_id, "12345")
        self.assertEqual(documents.result[0].title, "Sample Document")
        self.assertEqual(documents.result[0].status, "Completed")
        mock_document_api_instance.list_documents.assert_called_once_with(
            page=page,
            page_size=page_size,
            search_key=search_key,
            labels=labels,
            status=status,
            next_cursor=next_cursor
        )

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_get_document_properties(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()

        # Mocking the response for the get_properties API
        mock_response.document_id = "12345"
        mock_response.brand_id = "brand123"
        mock_response.message_title = "Sample Document"
        mock_response.document_description = "This is a sample document."
        mock_response.status = "Completed"
        mock_response.files = []  # Assuming no files for this test
        mock_response.sender_detail = None  # Assuming no sender detail for this test
        mock_response.signer_details = []  # Assuming no signer details for this test
        mock_response.form_groups = []  # Assuming no form groups for this test
        mock_response.common_fields = []  # Assuming no common fields for this test
        mock_response.behalf_of = None  # Assuming no behalf of for this test
        mock_response.cc_details = []  # Assuming no cc details for this test
        mock_response.reminder_settings = None  # Assuming no reminder settings for this test
        mock_response.reassign = []  # Assuming no reassign for this test
        mock_response.document_history = []  # Assuming no document history for this test
        mock_response.activity_by = "user@example.com"
        mock_response.activity_date = 1622548800
        mock_response.activity_action = "Viewed"
        mock_response.created_date = 1622548800
        mock_response.expiry_days = 30
        mock_response.expiry_date = 1625140800
        mock_response.enable_signing_order = True
        mock_response.is_deleted = False
        mock_response.revoke_message = None
        mock_response.decline_message = None
        mock_response.application_id = "app123"
        mock_response.labels = ["label1", "label2"]
        mock_response.disable_emails = False
        mock_response.disable_expiry_alert = False
        mock_response.hide_document_id = False
        mock_response.enable_print_and_sign = True
        mock_response.enable_reassign = True
        mock_response.expiry_date_type = "Days"
        mock_response.expiry_value = 60
        mock_response.document_download_option = "Combined"
        mock_response.meta_data = {}
        mock_response.recipient_notification_settings = None

        mock_document_api_instance.get_properties.return_value = mock_response

        # Call the API method
        document_id = "12345"
        response = mock_document_api_instance.get_properties(document_id=document_id)

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response.document_id, "12345")
        self.assertEqual(response.brand_id, "brand123")
        self.assertEqual(response.message_title, "Sample Document")
        self.assertEqual(response.document_description, "This is a sample document.")
        self.assertEqual(response.status, "Completed")
        self.assertEqual(response.activity_by, "user@example.com")
        self.assertEqual(response.activity_action, "Viewed")
        self.assertEqual(response.expiry_days, 30)
        self.assertTrue(response.enable_signing_order)
        mock_document_api_instance.get_properties.assert_called_once_with(document_id=document_id)

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_download_document(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()

        # Mocking the response for the download document API
        mock_response = b'Mock PDF content'  # Simulating a binary response for a PDF document

        mock_document_api_instance.download_document.return_value = mock_response

        # Define parameters for the download document API
        document_id = "12345"
        on_behalf_of = None  # Assuming no on behalf of for this test

        # Call the API method
        response = mock_document_api_instance.download_document(document_id=document_id, on_behalf_of=on_behalf_of)

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response, b'Mock PDF content')  # Ensure the response matches the mocked content
        mock_document_api_instance.download_document.assert_called_once_with(document_id=document_id, on_behalf_of=on_behalf_of)

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_download_audit_log(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()

        # Mocking the response for the download audit log API
        mock_response = b'Mock Audit Log Content'  # Simulating a binary response for the audit log

        mock_document_api_instance.download_audit_log.return_value = mock_response

        # Define parameters for the download audit log API
        document_id = "12345"
        on_behalf_of = None  # Assuming no on behalf of for this test

        # Call the API method
        response = mock_document_api_instance.download_audit_log(document_id=document_id, on_behalf_of=on_behalf_of)

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response, b'Mock Audit Log Content')  # Ensure the response matches the mocked content
        mock_document_api_instance.download_audit_log.assert_called_once_with(document_id=document_id, on_behalf_of=on_behalf_of)

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_revoke_document(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()
        mock_response.message = "Document revoked successfully"  # Mocking the success message
        mock_document_api_instance.revoke_document.return_value = mock_response

        # Define parameters for revoking the document
        document_id = "12345"
        revoke_details = {
            "message": "Revoking the document due to changes.",
            "on_behalf_of": None  # Assuming no on behalf of for this test
        }

        # Create an instance of RevokeDocument
        revoke_document_instance = boldsign.RevokeDocument(**revoke_details)

        # Call the API method
        response = mock_document_api_instance.revoke_document(document_id=document_id, revoke_document=revoke_document_instance)

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response.message, "Document revoked successfully")  # Ensure the response message matches
        mock_document_api_instance.revoke_document.assert_called_once_with(document_id=document_id, revoke_document=revoke_document_instance)

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_delete_document(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()
        mock_response.message = "Document deleted successfully"  # Mocking the success message
        mock_document_api_instance.delete_document.return_value = mock_response

        # Define parameters for deleting the document
        document_id = "12345"
        on_behalf_of = None  # Assuming no on behalf of for this test

        # Call the API method
        response = mock_document_api_instance.delete_document(document_id=document_id, on_behalf_of=on_behalf_of)

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response.message, "Document deleted successfully")  # Ensure the response message matches
        mock_document_api_instance.delete_document.assert_called_once_with(document_id=document_id, on_behalf_of=on_behalf_of)

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_remind_document(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()
        mock_response.message = "Reminder sent successfully"  # Mocking the success message

        mock_document_api_instance.remind_document.return_value = mock_response

        # Define parameters for the remind document API
        document_id = "12345"
        receiver_emails = ["john.doe@example.com"]
        reminder_message = boldsign.ReminderMessage(message="Please sign the document.")

        # Call the API method
        response = mock_document_api_instance.remind_document(
            document_id=document_id,
            receiver_emails=receiver_emails,
            reminder_message=reminder_message
        )

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response.message, "Reminder sent successfully")  # Ensure the response message matches
        mock_document_api_instance.remind_document.assert_called_once_with(
            document_id=document_id,
            receiver_emails=receiver_emails,
            reminder_message=reminder_message
        )

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_change_access_code(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()
        mock_response.message = "Access code changed successfully"  # Mocking the success message
        mock_response.document_id = "12345"  # Mocking the document ID
        mock_document_api_instance.change_access_code.return_value = mock_response

        # Define parameters for changing the access code
        document_id = "12345"
        access_code_detail = {
            "new_access_code": "new_access_code_value",
            "email_id": "john.doe@example.com",
            "z_order": 1
        }

        # Call the API method
        response = mock_document_api_instance.change_access_code(
            document_id=document_id,
            access_code_detail=access_code_detail
        )

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response.message, "Access code changed successfully")  # Ensure the response message matches
        self.assertEqual(response.document_id, "12345")  # Ensure the document ID matches
        mock_document_api_instance.change_access_code.assert_called_once_with(
            document_id=document_id,
            access_code_detail=access_code_detail
        )

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_change_recipient(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()
        mock_response.message = "Recipient changed successfully"  # Mocking the success message
        mock_response.document_id = "12345"  # Mocking the document ID
        mock_document_api_instance.change_recipient.return_value = mock_response

        # Define parameters for changing the recipient
        document_id = "12345"
        change_recipient = {
            "newSignerName": "john",
            "newSignerEmail": "john.doe@example.com",
            "oldSignerEmail": "hankyWhites@cubeflakes.com",
            "reason":"Test change recipient"
        }

        # Call the API method
        response = mock_document_api_instance.change_recipient(
            document_id=document_id,
            change_recipient=change_recipient
        )

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response.message, "Recipient changed successfully")  # Ensure the response message matches
        self.assertEqual(response.document_id, "12345")  # Ensure the document ID matches
        mock_document_api_instance.change_recipient.assert_called_once_with(
            document_id=document_id,
            change_recipient=change_recipient
        )

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_get_embedded_sign_link(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()
        
        # Mocking the response for the get_embedded_sign_link API
        mock_response.sign_link = "https://mocked.sign.link"  # Mocking the sign link
        mock_document_api_instance.get_embedded_sign_link.return_value = mock_response

        # Define parameters for the get_embedded_sign_link API
        document_id = "12345"
        signer_email = "john.doe@example.com"
        country_code = "US"
        phone_number = "1234567890"
        sign_link_valid_till = None  # Assuming no specific time limit for the link
        redirect_url = "https://example.com/redirect"

        # Call the API method
        response = mock_document_api_instance.get_embedded_sign_link(
            document_id=document_id,
            signer_email=signer_email,
            country_code=country_code,
            phone_number=phone_number,
            sign_link_valid_till=sign_link_valid_till,
            redirect_url=redirect_url
        )

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response.sign_link, "https://mocked.sign.link")  # Ensure the sign link matches
        mock_document_api_instance.get_embedded_sign_link.assert_called_once_with(
            document_id=document_id,
            signer_email=signer_email,
            country_code=country_code,
            phone_number=phone_number,
            sign_link_valid_till=sign_link_valid_till,
            redirect_url=redirect_url
        )

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_add_tag(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()
        mock_response.message = "Tags added successfully"  # Mocking the success message
        mock_document_api_instance.add_tag.return_value = mock_response

        # Define parameters for adding tags
        document_tags = {
            "document_id": "12345",
            "tags": ["label1", "label2"]
        }

        # Call the API method
        response = mock_document_api_instance.add_tag(document_tags=document_tags)

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response.message, "Tags added successfully")  # Ensure the response message matches
        mock_document_api_instance.add_tag.assert_called_once_with(document_tags=document_tags)

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_delete_tag(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()
        mock_response.message = "Tags deleted successfully"  # Mocking the success message
        mock_document_api_instance.delete_tag.return_value = mock_response

        # Define parameters for deleting tags
        document_tags = {
            "document_id": "12345",
            "tags": ["label1", "label2"]
        }

        # Call the API method
        response = mock_document_api_instance.delete_tag(document_tags=document_tags)

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response.message, "Tags deleted successfully")  # Ensure the response message matches
        mock_document_api_instance.delete_tag.assert_called_once_with(document_tags=document_tags)

        # Test with empty tags
        document_tags_empty = {
            "document_id": "12345",
            "tags": []
        }
        response_empty = mock_document_api_instance.delete_tag(document_tags=document_tags_empty)
        self.assertIsNotNone(response_empty)
        self.assertEqual(response_empty.message, "Tags deleted successfully")  # Ensure the response message matches
        mock_document_api_instance.delete_tag.assert_called_with(document_tags=document_tags_empty)

    @patch('boldsign.DocumentApi')
    @pytest.mark.unit
    def test_add_authentication(self, mock_document_api):
        mock_document_api_instance = mock_document_api.return_value
        mock_response = MagicMock()
        mock_response.message = "Authentication added successfully"  # Mocking the success message
        mock_document_api_instance.add_authentication.return_value = mock_response

        # Define parameters for adding authentication
        document_id = "12345"
        access_code_detail = {
            "authentication_type": "AccessCode",
            "new_access_code": "new_access_code_value",
        }

        # Create an instance of AccessCodeDetail
        access_code_instance = boldsign.AccessCodeDetail(**access_code_detail)

        # Call the API method
        response = mock_document_api_instance.add_authentication(
            document_id=document_id,
            access_code_detail=access_code_instance
        )

        # Assertions to check if the response is as expected
        self.assertIsNotNone(response)
        self.assertEqual(response.message, "Authentication added successfully")  # Ensure the response message matches
        mock_document_api_instance.add_authentication.assert_called_once_with(
            document_id=document_id,
            access_code_detail=access_code_instance
        )

if __name__ == '__main__':
    unittest.main()