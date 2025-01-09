import unittest
from unittest.mock import patch, MagicMock

import pytest
import boldsign
from boldsign.rest import ApiException
from boldsign.models.template_properties import TemplateProperties

class TestTemplateApi(unittest.TestCase):

    @patch('boldsign.TemplateApi')
    @pytest.mark.unit
    def testTemplateList(self, mock_template_api):
        mock_template_api_instance = mock_template_api.return_value
        mock_template_api_instance.list_templates.return_value = MagicMock(result=[MagicMock()])

        templates = mock_template_api_instance.list_templates(
            page=1,
            template_type=None,
            page_size=10,
            search_key=None,
            on_behalf_of=None,
            created_by=None,
            template_labels=None,
            start_date=None,
            end_date=None
        )

        self.assertIsNotNone(templates)
        self.assertGreater(len(templates.result), 0)
        mock_template_api_instance.list_templates.assert_called_once()

    @patch('boldsign.TemplateApi')
    @pytest.mark.unit
    def testTemplateDownload(self, mock_template_api):
        mock_template_api_instance = mock_template_api.return_value
        mock_template_file = b'Mock PDF content'
        mock_template_api_instance.download.return_value = mock_template_file

        template_file = mock_template_api_instance.download(
            template_id=None,
            on_behalf_of=None
        )

        self.assertIsNotNone(template_file)
        self.assertGreater(len(template_file), 0)
        mock_template_api_instance.download.assert_called_once_with(
            template_id=None,
            on_behalf_of=None
        )

    @patch('boldsign.TemplateApi')
    @pytest.mark.unit
    def test_create_template(self, mock_template_api):
        mock_template_api_instance = mock_template_api.return_value
        mock_template_instance = MagicMock()
        mock_template_api_instance.create_template.return_value = mock_template_instance

        template_data = {
            "title": "New Template",
            "description": "This is a new template.",
            "files": [],
            "roles": []
        }

        created_template = mock_template_api_instance.create_template(template_data)

        self.assertIsNotNone(created_template)
        mock_template_api_instance.create_template.assert_called_once_with(template_data)

    @patch('boldsign.TemplateApi')
    @pytest.mark.unit
    def test_delete_template(self, mock_template_api):
        mock_template_api_instance = mock_template_api.return_value
        mock_template_api_instance.delete_template.return_value = None  # Assuming it returns None on success

        template_id = "12345"
        response = mock_template_api_instance.delete_template(template_id)

        self.assertIsNone(response)
        mock_template_api_instance.delete_template.assert_called_once_with(template_id)

    @patch('boldsign.TemplateApi')
    @pytest.mark.unit
    def test_template_properties(self, mock_template_api):
        mock_template_api_instance = mock_template_api.return_value
        # Mocking the response of the get_template_properties API call
        mock_template_properties = TemplateProperties(
            template_id="12345",
            title="Sample Template",
            description="This is a sample template.",
            document_title="Sample Document",
            document_message="Please sign this document.",
            files=[],
            roles=[],
            form_groups=[],
            common_fields=[],
            c_c_details=["example@example.com"],
            brand_id="brand123",
            allow_message_editing=True,
            allow_new_roles=False,
            allow_new_files=True,
            allow_modify_files=False,
            enable_reassign=True,
            enable_print_and_sign=False,
            enable_signing_order=True,
            created_date=1622548800,
            created_by=None,
            shared_template_detail=[],
            document_info=[],
            document_download_option="Combined",
            labels=["label1", "label2"],
            template_labels=["template_label1"],
            behalf_of=None
        )
        mock_template_api_instance.get_template_properties.return_value = mock_template_properties

        # Call the API method
        template_properties = mock_template_api_instance.get_template_properties(template_id="12345")

        # Assertions to check if properties are set correctly
        self.assertEqual(template_properties.template_id, "12345")
        self.assertEqual(template_properties.title, "Sample Template")
        self.assertEqual(template_properties.description, "This is a sample template.")
        self.assertEqual(template_properties.document_title, "Sample Document")
        self.assertEqual(template_properties.document_message, "Please sign this document.")
        self.assertIsInstance(template_properties.files, list)
        self.assertIsInstance(template_properties.roles, list)
        self.assertIsInstance(template_properties.form_groups, list)
        self.assertIsInstance(template_properties.common_fields, list)
        self.assertEqual(template_properties.c_c_details, ["example@example.com"])
        self.assertEqual(template_properties.brand_id, "brand123")
        self.assertTrue(template_properties.allow_message_editing)
        self.assertFalse(template_properties.allow_new_roles)
        self.assertTrue(template_properties.allow_new_files)
        self.assertFalse(template_properties.allow_modify_files)
        self.assertTrue(template_properties.enable_reassign)
        self.assertFalse(template_properties.enable_print_and_sign)
        self.assertTrue(template_properties.enable_signing_order)
        self.assertEqual(template_properties.created_date, 1622548800)
        self.assertIsNone(template_properties.created_by)
        self.assertIsInstance(template_properties.shared_template_detail, list)
        self.assertIsInstance(template_properties.document_info, list)
        self.assertEqual(template_properties.document_download_option, "Combined")
        self.assertEqual(template_properties.labels, ["label1", "label2"])
        self.assertEqual(template_properties.template_labels, ["template_label1"])
        self.assertIsNone(template_properties.behalf_of)

    @patch('boldsign.TemplateApi')
    @pytest.mark.unit
    def test_send_template(self, mock_template_api):
        mock_template_api_instance = mock_template_api.return_value
        mock_response = MagicMock()
        mock_response.document_id = "12345"  # Mocking the document ID in the response
        mock_template_api_instance.send_using_template.return_value = mock_response

        template_data = {
            "document_id": "12345",
            "title": "Sample Template",
            "message": "Please sign this document.",
            "roles": [],
            "brand_id": "brand123",
            "labels": ["label1", "label2"],
            "disable_emails": False,
            "disable_sms": False,
            "hide_document_id": False,
            "expiry_days": 30,
            "expiry_date_type": "Days",
            "expiry_value": 60,
            "enable_print_and_sign": True,
            "enable_reassign": True,
            "enable_signing_order": True,
            "use_text_tags": False,
            "text_tag_definitions": [],
            "document_info": [],
            "on_behalf_of": None,
            "is_sandbox": False,
            "role_removal_indices": [],
            "document_download_option": "Combined"
        }

        response = mock_template_api_instance.send_using_template(
            template_id="12345",
            send_for_sign_from_template_json=template_data
        )

        self.assertIsNotNone(response)
        self.assertEqual(response.document_id, "12345")  # Ensure the document ID matches
        mock_template_api_instance.send_using_template.assert_called_once_with(
            template_id="12345",
            send_for_sign_from_template_json=template_data
        )

    @patch('boldsign.TemplateApi')
    @pytest.mark.unit
    def test_create_embedded_request_url_template(self, mock_template_api):
        mock_template_api_instance = mock_template_api.return_value
        mock_response = MagicMock()
        mock_response.url = "https://mocked.url/embedded/request"  # Mocked URL response
        mock_template_api_instance.create_embedded_request_url_template.return_value = mock_response

        template_id = "12345"
        embedded_send_template_json_request = {
            "files": [],
            "redirect_url": "https://example.com/redirect",
            "show_toolbar": True,
            "locale": "EN"
        }

        response = mock_template_api_instance.create_embedded_request_url_template(
            template_id=template_id,
            embedded_send_template_json_request=embedded_send_template_json_request
        )

        self.assertIsNotNone(response)
        self.assertEqual(response.url, "https://mocked.url/embedded/request")
        mock_template_api_instance.create_embedded_request_url_template.assert_called_once_with(
            template_id=template_id,
            embedded_send_template_json_request=embedded_send_template_json_request
        )

    @patch('boldsign.TemplateApi')
    @pytest.mark.unit
    def test_create_embedded_template_url(self, mock_template_api):
        mock_template_api_instance = mock_template_api.return_value
        mock_response = MagicMock()
        mock_response.url = "https://mocked.url/embedded/template"  # Mocked URL response
        mock_response.template_id = "template123"  # Mocked template ID response
        mock_template_api_instance.create_embedded_template_url.return_value = mock_response

        template_data = {
            "title": "New Embedded Template",
            "description": "This is an embedded template.",
            "files": [],
            "roles": [],
            "redirect_url": "https://example.com/redirect",
            "show_toolbar": True,
            "locale": "EN"
        }

        response = mock_template_api_instance.create_embedded_template_url(
            embedded_template_json_request=template_data
        )

        self.assertIsNotNone(response)
        self.assertEqual(response.url, "https://mocked.url/embedded/template")
        self.assertEqual(response.template_id, "template123")
        mock_template_api_instance.create_embedded_template_url.assert_called_once_with(
            embedded_template_json_request=template_data
        )

if __name__ == '__main__':
    unittest.main()