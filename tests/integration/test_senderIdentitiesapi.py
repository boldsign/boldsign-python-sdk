import unittest
import pytest
import boldsign
import os
import time
from boldsign.rest import ApiException
from random import randint

APIKey = os.getenv('API_KEY')
url = os.getenv('HOST_URL')

@pytest.mark.integration
class TestSenderIdentitysApi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.emailId = None
        cls.contact_id = None

    def random_numbers(self):
       range_start = 10**(3-1)
       range_end = (10**3)-1
       return str(randint(range_start, range_end))
    
    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=APIKey, host=url)
        self.api_client = boldsign.ApiClient(self.configuration)
        srting_value = self.random_numbers()
        TestSenderIdentitysApi.emailId = "sdktesting"+srting_value+"@syncfusion.com"

   
    @pytest.mark.run(order=98)
    def test_create_sender_identities_positive(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)
            
            # Define parameters for create sender identities
            sender_identity_name = "SenderIdentity API"
            sender_identity_request = boldsign.CreateSenderIdentityRequest(
                name= sender_identity_name,
                email=TestSenderIdentitysApi.emailId
            )
            
            sender_identitys_response = self.sender_identities_api.create_sender_identities(
                create_sender_identity_request= sender_identity_request
            )
            assert sender_identitys_response is None           

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(10)

    
    @pytest.mark.run(order=99)
    def test_create_sender_identities_negative(self):
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

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"Email\":[\"The field Email is invalid.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"  

    @pytest.mark.run(order=100)
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
            
    @pytest.mark.run(order=101)
    def test_update_sender_identities_negative(self):
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
            
    @pytest.mark.run(order=102)
    def test_list_sender_identities_positive(self):
        try:
            self.sender_identities_api = boldsign.SenderIdentitiesApi(self.api_client)

            # Define parameters for List sender identities
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
            
    @pytest.mark.run(order=103)
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
            
    @pytest.mark.run(order=104)
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
            
    @pytest.mark.run(order=105)
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
            
    @pytest.mark.run(order=106)
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
            
    @pytest.mark.run(order=107)
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
            
    @pytest.mark.run(order=108)
    def test_delete_sender_identities_negative(self):
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


if __name__ == '__main__':
    unittest.main()