import datetime
import unittest
import logging
import pytest
import boldsign
from boldsign.rest import ApiException
from random import randint
import time
from config import API_KEY, BASE_URL

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.mark.integration
class TestCustomFieldsApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.created_custom_field_id = None
        cls.Custom_field_name = None
        cls.created_brand_id = None

    def random_numbers(self):
        range_start = 10**(3-1)
        range_end = (10**3)-1
        return str(randint(range_start, range_end))

    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=API_KEY, host=BASE_URL)
        self.api_client = boldsign.ApiClient(self.configuration)
        self.custom_field_api = boldsign.CustomFieldApi(self.api_client)
        srting_value = self.random_numbers()
        TestCustomFieldsApi.Custom_field_name = "Test Custom Field"+srting_value
        
    @pytest.mark.run(order=146)
    def test_create_brand(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters for create brand
            brand_name = 'TestBrandAPI'
            brand_logo = 'tests/documents/input/logo.png'
            background_color = "#FFFFFF"
            button_color = "#000000"
            button_text_color = "#FFFFFF"
            
            create_branding_response = self.branding_api.create_brand(
                brand_name=brand_name,
                brand_logo=brand_logo,
                background_color=background_color,
                button_color=button_color,
                button_text_color=button_text_color
            )

            assert create_branding_response is not None
            assert create_branding_response.brand_id is not None
            assert isinstance(create_branding_response, boldsign.BrandCreated)
            TestCustomFieldsApi.created_brand_id = create_branding_response.brand_id

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=147)
    def test_create_custom_field(self):
        try:
            custom_form_fields = boldsign.CustomFormField(
                fieldType="Signature",
                font="Courier",
                width= 60,
                height=60,
            )

            brand_custom_field_details_request = boldsign.BrandCustomFieldDetails(
                fieldName=TestCustomFieldsApi.Custom_field_name,
                fieldDescription="Test custon field creation",
                fieldOrder=1,
                brandId=TestCustomFieldsApi.created_brand_id,
                formField=custom_form_fields
            )

            create_custom_field_details_response =self.custom_field_api.create_custom_field(
                brand_custom_field_details=brand_custom_field_details_request
                )
            assert create_custom_field_details_response is not None
            assert create_custom_field_details_response.custom_field_id is not None
            TestCustomFieldsApi.created_custom_field_id = create_custom_field_details_response.custom_field_id
            logger.info("Custom field created with ID: %s", TestCustomFieldsApi.created_custom_field_id)
        except ApiException as e:
            logger.error("API Exception during custom field creation: %s", str(e))
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            logger.error("Unexpected exception during custom field creation: %s", str(e))
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=148)
    def test_create_custom_field_negative_empty_field_name(self):
        try:
            custom_form_fields = boldsign.CustomFormField(
                fieldType="Signature",
                font="Courier",
                width=60,
                height=60,
            )

            brand_custom_field_details_request = boldsign.BrandCustomFieldDetails(
                fieldName="",
                fieldDescription="Test custom field creation with invalid type",
                fieldOrder=1,
                brandId=TestCustomFieldsApi.created_brand_id,
                formField=custom_form_fields
            )

            # Attempt to create the custom field with invalid field type
            create_custom_field_details_response = self.custom_field_api.create_custom_field(
                brand_custom_field_details=brand_custom_field_details_request
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            logger.error("Unexpected exception during custom field creation: %s", str(e))
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=149)
    def test_create_custom_field_negative_invalid_brand_id(self):
        try:
            custom_form_fields = boldsign.CustomFormField(
                fieldType="Signature",
                font="Courier",
                width=60,
                height=60,
            )

            invalid_brand_id = "invalid-brand-id"

            brand_custom_field_details_request = boldsign.BrandCustomFieldDetails(
                fieldName=TestCustomFieldsApi.Custom_field_name,
                fieldDescription="Test custom field creation with invalid brand ID",
                fieldOrder=1,
                brandId=invalid_brand_id,
                formField=custom_form_fields
            )

            self.custom_field_api.create_custom_field(
                brand_custom_field_details=brand_custom_field_details_request
            )

            assert False, "Expected an exception due to invalid brand ID, but received a response."

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=150)
    def test_edit_custom_field(self):
        try:
            custom_form_fields = boldsign.CustomFormField(
                fieldType="TextBox",
                font="Courier",
                width= 60,
                height=60,
                validationCustomRegex="NumbersOnly",
                isRequired=True
            )

            edit_custom_field_details_request = boldsign.BrandCustomFieldDetails(
                fieldName=TestCustomFieldsApi.Custom_field_name,
                fieldDescription="Test custon field creation",
                fieldOrder=1,
                brandId=TestCustomFieldsApi.created_brand_id,
                formField=custom_form_fields
            )
            edit_custom_field_details_response = self.custom_field_api.edit_custom_field(
            custom_field_id=TestCustomFieldsApi.created_custom_field_id,
            brand_custom_field_details=edit_custom_field_details_request
        )
            assert edit_custom_field_details_response is not None
            print(edit_custom_field_details_response.message)
            assert edit_custom_field_details_response.message == "Custom field edited successfully"
            logger.info("Custom field updated successfully.")
        except ApiException as e:
            logger.error("API Exception during custom field update: %s", str(e))
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            logger.error("Unexpected exception during custom field update: %s", str(e))
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=151)
    def test_edit_custom_field_negative_invalid_custom_field_id(self):
        try:
            custom_form_fields = boldsign.CustomFormField(
                fieldType="TextBox",
                font="Courier",
                width=60,
                height=60,
                validationCustomRegex="NumbersOnly",
                isRequired=True
            )

            invalid_custom_field_id = "invalid-custom-field-id"

            edit_custom_field_details_request = boldsign.BrandCustomFieldDetails(
                fieldName=TestCustomFieldsApi.Custom_field_name,
                fieldDescription="Test custom field update with invalid ID",
                fieldOrder=1,
                brandId=TestCustomFieldsApi.created_brand_id,
                formField=custom_form_fields
            )

            self.custom_field_api.edit_custom_field(
                custom_field_id=invalid_custom_field_id,
                brand_custom_field_details=edit_custom_field_details_request
            )

            assert False, "Expected an exception due to invalid custom field ID, but received a response."

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=152)
    def test_edit_custom_field_invalid_brand_id(self):
        try:
            custom_form_fields = boldsign.CustomFormField(
                fieldType="TextBox",
                font="Courier",
                width=60,
                height=60
            )

            edit_custom_field_details_request = boldsign.BrandCustomFieldDetails(
                fieldName="InvalidBrandIDTest",
                fieldDescription="Invalid brand ID",
                fieldOrder=1,
                brandId="InvalidBrandID",
                formField=custom_form_fields
            )

            response = self.custom_field_api.edit_custom_field(
                custom_field_id=TestCustomFieldsApi.created_custom_field_id,
                brand_custom_field_details=edit_custom_field_details_request
            )
            assert False, "Expected failure due to invalid brand ID."

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=153)
    def test_list_custom_fields(self):
        logger.info("Listing custom fields...")
        try:
            custom_fields = self.custom_field_api.custom_fields_list(
                brand_id=TestCustomFieldsApi.created_brand_id,
            )
            assert custom_fields is not None
            assert len(custom_fields.result) > 0
            logger.info("Custom fields listed successfully. Count: %d", len(custom_fields.result))
        except ApiException as e:
            logger.error("API Exception during listing custom fields: %s", str(e))
            assert False, f"API Exception occurred: %s" % str(e)
        except Exception as e:
            logger.error("Unexpected exception during listing custom fields: %s", str(e))
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=154)
    def test_list_custom_fields_negative_invalid_brand_id(self):
        logger.info("Listing custom fields with invalid brand ID...")

        try:
            invalid_brand_id = "invalid-brand-id"

            custom_fields = self.custom_field_api.custom_fields_list(
                brand_id=invalid_brand_id,
            )

            assert False, "Expected an exception due to invalid brand ID, but received a response."

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=155)
    def test_embed_custom_field_successful(self):
        try:
            current_date = datetime.datetime.now()
            link_valid_till = current_date + datetime.timedelta(days=20)

            embedded_custom_field_response = self.custom_field_api.embed_custom_field(
                brand_id=TestCustomFieldsApi.created_brand_id,
                link_valid_till=link_valid_till
            )

            logger.info("Embedded custom field response: %s", embedded_custom_field_response)

            assert embedded_custom_field_response is not None

        except ApiException as e:
            logger.error("API Exception during custom field embedding: %s", str(e))
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            logger.error("Unexpected exception during custom field embedding: %s", str(e))
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=156)
    def test_embed_custom_field_invalid_brand_id_negative(self):
        try:
            current_date = datetime.datetime.now()
            link_valid_till = current_date + datetime.timedelta(days=20)
            invalid_brand_id ="invalid-brand-id"

            self.custom_field_api.embed_custom_field(
                brand_id=invalid_brand_id,
                link_valid_till=link_valid_till
            )

            assert False, "Expected an exception due to invalid brand ID, but received a response."

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=157)
    def test_delete_custom_field(self):
        logger.info("Deleting the custom field...")
        try:
            custom_field_id=TestCustomFieldsApi.created_custom_field_id
            # Deleting the created custom field
            response = self.custom_field_api.delete_custom_field(
                custom_field_id=custom_field_id
            )
            assert response.message == "Custom field deleted successfully"
            logger.info("Custom field deleted successfully.")
        except ApiException as e:
            logger.error("API Exception during custom field deletion: %s", str(e))
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            logger.error("Unexpected exception during custom field deletion: %s", str(e))
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=158)
    def test_delete_custom_field_negative_invalid_custom_field_id(self):
        logger.info("Attempting to delete a custom field with an invalid custom field ID...")

        try:
            invalid_custom_field_id = "invalid-custom-field-id"

            self.custom_field_api.delete_custom_field(
                custom_field_id=invalid_custom_field_id
            )

            assert False, "Expected an exception due to invalid custom field ID, but received a response."

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=159)
    def test_delete_brand(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)

            brandId = TestCustomFieldsApi.created_brand_id
                        
            delete_brand_response = self.branding_api.delete_brand(
                brand_id=brandId
            )
            assert delete_brand_response is not None
            assert delete_brand_response.message =="The brand has been deleted successfully"
            assert isinstance(delete_brand_response, boldsign.BrandingMessage)

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