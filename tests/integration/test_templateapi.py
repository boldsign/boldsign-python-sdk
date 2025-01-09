import unittest
import pytest
import boldsign
import os
import base64
from boldsign.rest import ApiException
import time

APIKey = os.getenv('BoldSignAPIKey')
url = os.getenv('BoldSignURL')

@pytest.mark.integration
class TestTemplateApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.created_template_id = None        
        cls.created_template_id_from_field = None
        cls.created_template_id_image_field = None
    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=APIKey, host=url)
        self.api_client = boldsign.ApiClient(self.configuration)

    def pdf_to_base64(self, pdf_file_path):
        pdf_file_path = "tests/documents/input/" + pdf_file_path
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_content = pdf_file.read()
            base64_content = "data:application/pdf;base64," + base64.b64encode(pdf_content).decode('utf-8')
        return base64_content

    def save_file(self, file_name, file_content):
        newpath = r"tests/documents/output/"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        full_file_name = "tests/documents/output/" + file_name
        with open(full_file_name, "wb") as file:
            file.write(file_content)
        return full_file_name  # Return the full file name    

    def image_to_base64(self, image_path):
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            image_type = image_path.split('.')[-1]  # Extract the image type from the file extension
            return f"data:image/{image_type};base64,{encoded_image}"

    @pytest.mark.run(order=41)
    def testTemplateList(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            # Define parameters for listing templates
            page = 1
            template_type = None  # Example: 'mytemplates', 'sharedtemplates', 'alltemplates'
            page_size = 10
            search_key = None
            on_behalf_of = None
            created_by = None
            template_labels = None   
            start_date = None
            end_date = None

            templates = self.template_api.list_templates(
                page=page,
                template_type=template_type,
                page_size=page_size,
                search_key=search_key,
                on_behalf_of=on_behalf_of,
                created_by=created_by,
                template_labels=template_labels,
                start_date=start_date,
                end_date=end_date
            )
            assert templates is not None
            assert len(templates.result) > 0
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert e is None  # make the test case fail in case of an API exception    
   
    @pytest.mark.run(order=42)
    def test_create_template_positive(self):
        try:
            roles = [
                boldsign.TemplateRole(
                    index = 1,
                    name="Signer",
                    signer_type="Signer",
                    impose_authentication="None",
                    delivery_mode="Email",
                    signer_order = 1
                )
            ]

            self.template_api = boldsign.TemplateApi(self.api_client)
            template_data = boldsign.CreateTemplateRequest(
                title="New Template",
                document_title = "python_test_template",
                description="This is a new template.",
                files=["tests/documents/input/doc_1.pdf"],
                roles=roles,
                allow_message_editing=True,
                allow_new_roles=True,
                allow_new_files=True,
                enable_reassign=True,
                enable_print_and_assign=False,
                enable_signing_order=True
            )

            response = self.template_api.create_template(create_template_request=template_data)
            assert response is not None
            assert isinstance(response, boldsign.TemplateCreated)
            assert response.template_id is not None
            TestTemplateApi.created_template_id = response.template_id
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)             
   
    @pytest.mark.run(order=42)
    def test_create_template_with_form_field(self):
        try:
            roles = [
                boldsign.TemplateRole(
                    index = 1,
                    name="Signer",
                    signer_type="Signer",
                    impose_authentication="None",
                    delivery_mode="Email",
                    signer_order = 1,
                    defaultSignerEmail="john.doe@example.com",
                    defaultSignerName="John Doe",
                    formFields=[
                        boldsign.FormField(
                                name="Sign",
                                id="State",
                                fieldType="TextBox",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                        )
                        ]
                )
            ]

            self.template_api = boldsign.TemplateApi(self.api_client)
            template_data = boldsign.CreateTemplateRequest(
                title="New Template",
                document_title = "python_test_template",
                description="This is a new template.",
                files=["tests/documents/input/nda-document.pdf"],
                roles=roles,
                allow_message_editing=True,
                allow_new_roles=True,
                allow_new_files=True,
                enable_reassign=True,
                enable_print_and_assign=False,
                enable_signing_order=True
            )

            response = self.template_api.create_template(create_template_request=template_data)
            assert response is not None
            assert isinstance(response, boldsign.TemplateCreated)
            assert response.template_id is not None
            TestTemplateApi.created_template_id_from_field = response.template_id
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)             
   
    @pytest.mark.run(order=43)
    def test_create_template_with_image_field(self):
        try:
            roles = [
                boldsign.TemplateRole(
                    index = 1,
                    name="Signer",
                    signer_type="Signer",
                    impose_authentication="None",
                    delivery_mode="Email",
                    signer_order = 1,
                    defaultSignerEmail="john.doe@example.com",
                    defaultSignerName="John Doe",
                    formFields=[
                        boldsign.FormField(
                                name="image",
                                id="Image1",
                                fieldType="Image",
                                font="Helvetica",
                                pageNumber=1,
                                isRequired=True,
                                imageInfo=boldsign.ImageInfo(
                                   title="Image Test",
                                   allowedFileExtensions=".png",
                                   description="Image for testing"
                                ),
                                bounds=boldsign.Rectangle(x=50, y=50, width=100, height=150)
                        )
                        ]
                )
            ]

            self.template_api = boldsign.TemplateApi(self.api_client)
            template_data = boldsign.CreateTemplateRequest(
                title="New Template",
                document_title = "python_test_template",
                description="This is a new template.",
                files=["tests/documents/input/nda-document.pdf"],
                roles=roles,
                allow_message_editing=True,
                allow_new_roles=True,
                allow_new_files=True,
                enable_reassign=True,
                enable_print_and_assign=False,
                enable_signing_order=True
            )

            response = self.template_api.create_template(create_template_request=template_data)
            assert response is not None
            assert isinstance(response, boldsign.TemplateCreated)
            assert response.template_id is not None
            TestTemplateApi.created_template_id_image_field = response.template_id
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id_image_field}")
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(10) 

    @pytest.mark.run(order=44)
    def test_create_template_with_multiple_roles(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")  # Debug print
            roles = [
                boldsign.TemplateRole(
                    index=1,
                    name="Signer1",
                    signer_type="Signer",
                    impose_authentication="EmailOTP",
                    delivery_mode="Email",
                    signer_order=1,
                    locale="EN",
                    allow_field_configuration=True,
                    allow_role_edit=True,
                    allow_role_delete=True
                ),
                boldsign.TemplateRole(
                    index=2,
                    name="Reviewer1",
                    signer_type="Reviewer",
                    impose_authentication="None",
                    delivery_mode="Email",
                    signer_order=2,
                    locale="EN",
                    allow_field_configuration=False,
                    allow_role_edit=True,
                    allow_role_delete=True
                ),
                boldsign.TemplateRole(
                    index=3,
                    name="InPersonSigner1",
                    signer_type="Reviewer",
                    impose_authentication="AccessCode",
                    delivery_mode="Email",
                    signer_order=3,
                    locale="EN",
                    allow_field_configuration=False,
                    allow_role_edit=True,
                    allow_role_delete=True
                )
            ]

            self.template_api = boldsign.TemplateApi(self.api_client)
            template_data = boldsign.CreateTemplateRequest(
                title="New Template with Multiple Roles",
                document_title="python_test_template_multiple_roles",
                description="This is a new template with multiple roles.",
                files=["tests/documents/input/nda-document.pdf", "tests/documents/input/nda-document1.pdf"],
                roles=roles,
                allow_message_editing=True,
                allow_new_roles=True,
                allow_new_files=True,
                enable_reassign=True,
                enable_print_and_assign=False,
                enable_signing_order=True
            )

            response = self.template_api.create_template(create_template_request=template_data)
            assert response is not None
            assert isinstance(response, boldsign.TemplateCreated)
            assert response.template_id is not None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

   
    @pytest.mark.run(order=45)
    def testTemplateDownload(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")  # Debug print
            self.template_api = boldsign.TemplateApi(self.api_client)

            # Define parameters for template download
            template_id = TestTemplateApi.created_template_id  # Replace with a valid template ID
            on_behalf_of = None

            # Download the template
            template_file = self.template_api.download(
                template_id=template_id,
                on_behalf_of=on_behalf_of
            )

            assert template_file is not None
            assert len(template_file) > 0  # Ensure the downloaded file is not empty

            # Save the downloaded file to disk for verification
            filename = f"downloaded_template_{template_id}.pdf"
            full_file_name = self.save_file(filename, template_file)

            # Assert that the file was created and is not empty
            assert os.path.exists(full_file_name)
            assert os.path.getsize(full_file_name) > 0

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

 
    @pytest.mark.run(order=46)
    def test_send_using_template_best_case(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")  # Debug print
            self.template_api = boldsign.TemplateApi(self.api_client)
            template_data = {
                "document_id": TestTemplateApi.created_template_id,
                "title": "Sample Template",
                "message": "Please sign this document.",
                "roles": [
                    {
                        "roleIndex": 1,
                        "role_name": "Signer",
                        "signer_name": "John Doe",
                        "signer_email": "john.doe@example.com",
                        "form_fields": [
                        {
                            "name": "textbox",
                            "field_type": "TextBox",
                            "required": True,
                            "read_only": False,
                            "page_number": 1,
                            "value": "string",
                            "font_size": 12,
                            "font": "Helvetica",
                            "language": 0,
                            "locale": "EN",
                            "bounds": { "x":100, "y":100, "width":200, "height":200 }
                        }]
                    }
                ],
                "labels": ["label1", "label2"],
                "disable_emails": False,
                "disable_sms": False,
                "hide_document_id": False,
                "expiry_days": 30,
                "expiry_date_type": "Days",
                "expiry_value": 60,
                "enable_print_and_sign": True,
                "enable_reassign": True,
                "enable_signing_order": True,
                "use_text_tags": False,
                "text_tag_definitions": [],
                "document_info": [],
                "on_behalf_of": None,
                "is_sandbox": False,
                "role_removal_indices": [],
                "document_download_option": "Combined",
                "recipient_notification_settings": None,
                "ReminderSettings.EnableAutoReminder": True,
                "ReminderSettings.ReminderDays": "4",
                "ReminderSettings.ReminderCount": "3"
            }

            response = self.template_api.send_using_template(
                template_id=TestTemplateApi.created_template_id,
                send_for_sign_from_template_form=template_data
            )
            assert response is not None, "Response should not be None"
            assert isinstance(response, boldsign.DocumentCreated),"Response should be of type DocumentCreated"
            assert hasattr(response, 'document_id'), "Response should have a document_id attribute"
            assert response.document_id is not None, "Document ID should not be None"
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.integration
    @pytest.mark.run(order=47)
    def test_send_using_template_worst_case(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")  # Debug print
            self.template_api = boldsign.TemplateApi(self.api_client)
            template_data = {
                "document_id": "",
                "title": "",
                "message": "",
                "roles": [
                    {
                        "role_name": "",
                        "signer_name": "",
                        "signer_email": ""
                    }
                ],
                "brand_id": "",
                "labels": [],
                "disable_emails": True,
                "disable_sms": True,
                "hide_document_id": True,
                "expiry_days": 3,
                "expiry_date_type": "Days",
                "expiry_value": -1,
                "enable_print_and_sign": False,
                "enable_reassign": False,
                "enable_signing_order": False,
                "use_text_tags": True,
                "text_tag_definitions": [],
                "document_info": [],
                "on_behalf_of": None,
                "is_sandbox": True,
                "role_removal_indices": [],
                "document_download_option": "Combined",
                "recipient_notification_settings": None,
            }

            response = self.template_api.send_using_template(
                template_id="",
                send_for_sign_from_template_form=template_data
            )
            assert response is None  # Expecting failure
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400  # Assuming 400 Bad Request for invalid input
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
 
    #How to request signature by email and SMS when sending document from template?
    @pytest.mark.run(order=48)
    def test_send_using_template_with_email_and_SMS(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)
            template_data = {
                "document_id": TestTemplateApi.created_template_id,
                "title": "Sample Template",
                "message": "Please sign this document.",
                "roles": [
                    {
                        "roleIndex": 1,
                        "role_name": "Signer",
                        "signer_name": "John Doe",
                        "signer_email": "john.doe@example.com",
                        "phoneNumber": {
                            "countryCode": "+91",
                            "number": "9876543210"
                            },
                        "deliveryMode": "EmailAndSMS",
                        "form_fields": [
                        {
                            "name": "textbox",
                            "field_type": "TextBox",
                            "required": True,
                            "read_only": False,
                            "page_number": 1,
                            "value": "string",
                            "font_size": 12,
                            "font": "Helvetica",
                            "language": 0,
                            "locale": "EN",
                            "bounds": { "x":100, "y":100, "width":200, "height":200 }
                        }]
                    }
                ],
                "labels": ["label1", "label2"],
                "disable_emails": False,
                "disable_sms": False,
                "hide_document_id": False,
                "expiry_days": 30,
                "expiry_date_type": "Days",
                "expiry_value": 60,
                "enable_print_and_sign": True,
                "enable_reassign": True,
                "enable_signing_order": True,
                "use_text_tags": False,
                "text_tag_definitions": [],
                "document_info": [],
                "on_behalf_of": None,
                "is_sandbox": False,
                "role_removal_indices": [],
                "document_download_option": "Combined",
                "recipient_notification_settings": None,
            }

            response = self.template_api.send_using_template(
                template_id=TestTemplateApi.created_template_id,
                send_for_sign_from_template_form=template_data
            )
            assert response is not None, "Response should not be None"
            assert isinstance(response, boldsign.DocumentCreated),"Response should be of type DocumentCreated"
            assert hasattr(response, 'document_id'), "Response should have a document_id attribute"
            assert response.document_id is not None, "Document ID should not be None"
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5) 
   
    @pytest.mark.run(order=49)
    def test_send_using_template_with_existing_form_fields(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id_from_field}")  # Debug print
            self.template_api = boldsign.TemplateApi(self.api_client)
            template_data = {
                "document_id": TestTemplateApi.created_template_id_from_field,
                "title": "Sample Template",
                "message": "Please sign this document.",
                "roles": [
                    {
                        "roleIndex": 1,
                        "role_name": "Signer",
                        "signer_name": "John Doe",
                        "signer_email": "john.doe@example.com",
                        "existingFormFields": [
                            {
                                "id": "State",
                                "value": "North Carolina"
                            }
                        ]
                    }
                ]
            }

            response = self.template_api.send_using_template(
                template_id=TestTemplateApi.created_template_id_from_field,
                send_for_sign_from_template_form=template_data
            )
            assert response is not None, "Response should not be None"
            assert isinstance(response, boldsign.DocumentCreated),"Response should be of type DocumentCreated"
            assert hasattr(response, 'document_id'), "Response should have a document_id attribute"
            assert response.document_id is not None, "Document ID should not be None"
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

 
    #How to prefill values for image field while sending document from template for signature?
    @pytest.mark.run(order=50)
    def test_send_using_template_with_existing_image_field(self):
        try:
            image_path = "tests\documents\input\logo.png" 
            base64_image = self.image_to_base64(image_path)

            print(f"Using Created Template ID: {TestTemplateApi.created_template_id_image_field}")  # Debug print
            self.template_api = boldsign.TemplateApi(self.api_client)
            template_data = {
                "document_id": TestTemplateApi.created_template_id_image_field,
                "title": "Sample Template",
                "message": "Please sign this document.",
                "roles": [
                    {
                        "roleIndex": 1,
                        "role_name": "Signer",
                        "signer_name": "John Doe",
                        "signer_email": "john.doe@example.com",
                        "existingFormFields": [
                            {
                                "id": "Image1",
                                "value": base64_image
                            }
                        ]
                    }
                ]
            }

            response = self.template_api.send_using_template(
                template_id=TestTemplateApi.created_template_id_image_field,
                send_for_sign_from_template_form=template_data
            )
            assert response is not None, "Response should not be None"
            assert isinstance(response, boldsign.DocumentCreated),"Response should be of type DocumentCreated"
            assert hasattr(response, 'document_id'), "Response should have a document_id attribute"
            assert response.document_id is not None, "Document ID should not be None"
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=51)
    def test_delete_template_positive(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")  # Debug print
            self.template_api = boldsign.TemplateApi(self.api_client)
            template_id = TestTemplateApi.created_template_id
            # Delete the template
            self.template_api.delete_template(template_id=template_id)
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=52)
    def test_delete_template_negative(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)
            
            # Attempt to delete a non-existent template
            non_existent_template_id = "non-existent-template-id"
            with self.assertRaises(ApiException) as context:
                self.template_api.delete_template(template_id=non_existent_template_id)
            self.assertEqual(context.exception.status, 400)
        
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"

if __name__ == '__main__':
    unittest.main()