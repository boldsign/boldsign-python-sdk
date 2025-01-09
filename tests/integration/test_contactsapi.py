import unittest
import pytest
import boldsign
import os
import time
from boldsign.rest import ApiException
from random import randint

APIKey = os.getenv('BoldSignAPIKey')
url = os.getenv('BoldSignURL')

@pytest.mark.integration
class TestContactsApi(unittest.TestCase):
    
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
        TestContactsApi.emailId = "sdktesting"+srting_value+"@syncfusion.com"

    @pytest.mark.run(order=63)
    def test_create_contacts_positive(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)
            
            # Define parameters for create contacts
            User_name = "SDK Testing 1"
            email_Id = TestContactsApi.emailId
            contacts_details = boldsign.ContactDetails(
                email= email_Id,
                name= User_name
            )
            
            create_contacts_response = self.contacts_api.create_contact(
                contact_details= [contacts_details]
            )
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    
    @pytest.mark.run(order=64)
    def test_create_contacts_negative(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)
            
            # Define parameters for create Contacts
            User_name = "SDK Testing 1"
            email_Id = "InvalidEmail"
            contacts_details = boldsign.ContactDetails(
                email= email_Id,
                name= User_name
            )
            
            create_contacts_response = self.contacts_api.create_contact(
                contact_details=[contacts_details]
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"[0].Email\":[\"The field Email is invalid.\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"  

    @pytest.mark.run(order=65)
    def test_get_brand_positive(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)

            # Define parameters for contact user list
            Page =1
            Page_size = 20
            
                        
            contact_user_list_response = self.contacts_api.contact_user_list(
                page=Page,
                page_size=Page_size
            )
            assert contact_user_list_response is not None
            assert contact_user_list_response.result is not None
            contactsList = contact_user_list_response.result         
            assert isinstance(contact_user_list_response, boldsign.ContactsList)

            for contacts in contactsList:
                if contacts.email == TestContactsApi.emailId:
                    TestContactsApi.contact_id = contacts.id
                    print(contacts.email)

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"     
            
    @pytest.mark.run(order=66)
    def test_get_contact_positive(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)

            # Define parameters for get brand
            contactsId = TestContactsApi.contact_id
                        
            get_contact_response = self.contacts_api.get_contact(
                id=contactsId
            )
            assert get_contact_response is not None
            assert get_contact_response.email is not None
            assert get_contact_response.email == TestContactsApi.emailId
            assert get_contact_response.name== 'SDK Testing 1'
            assert isinstance(get_contact_response, boldsign.ContactsDetails)

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"       
            
    @pytest.mark.run(order=67)
    def test_get_contact_negative(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)

            # Define parameters for get brand
            contactsId = "WrongUserID"
                        
            get_contact_response = self.contacts_api.get_contact(
                id=contactsId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"id\":[\"Provide a valid Contact Id\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"   
            
    @pytest.mark.run(order=68)
    def test_update_contact_positive(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)

            # Define parameters for update contact
            contactsId = TestContactsApi.contact_id

            update_request = boldsign.ContactDetails(
                name="Update Contact name",
                email=TestContactsApi.emailId
                )
                        
            updat_contact_response = self.contacts_api.update_contact(
                id=contactsId,
                contact_details=update_request
            )
            assert updat_contact_response is None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"       
            
    @pytest.mark.run(order=69)
    def test_update_contact_negative(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)

            # Define parameters for update contact
            contactsId = "wrongUserId"

            update_request = boldsign.ContactDetails(
                name="Update Contact name",
                email=TestContactsApi.emailId
                )
                        
            updat_contact_response = self.contacts_api.update_contact(
                id=contactsId,
                contact_details=update_request
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"id\":[\"Provide a valid Contact Id\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"   

      
    @pytest.mark.run(order=70)
    def test_delete_contacts_positive(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)
            
            # Define parameters for delete contacts
            contactsId = TestContactsApi.contact_id
            
            delete_contacts_response = self.contacts_api.delete_contacts(
               id= contactsId
            )

            assert delete_contacts_response is None
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"        
  
    
    @pytest.mark.run(order=71)
    def test_delete_contacts_negative(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)
            
            # Define parameters for delete contacts
            contactsId = "WrongId"
            
            delete_contacts_response = self.contacts_api.delete_contacts(
               id= contactsId
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert e.body.startswith("{\"errors\":{\"id\":[\"Provide a valid Contact Id\"]},")
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"    


if __name__ == '__main__':
    unittest.main()