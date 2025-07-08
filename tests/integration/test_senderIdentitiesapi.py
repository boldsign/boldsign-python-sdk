import unittest
import pytest
import boldsign
import os
import time
import random
import string
from boldsign.rest import ApiException
from random import randint
from config import API_KEY, BASE_URL

@pytest.mark.integration
class TestSenderIdentitysApi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.created_brand_id = None
        cls.emailId = None
        cls.contact_id = None

    def random_numbers(self):
        range_start = 10**(3-1)
        range_end = (10**3)-1
        return str(randint(range_start, range_end))
    
    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=API_KEY, host=BASE_URL)
        self.api_client = boldsign.ApiClient(self.configuration)
        srting_value = self.random_numbers()
        TestSenderIdentitysApi.emailId = "sdktesting"+srting_value+"@syncfusion.com"

    @pytest.mark.run(order=165)
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
            TestSenderIdentitysApi.created_brand_id = create_branding_response.brand_id

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=166)
    def test_create_sender_identities_positive(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            sender_identity_name = "SenderIdentity API"
            sender_identity_request = boldsign.CreateSenderIdentityRequest(
                name= sender_identity_name,
                email=TestSenderIdentitysApi.emailId
            )
            
            sender_identitys_response = self.sender_identities_api.create_sender_identities(
                create_sender_identity_request= sender_identity_request
            )
            assert sender_identitys_response is not None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(10)

    @pytest.mark.run(order=167)
    def test_create_sender_identities_negative_missing_name(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            sender_identity_request = boldsign.CreateSenderIdentityRequest(
                name="",
                email=TestSenderIdentitysApi.emailId
            )

            sender_identity_response = self.sender_identities_api.create_sender_identities(
                create_sender_identity_request=sender_identity_request
            )

            assert sender_identity_response is not None

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=168)
    def test_create_sender_identities_negative_with_invalid_email_id(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for create sender identities
            sender_identity_name = "SenderIdentity API"
            sender_identity_request = boldsign.CreateSenderIdentityRequest(
                name= sender_identity_name,
                email="InvalidEmail"
            )
            
            sender_identitys_response = self.sender_identities_api.create_sender_identities(
                create_sender_identity_request= sender_identity_request
            )
            assert sender_identitys_response is not None
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"Email\":[\"The field Email is invalid.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=169)
    def test_create_sender_identities_negative_empty_email(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            sender_identity_name = "Sender Identity with Empty Email"
            sender_identity_request = boldsign.CreateSenderIdentityRequest(
                name=sender_identity_name,
                email=""  # Empty email
            )

            sender_identity_response = self.sender_identities_api.create_sender_identities(
                create_sender_identity_request=sender_identity_request
            )
            assert sender_identity_response is not None

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=170)
    def test_update_sender_identities_positive(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for update sender identities
            emailId = TestSenderIdentitysApi.emailId
            sender_identity_name = "SenderIdentity API Update"
            edit_sender_identity_request = boldsign.EditSenderIdentityRequest(
                name= sender_identity_name
            )
            
            update_sender_identity_response = self.sender_identities_api.update_sender_identities(
                email=emailId,
                edit_sender_identity_request=edit_sender_identity_request
            )
            assert update_sender_identity_response is None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=171)
    def test_update_sender_identities_empty_name(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            email_id = TestSenderIdentitysApi.emailId
            empty_name = ""
            
            edit_sender_identity_request = boldsign.EditSenderIdentityRequest(
                name=empty_name
            )
            
            self.sender_identities_api.update_sender_identities(
                email=email_id,
                edit_sender_identity_request=edit_sender_identity_request
            )
            assert False, "Expected failure due to empty sender identity name."

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            assert False, f"Unexpected error: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=172)
    def test_update_sender_identities_negative_invalid_email(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for update sender identities
            emailId = "InvalidEmail"
            sender_identity_name = "SenderIdentity API Update"
            edit_sender_identity_request = boldsign.EditSenderIdentityRequest(
                name= sender_identity_name
            )
            
            update_sender_identity_response = self.sender_identities_api.update_sender_identities(
                email=emailId,
                edit_sender_identity_request=edit_sender_identity_request
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"email\":[\"The field email is invalid.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=173)
    def test_update_sender_identities_negative_empty_email(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for update sender identities
            emailId = ""
            sender_identity_name = "SenderIdentity API Update"
            edit_sender_identity_request = boldsign.EditSenderIdentityRequest(
                name= sender_identity_name
            )
            
            update_sender_identity_response = self.sender_identities_api.update_sender_identities(
                email=emailId,
                edit_sender_identity_request=edit_sender_identity_request
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=174)
    def test_list_sender_identities_positive(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)

            Page= 1
            PageSize = 10
            
            list_sender_identity_response = self.sender_identities_api.list_sender_identities(
                page= Page,
                page_size=PageSize
            )
            assert list_sender_identity_response is not None
            assert list_sender_identity_response.result is not None
            assert isinstance(list_sender_identity_response, boldsign.SenderIdentityList)

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)
            
    @pytest.mark.run(order=175)
    def test_list_sender_identities_negative(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for List sender identities
            Page= 200
            PageSize = 210
            
            list_sender_identity_response = self.sender_identities_api.list_sender_identities(
                page= Page,
                page_size=PageSize
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

    @pytest.mark.run(order=176)
    def test_list_sender_identities_negative_invalid_page_and_page_size(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for List sender identities
            Page= -12
            PageSize = -17
            
            list_sender_identity_response = self.sender_identities_api.list_sender_identities(
                page= Page,
                page_size=PageSize
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=177)
    def test_resend_invitation_sender_identities_positive(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for List sender identities
            emailId = TestSenderIdentitysApi.emailId
            
            re_request_sender_identity_response = self.sender_identities_api.resend_invitation_sender_identities(
                email= emailId
            )
            assert re_request_sender_identity_response is None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=178)
    def test_resend_invitation_sender_identities_negative(self):
        try:
            
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for List sender identities
            emailId = "InvalidEmail"
            
            re_request_sender_identity_response = self.sender_identities_api.resend_invitation_sender_identities(
                email= emailId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"email\":[\"The field email is invalid.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"            
        finally:
            time.sleep(5)

    @pytest.mark.run(order=179)
    def test_resend_invitation_sender_identities_negative_empty_emailid(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for List sender identities
            emailId = ""
            
            re_request_sender_identity_response = self.sender_identities_api.resend_invitation_sender_identities(
                email= emailId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=180)
    def test_resend_invitation_sender_identities_negative_non_existing_senderidentity_email(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for List sender identities
            emailId = "sdktestinabc@syncfusion.com"
            
            re_request_sender_identity_response = self.sender_identities_api.resend_invitation_sender_identities(
                email= emailId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=181)
    def test_re_request_sender_identities_negative(self):
        try:
            
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for re request sender identities
            emailId = TestSenderIdentitysApi.emailId
            
            re_request_sender_identity_response = self.sender_identities_api.re_request_sender_identities(
                email= emailId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"error\":\"You can re-request sender identity only if the invitation is rejected.\"}")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"     
        finally:
            time.sleep(5)

    @pytest.mark.run(order=182)
    def test_delete_sender_identities_positive(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for delete sender identities
            emailId = TestSenderIdentitysApi.emailId
            
            delete_sender_identity_response = self.sender_identities_api.delete_sender_identities(
                email= emailId
            )
            assert delete_sender_identity_response is None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"        
        finally:
            time.sleep(5)

    @pytest.mark.run(order=183)
    def test_delete_sender_identities_negative_invalid_email(self):
        try:
            
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for delete sender identities
            emailId = "InvalidEmail"
            
            delete_sender_identity_response = self.sender_identities_api.delete_sender_identities(
                email= emailId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"email\":[\"The field email is invalid.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"  
        finally:
            time.sleep(5)

    @pytest.mark.run(order=184)
    def test_delete_sender_identities_negative_empty_email(self):
        try:
            
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            emailId = ""
            
            delete_sender_identity_response = self.sender_identities_api.delete_sender_identities(
                email= emailId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"email\":[\"The email field is required.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"  
        finally:
            time.sleep(5)

    @pytest.mark.run(order=185)
    def test_delete_sender_identities_negative_non_existance_sender_identity_email(self):
        try:
            
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for delete sender identities
            emailId = "sdktestinabc@syncfusion.com"
            
            delete_sender_identity_response = self.sender_identities_api.delete_sender_identities(
                email= emailId
            )

        except ApiException as e:
            assert e.status == 403
            assert e.reason == "Forbidden"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=186)
    def test_create_sender_identities_with_existing_brand(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)

            existing_brand_id = TestSenderIdentitysApi.created_brand_id

            sender_identity_name = "Sender Identity with Existing Brand"
            sender_identity_request = boldsign.CreateSenderIdentityRequest(
                name=sender_identity_name,
                email=TestSenderIdentitysApi.emailId,
                brandId=existing_brand_id
            )

            sender_identity_response = self.sender_identities_api.create_sender_identities(
                create_sender_identity_request=sender_identity_request
            )

            assert sender_identity_response is not None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nUnexpected exception when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(10)

    @pytest.mark.run(order=187)
    def test_delete_sender_identities_(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)

            emailId = TestSenderIdentitysApi.emailId
            
            delete_sender_identity_response = self.sender_identities_api.delete_sender_identities(
                email= emailId
            )
            assert delete_sender_identity_response is None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=188)
    def test_delete_brand_positive(self):
        try:
            self.branding_api = boldsign.BrandingApi(self.api_client)

            brandId = TestSenderIdentitysApi.created_brand_id
                        
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

    @pytest.mark.run(order=189)
    def test_create_sender_identities_with_dynamic_80_chars_name(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            sender_identity_name = ''.join(random.choices(string.ascii_letters + string.digits, k=80))
            sender_identity_request = boldsign.CreateSenderIdentityRequest(
                name=sender_identity_name,
                email=TestSenderIdentitysApi.emailId
            )
            sender_identitys_response = self.sender_identities_api.create_sender_identities(
                create_sender_identity_request=sender_identity_request
            )
            assert sender_identitys_response is not None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(10)

    pytest.mark.run(order=190)
    def test_create_sender_identities_negative_with_duplicate_email(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            sender_identity_name = ''.join(random.choices(string.ascii_letters + string.digits, k=80))
            sender_identity_request = boldsign.CreateSenderIdentityRequest(
                name=sender_identity_name,
                email=TestSenderIdentitysApi.emailId
            )
            sender_identitys_response = self.sender_identities_api.create_sender_identities(
                create_sender_identity_request=sender_identity_request
            )
            assert sender_identitys_response is not None
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}" 
        finally:
            time.sleep(5)

if __name__ == '__main__':
    unittest.main()