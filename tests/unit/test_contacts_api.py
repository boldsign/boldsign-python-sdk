import unittest
from unittest.mock import patch, MagicMock

import pytest
import boldsign
from boldsign.rest import ApiException

class TestContactsApi(unittest.TestCase):

    @patch('boldsign.ContactsApi')
    @pytest.mark.unit
    def testContactsList(self, mock_contacts_api):
        mock_contacts_api_instance = mock_contacts_api.return_value
        mock_contacts_api_instance.contact_user_list.return_value = MagicMock(result=[MagicMock()])

        contacts = mock_contacts_api_instance.contact_user_list()

        self.assertIsNotNone(contacts)
        self.assertGreater(len(contacts.result), 0)
        mock_contacts_api_instance.contact_user_list.assert_called_once()

    @patch('boldsign.ContactsApi')
    @pytest.mark.unit
    def testCreateContact(self, mock_contacts_api):
        mock_contacts_api_instance = mock_contacts_api.return_value
        mock_contacts_created = MagicMock(id="ContactsUser1")
        mock_contacts_api_instance.create_contact.return_value = mock_contacts_created

        contacts_data = {
            "name": "New contact",
            "email": "newEmail@gmail.com",
            "phoneNumber": "9876543210",
            "jobTitle": "Test",
            "companyName": "Syncfusion" 
        }

        created_contact = mock_contacts_api_instance.create_contact(**contacts_data)

        self.assertIsNotNone(created_contact)
        self.assertEqual(created_contact.id, "ContactsUser1")
        mock_contacts_api_instance.create_contact.assert_called_once_with(**contacts_data)

    @patch('boldsign.ContactsApi')
    @pytest.mark.unit
    def testUpdateContacts(self, mock_contacts_api):
        mock_contacts_api_instance = mock_contacts_api.return_value
        mock_contact_response = MagicMock(
            id = "ContactsUser1",
            name= "Update contacts",
            email= "updateEmail@gmail.com",
            phoneNumber= "98765432100",
            jobTitle= "UpdateTest",
            companyName= "UpdateSyncfusion" 
        )
        mock_contacts_api_instance.update_contact.return_value = mock_contact_response

        id = "ContactsUser1"
        contacts_data = {
            "name": "Update contacts",
            "email": "updateEmail@gmail.com",
            "phoneNumber": "98765432100",
            "jobTitle": "UpdateTest",
            "companyName": "UpdateSyncfusion" 
        }

        update_contact = mock_contacts_api_instance.update_contact(id, **contacts_data)

        self.assertIsNotNone(update_contact)
        self.assertEqual(update_contact.id, "ContactsUser1")
        self.assertEqual(update_contact.email, "updateEmail@gmail.com")
        self.assertEqual(update_contact.phoneNumber, "98765432100")
        self.assertEqual(update_contact.jobTitle, "UpdateTest")
        self.assertEqual(update_contact.companyName, "UpdateSyncfusion")
        mock_contacts_api_instance.update_contact.assert_called_once_with(id, **contacts_data)

    @patch('boldsign.ContactsApi')
    @pytest.mark.unit
    def testDeleteContacts(self, mock_contacts_api):
        mock_contacts_api_instance = mock_contacts_api.return_value
        mock_response = MagicMock()
        mock_response.message = "Contacts deleted successfully"
        mock_contacts_api_instance.delete_contacts.return_value = mock_response

        id = "ContactsUser1"
        response = mock_contacts_api_instance.delete_contacts(id)

        self.assertIsNotNone(response)
        self.assertEqual(response.message, "Contacts deleted successfully")
        mock_contacts_api_instance.delete_contacts.assert_called_once_with(id)

    @patch('boldsign.ContactsApi')
    @pytest.mark.unit
    def testGetContacts(self, mock_contacts_api):       
        mock_contacts_api_instance = mock_contacts_api.return_value
        mock_contacts_api_instance.get_contact.return_value = MagicMock(result=[MagicMock()])
        id = "ContactsUser1"

        contacts = mock_contacts_api_instance.get_contact(id)

        self.assertIsNotNone(contacts)
        self.assertGreater(len(contacts.result), 0)
        mock_contacts_api_instance.get_contact.assert_called_once()

if __name__ == '__main__':
    unittest.main()