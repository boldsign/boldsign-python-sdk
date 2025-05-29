import unittest
import pytest
import boldsign
import time
from boldsign.rest import ApiException
from random import randint
from config import API_KEY, BASE_URL

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
        self.configuration = boldsign.Configuration(api_key=API_KEY, host=BASE_URL)
        self.api_client = boldsign.ApiClient(self.configuration)
        srting_value = self.random_numbers()
        TestContactsApi.emailId = "sdktesting"+srting_value+"@syncfusion.com"

    @pytest.mark.run(order=124)
    def test_create_contacts_positive(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)
            
            User_name = "SDK Testing 1"
            email_Id = TestContactsApi.emailId
            contacts_details = boldsign.ContactDetails(
                email= email_Id,
                name= User_name
            )
            print(contacts_details)
            create_contacts_response = self.contacts_api.create_contact(
                contact_details= [contacts_details]
            )
            print(TestContactsApi.emailId)
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=125)
    def test_create_contacts_positive_with_all_fields(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)
            
            # Define parameters for create contacts
            User_name = "SDK Testing 1"
            email_Id = TestContactsApi.emailId + str(45)
            contacts_details = boldsign.ContactDetails(
                email= email_Id,
                name= User_name,
                phoneNumber= boldsign.PhoneNumber(
                countryCode="+91",
                number="6381261236"
            ),
            jobTitle= "Developer",
            companyName="CubeFlakes"
            )
            print(contacts_details)
            create_contacts_response = self.contacts_api.create_contact(
                contact_details= [contacts_details]
            )
            print(TestContactsApi.emailId)
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=126)
    def test_create_contacts_negative_invalid_email(self):
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=127)
    def test_list_contact_positive(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)

            # Define parameters for contact user list
            Page =1
            Page_size = 100
            
                        
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
                    # print(contacts.email)
                    print(f"Contact Email: {TestContactsApi.emailId}, Contact ID: {TestContactsApi.contact_id}")

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=128)
    def test_list_contact_negative_invalid_page(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)

            Page = -1
            Page_size = 100

            contact_user_list_response = self.contacts_api.contact_user_list(
                page=Page,
                page_size=Page_size
            )

            assert False, "Expected an exception due to invalid page number, but received a response."

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=129)
    def test_list_contact_negative_invalid_page_size(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)

            Page = 1
            Page_size = -100

            contact_user_list_response = self.contacts_api.contact_user_list(
                page=Page,
                page_size=Page_size
            )

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=130)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=131)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=132)
    def test_update_contact_positive(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)
            print(f"ContactId: {TestContactsApi.contact_id}")
            # Define parameters for update contact
            contactsId = TestContactsApi.contact_id

            update_request = boldsign.ContactDetails(
                name="Update Contact name",
                email=TestContactsApi.emailId
                )

            update_contact_response = self.contacts_api.update_contact(
                id=contactsId,
                contact_details=update_request
            )
            assert update_contact_response is None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=133)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=134)
    def test_update_contact_negative_invalid_email(self):
        try:
            self.contacts_api = boldsign.ContactsApi(self.api_client)
            contact_id = TestContactsApi.contact_id

            update_request = boldsign.ContactDetails(
                name="Update Contact name",
                email="invalid-email"
            )

            update_contact_response = self.contacts_api.update_contact(
                id=contact_id,
                contact_details=update_request
            )
            assert update_contact_response is None

        except ApiException as e:
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=136)
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=137)
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
        finally:
            time.sleep(5)

if __name__ == '__main__':
    unittest.main()