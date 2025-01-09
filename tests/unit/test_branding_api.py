import unittest
from unittest.mock import patch, MagicMock

import pytest
import boldsign
from boldsign.rest import ApiException

class TestBrandingApi(unittest.TestCase):

    @patch('boldsign.BrandingApi')
    @pytest.mark.unit
    def testBrandingList(self, mock_branding_api):
        mock_branding_api_instance = mock_branding_api.return_value
        mock_branding_api_instance.brand_list.return_value = MagicMock(result=[MagicMock()])

        brandings = mock_branding_api_instance.brand_list()

        self.assertIsNotNone(brandings)
        self.assertGreater(len(brandings.result), 0)
        mock_branding_api_instance.brand_list.assert_called_once()

    @patch('boldsign.BrandingApi')
    @pytest.mark.unit
    def testCreateBrand(self, mock_branding_api):
        mock_branding_api_instance = mock_branding_api.return_value
        mock_brand_created = MagicMock(brand_id="brand123")
        mock_branding_api_instance.create_brand.return_value = mock_brand_created

        brand_data = {
            "brand_name": "New Brand",
            "brand_logo": b"mock_logo_data",
            "background_color": "#FFFFFF",
            "button_color": "#000000",
            "button_text_color": "#FFFFFF",
            "email_display_name": "Brand Email",
            "disclaimer_description": "Disclaimer",
            "disclaimer_title": "Disclaimer Title",
            "redirect_url": "https://example.com",
            "is_default": True,
            "can_hide_tag_line": False,
            "combine_audit_trail": True,
            "exclude_audit_trail_from_email": False,
            "document_time_zone": "UTC",
            "completed_email_type": "email_type",
            "email_signed_document": "email_signed_doc",
            "show_built_in_form_fields": True,
            "allow_custom_field_creation": True,
            "show_shared_custom_fields": True,
            "hide_decline": False,
            "hide_save": False
        }

        created_brand = mock_branding_api_instance.create_brand(**brand_data)

        self.assertIsNotNone(created_brand)
        self.assertEqual(created_brand.brand_id, "brand123")
        mock_branding_api_instance.create_brand.assert_called_once_with(**brand_data)

    @patch('boldsign.BrandingApi')
    @pytest.mark.unit
    def testEditBrand(self, mock_branding_api):
        mock_branding_api_instance = mock_branding_api.return_value
        mock_brand_response = MagicMock(
            brand_id="brand123",
            brand_name="Updated Brand",
            brand_logo="updated_logo.png",
            background_color="#FFFFFF",
            button_color="#000000",
            button_text_color="#FFFFFF",
            email_display_name="Updated Brand Email",
            disclaimer_title="Updated Disclaimer Title",
            disclaimer_description="Updated Disclaimer",
            redirect_url="https://example.com/updated",
            is_default=False,
            can_hide_tag_line=True,
            combine_audit_trail=False,
            exclude_audit_trail_from_email=True
        )
        mock_branding_api_instance.edit_brand.return_value = mock_brand_response

        brand_id = "brand123"
        brand_data = {
            "brand_name": "Updated Brand",
            "brand_logo": b"updated_logo_data",
            "background_color": "#FFFFFF",
            "button_color": "#000000",
            "button_text_color": "#FFFFFF",
            "email_display_name": "Updated Brand Email",
            "disclaimer_description": "Updated Disclaimer",
            "disclaimer_title": "Updated Disclaimer Title",
            "redirect_url": "https://example.com/updated",
            "is_default": False,
            "can_hide_tag_line": True,
            "combine_audit_trail": False,
            "exclude_audit_trail_from_email": True
        }

        edited_brand = mock_branding_api_instance.edit_brand(brand_id, **brand_data)

        self.assertIsNotNone(edited_brand)
        self.assertEqual(edited_brand.brand_id, "brand123")
        self.assertEqual(edited_brand.brand_name, "Updated Brand")
        self.assertEqual(edited_brand.brand_logo, "updated_logo.png")
        self.assertEqual(edited_brand.background_color, "#FFFFFF")
        self.assertEqual(edited_brand.button_color, "#000000")
        self.assertEqual(edited_brand.button_text_color, "#FFFFFF")
        self.assertEqual(edited_brand.email_display_name, "Updated Brand Email")
        self.assertEqual(edited_brand.disclaimer_title, "Updated Disclaimer Title")
        self.assertEqual(edited_brand.disclaimer_description, "Updated Disclaimer")
        self.assertEqual(edited_brand.redirect_url, "https://example.com/updated")
        self.assertFalse(edited_brand.is_default)
        self.assertTrue(edited_brand.can_hide_tag_line)
        self.assertFalse(edited_brand.combine_audit_trail)
        self.assertTrue(edited_brand.exclude_audit_trail_from_email)
        mock_branding_api_instance.edit_brand.assert_called_once_with(brand_id, **brand_data)

    @patch('boldsign.BrandingApi')
    @pytest.mark.unit
    def testDeleteBrand(self, mock_branding_api):
        mock_branding_api_instance = mock_branding_api.return_value
        mock_response = MagicMock()
        mock_response.message = "Brand deleted successfully"
        mock_branding_api_instance.delete_brand.return_value = mock_response

        brand_id = "brand123"
        response = mock_branding_api_instance.delete_brand(brand_id)

        self.assertIsNotNone(response)
        self.assertEqual(response.message, "Brand deleted successfully")
        mock_branding_api_instance.delete_brand.assert_called_once_with(brand_id)

    @patch('boldsign.BrandingApi')
    @pytest.mark.unit
    def testResetDefaultBrand(self, mock_branding_api):
        mock_branding_api_instance = mock_branding_api.return_value
        mock_response = MagicMock()
        mock_response.message = "Default brand reset successfully"
        mock_response.brand_id = "brand123"
        mock_branding_api_instance.reset_default_brand.return_value = mock_response

        brand_id = "brand123"
        response = mock_branding_api_instance.reset_default_brand(brand_id)

        self.assertIsNotNone(response)
        self.assertEqual(response.message, "Default brand reset successfully")
        self.assertEqual(response.brand_id, "brand123")
        mock_branding_api_instance.reset_default_brand.assert_called_once_with(brand_id)

if __name__ == '__main__':
    unittest.main()