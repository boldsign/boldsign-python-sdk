import unittest

import pytest
import boldsign
import os
import time
from boldsign.rest import ApiException
import time

APIKey = os.getenv('API_KEY')
url = os.getenv('HOST_URL')

@pytest.mark.integration
class TestBrandApi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.created_brand_id = None
    
    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=APIKey, host=url)
        self.api_client = boldsign.ApiClient(self.configuration)

    @pytest.mark.run(order=53)
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
            time.sleep(10)

    @pytest.mark.run(order=54)
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
  
    
    @pytest.mark.run(order=55)
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
            
    @pytest.mark.run(order=56)
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

                   
    @pytest.mark.run(order=57)
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

    @pytest.mark.run(order=58)
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

                        
    @pytest.mark.run(order=59)
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

    @pytest.mark.run(order=60)
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
                        
    @pytest.mark.run(order=61)
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

    @pytest.mark.run(order=62)
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


if __name__ == '__main__':
    unittest.main()