import unittest
import pytest
import boldsign
import os
import time
import boldsign.models
import boldsign.models.users_details
from boldsign.rest import ApiException
from random import randint

APIKey = os.getenv('BoldSignAPIKey')
url = os.getenv('BoldSignURL')

@pytest.mark.integration
class TestUsersApi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.emailId = None
        cls.user_id = None

    def random_numbers(self):
       range_start = 10**(3-1)
       range_end = (10**3)-1
       return str(randint(range_start, range_end))
    
    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=APIKey, host=url)
        self.api_client = boldsign.ApiClient(self.configuration)
        srting_value = self.random_numbers()
        TestUsersApi.emailId = "prakash.viswanathan+sdk+"+srting_value+"@syncfusion.com"

    @pytest.mark.run(order=86)
    def test_create_user_positive(self):
        try:
            self.user_api = boldsign.UserApi(self.api_client)
            
            # Define parameters for create user
            create_user_request = boldsign.CreateUser(
                emailId=TestUsersApi.emailId
            )
            
            create_user_response = self.user_api.create_user(
                create_user= [create_user_request]
            )
            print("TestUserID:"+TestUsersApi.emailId)
            assert create_user_response is None           

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    
    @pytest.mark.run(order=87)
    def test_create_user_negative(self):
        try:
            self.user_api = boldsign.UserApi(self.api_client)
            
            # Define parameters for create user
            create_user_request = boldsign.CreateUser(
                emailId="InvalidEmail"
            )
            
            create_user_response = self.user_api.create_user(
                create_user= [create_user_request]
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"[0]\":[\"The email property does not contain a valid email address\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}" 
            
    @pytest.mark.run(order=88)
    def test_get_user_list_positive(self):
        try:
            print("TestUserID:"+TestUsersApi.emailId)
            self.user_api = boldsign.UserApi(self.api_client)

            # Define parameters for contact user list
            Page =1
            Page_size = 20
            
                        
            user_list_response = self.user_api.list_users(
                page=Page,
                page_size=Page_size
            )
            assert user_list_response is not None
            assert user_list_response.result is not None
            UsersList = user_list_response.result
            
            for users in UsersList:
                if users.email == TestUsersApi.emailId:
                    TestUsersApi.user_id = users.user_id
                    print("TestUserID:"+users.user_id)

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"     
            
    @pytest.mark.run(order=89)
    def test_get_user_list_negative(self):
        try:
            self.user_api = boldsign.UserApi(self.api_client)

            # Define parameters for contact user list
            Page =250
            Page_size = 250
            
                        
            user_list_response = self.user_api.list_users(
                page=Page,
                page_size=Page_size
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"PageSize\":[\"Provide a valid page size between 1 and 100\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"     
            
    @pytest.mark.run(order=90)
    def test_get_user_positive(self):
        try:
            print("TestUserID:"+TestUsersApi.user_id)
            self.user_api = boldsign.UserApi(self.api_client)

            # Define parameters for get user
            userId = TestUsersApi.user_id
                        
            get_user_response = self.user_api.get_user(
                user_id=userId
            )
            assert get_user_response is not None
            assert get_user_response.email is not None
            assert get_user_response.email == TestUsersApi.emailId

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"                
            
    @pytest.mark.run(order=91)
    def test_get_user_negative(self):
        try:
            self.user_api = boldsign.UserApi(self.api_client)

            # Define parameters for get brand
            userId = "WrongUserID"
                        
            get_user_response = self.user_api.get_user(
                user_id=userId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"userId\":[\"Provide valid user id.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"   
            
    @pytest.mark.run(order=93)
    def test_update_user_negative(self):
        try:
            self.user_api = boldsign.UserApi(self.api_client)
            
           # Define parameters for update user
            user_Id = "WrongUserID"
            update_user_request = boldsign.UpdateUser(
                userId= user_Id
            )
            
            update_user_response = self.user_api.update_user(
                update_user=update_user_request
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"UserId\":[\"Provide valid user id.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"  
            
    @pytest.mark.run(order=94)
    def test_resend_invitation_user_positive(self):
        try:
            self.user_api = boldsign.UserApi(self.api_client)
            
            # Define parameters for resend_invitation
            user_Id = TestUsersApi.user_id
            
            resend_invitation_response = self.user_api.resend_invitation(
               user_id= user_Id
            )
            assert resend_invitation_response is None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"        
            
    @pytest.mark.run(order=95)
    def test_resend_invitation_user_negative(self):
        try:            
            self.user_api = boldsign.UserApi(self.api_client)
            
            # Define parameters for resend_invitation
            user_Id = "WrongUserID"
            
            resend_invitation_response = self.user_api.resend_invitation(
               user_id= user_Id
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"UserId\":[\"Provide valid user id.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"            
            
    @pytest.mark.run(order=96)
    def test_cancel_invitation_positive(self):
        try:            
            self.user_api = boldsign.UserApi(self.api_client)
            
            # Define parameters for user cancel invitation
            userId = TestUsersApi.user_id
            
            cancel_invitation_user_response = self.user_api.cancel_invitation(
              user_id=userId
            )
            assert cancel_invitation_user_response is None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"              
            
    @pytest.mark.run(order=97)
    def test_cancel_invitation_negative(self):
        try:            
            self.user_api = boldsign.UserApi(self.api_client)
            
            # Define parameters for user cancel invitation
            userId = "WrongUserID"
            
            cancel_invitation_user_response = self.user_api.cancel_invitation(
              user_id=userId
            )
           
        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"UserId\":[\"Provide valid user id.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"     


if __name__ == '__main__':
    unittest.main()