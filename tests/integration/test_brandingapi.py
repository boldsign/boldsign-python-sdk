import unittest
import pytest
import boldsign
import time
from boldsign.rest import ApiException
import time
from config import API_KEY, BASE_URL

@pytest.mark.integration
class TestBrandApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.created_brand_id = None
    
    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=API_KEY, host=BASE_URL)
        self.api_client = boldsign.ApiClient(self.configuration)

    @pytest.mark.run(order=107)
    def test_create_brand_positive(self):
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
            TestBrandApi.created_brand_id = create_branding_response.brand_id

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=108)
    def test_create_brand_positive_with_only_required_fields(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters for create brand
            brand_name = 'TestBrandAPI'
            brand_logo = 'tests/documents/input/logo.png'
            
            create_branding_response = self.branding_api.create_brand(
                brand_name=brand_name,
                brand_logo=brand_logo
            )

            assert create_branding_response is not None
            assert create_branding_response.brand_id is not None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=109)
    def test_create_brand_negative_empty_name(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            brand_name = ''
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

            assert create_branding_response is None

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"BrandName\":[\"The Brand name is required\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=110)
    def test_create_brand_negative_invalid_background_color(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters for create brand with invalid background color
            brand_name = 'TestBrandAPI'
            brand_logo = 'tests/documents/input/logo.png'
            background_color = 'invalid_color'
            button_color = "#000000"
            button_text_color = "#FFFFFF"
            
            create_branding_response = self.branding_api.create_brand(
                brand_name=brand_name,
                brand_logo=brand_logo,
                background_color=background_color,
                button_color=button_color,
                button_text_color=button_text_color
            )

            assert create_branding_response is None

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nUnexpected exception occurred when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=111)
    def test_create_brand_negative_invalid_button_color(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters for create brand with an invalid button color
            brand_name = 'TestBrandAPI'
            brand_logo = 'tests/documents/input/logo.png'
            background_color = "#FFFFFF"
            button_color = 'invalid_color'  # Invalid button color format
            button_text_color = "#FFFFFF"
            
            # Attempt to create a brand with the invalid button color
            create_branding_response = self.branding_api.create_brand(
                brand_name=brand_name,
                brand_logo=brand_logo,
                background_color=background_color,
                button_color=button_color,
                button_text_color=button_text_color
            )

            assert create_branding_response is None

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nUnexpected exception occurred when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=112)
    def test_create_brand_negative_invalid_logo_path(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters with an empty logo file path
            brand_name = 'TestBrandAPI'
            brand_logo = 'tests/documents/input/doc_1.pdf'
            background_color = "#FFFFFF"
            button_color = "#000000"
            button_text_color = "#FFFFFF"
            
            # Attempt to create a brand with an empty logo path
            create_branding_response = self.branding_api.create_brand(
                brand_name=brand_name,
                brand_logo=brand_logo,
                background_color=background_color,
                button_color=button_color,
                button_text_color=button_text_color
            )

            assert create_branding_response is None

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nUnexpected exception occurred when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=113)
    def test_create_brand_negative_invalid_button_text_color(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters with an invalid button text color
            brand_name = 'TestBrandAPI'
            brand_logo = 'tests/documents/input/logo.png'
            background_color = "#FFFFFF"
            button_color = "#000000"
            button_text_color = "invalid_color"
            
            # Attempt to create a brand with an invalid button text color
            create_branding_response = self.branding_api.create_brand(
                brand_name=brand_name,
                brand_logo=brand_logo,
                background_color=background_color,
                button_color=button_color,
                button_text_color=button_text_color
            )

            assert create_branding_response is None

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nUnexpected exception occurred when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=114)
    def test_edit_brand_positive(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters for create brand
            brandId = TestBrandApi.created_brand_id
            brand_name = 'TestBrandAPIEdit'
            
            edit_branding_response = self.branding_api.edit_brand(
                brand_id= brandId,
                brand_name=brand_name
            )
            assert edit_branding_response is not None
            assert edit_branding_response.brand_id is not None
            assert isinstance(edit_branding_response, boldsign.BrandCreated)

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=115)
    def test_edit_brand_negative_invalid_filepath(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters for create brand
            brandId = TestBrandApi.created_brand_id
            brand_name = 'TestBrandAPIEdit'
            brand_logo = 'tests/documents/input/doc_1.pdf'
            
            edit_branding_response = self.branding_api.edit_brand(
                brand_id= brandId,
                brand_name=brand_name,
                brand_logo=brand_logo
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=116)
    def test_edit_brand_negative(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters for create brand
            brandId = "wrongDocId"
            brand_name = 'TestBrandAPIEdit'
            
            edit_branding_response = self.branding_api.edit_brand(
                brand_id= brandId,
                brand_name=brand_name
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"brandId\":[\"Provide a valid brand ID\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=117)
    def test_brand_list_positive(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
                        
            branding_list_response = self.branding_api.brand_list()
            assert branding_list_response is not None
            assert len(branding_list_response.result) > 0

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=118)
    def test_get_brand_positive(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)

            # Define parameters for get brand
            brandId = TestBrandApi.created_brand_id
                        
            get_brand_response = self.branding_api.get_brand(
                brand_id=brandId
            )
            assert get_brand_response is not None
            assert get_brand_response.brand_id is not None
            assert get_brand_response.brand_name == 'TestBrandAPIEdit'
            assert isinstance(get_brand_response, boldsign.ViewBrandDetails)

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=119)
    def test_get_brand_negative(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters for brand list
            brandId = "wrongDocId"
            
            branding_list_response = self.branding_api.get_brand(
                brand_id= brandId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"brandId\":[\"Provide a valid brand ID\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=120)
    def test_reset_default_brand_positive(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)

            # Define parameters for reset_default brand
            brandId = TestBrandApi.created_brand_id
                        
            get_brand_response = self.branding_api.reset_default_brand(
                brand_id=brandId
            )
            assert get_brand_response is not None
            assert get_brand_response.message == "The default brand has been updated successfully"
            assert isinstance(get_brand_response, boldsign.BrandingMessage)

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=121)
    def test_reset_default_brand_negative(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters for reset_default brand
            brandId = "wrongDocId"
            
            branding_list_response = self.branding_api.get_brand(
                brand_id= brandId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"brandId\":[\"Provide a valid brand ID\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=122)
    def test_delete_brand_positive(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)

            # Define parameters for delete brand
            brandId = TestBrandApi.created_brand_id
                        
            delete_brand_response = self.branding_api.delete_brand(
                brand_id=brandId
            )
            assert delete_brand_response is not None
            assert delete_brand_response.message == "The brand has been deleted successfully"
            assert isinstance(delete_brand_response, boldsign.BrandingMessage)

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=123)
    def test_delete__brand_negative(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)
            
            # Define parameters for delete brand
            brandId = "wrongDocId"
            
            delete_brand_response = self.branding_api.get_brand(
                brand_id= brandId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"brandId\":[\"Provide a valid brand ID\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

if __name__ == '__main__':
    unittest.main()