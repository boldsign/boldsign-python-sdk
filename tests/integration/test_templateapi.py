import unittest
from boldsign.api import template_api
from boldsign.models.merge_and_send_for_sign_form import MergeAndSendForSignForm
from boldsign.models.embedded_merge_template_form_request import EmbeddedMergeTemplateFormRequest
from boldsign.models.rectangle import Rectangle
from boldsign.models.role import Role
import pytest
import boldsign
import os
import base64
from boldsign.models.form_field import FormField
from boldsign.rest import ApiException
import time
from config import API_KEY, BASE_URL

@pytest.mark.integration
class TestTemplateApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.created_brand_id = None
        cls.created_template_id = None        
        cls.created_template_id1 = None
        cls.created_template_id_from_field = None
        cls.created_template_id_image_field = None
        cls.created_embedded_template_id = None

    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=API_KEY, host=BASE_URL)
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
        return full_file_name

    def image_to_base64(self, image_path):
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            image_type = image_path.split('.')[-1]
            return f"data:image/{image_type};base64,{encoded_image}"

    @pytest.mark.run(order=68)
    def testTemplateList(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            # Define parameters for listing templates
            page = 1
            template_type = None
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
            assert len(templates.result) >=0
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e is None
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert e is None
        finally:
            time.sleep(5)

    @pytest.mark.run(order=69)
    def testTemplateList_negative(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            page = -1
            template_type = None
            page_size = 0
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

            assert templates is None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=70)
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
            TestTemplateApi.created_brand_id = create_branding_response.brand_id

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=71)
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
                enable_print_and_sign=False,
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

    @pytest.mark.run(order=72)
    def test_edit_template_positive(self):
        self.template_api = boldsign.TemplateApi(self.api_client)
        print (TestTemplateApi.created_template_id)
        role = boldsign.TemplateRole(
            index=1,
            name="Manager",
            defaultSignerName="Alex Gayle",
            defaultSignerEmail="alexgayle@boldsign.dev",
            signerType="Signer",
        )
        
        edit_template_request = boldsign.EditTemplateRequest(
            title="A new title for template",
            enableSigningOrder=False,
            roles=[role]
        )
        
        template_id = TestTemplateApi.created_template_id
        try:
            response = self.template_api.edit_template(template_id=template_id, edit_template_request=edit_template_request)
            assert response is None
        
        except ApiException as e:
            print(f"Exception when calling BoldSign API: {e}")
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print(f"Unexpected exception: {e}")
        finally:
            time.sleep(5)

    @pytest.mark.run(order=73)
    def test_create_template_with_brand_id(self):
        try:
            # Define roles
            roles = [
                boldsign.TemplateRole(
                    index=1,
                    name="Signer",
                    signer_type="Signer",
                    impose_authentication="None",
                    delivery_mode="Email",
                    signer_order=1
                )
            ]

            # Initialize the API client
            self.template_api = boldsign.TemplateApi(self.api_client)

            # Prepare template data with an existing Brand ID
            template_data = boldsign.CreateTemplateRequest(
                title="Duplicate Brand Test",
                document_title="Duplicate Brand",
                description="Testing with an already existing Brand ID.",
                files=["tests/documents/input/doc_1.pdf"],
                roles=roles,
                allow_message_editing=True,
                allow_new_roles=True,
                allow_new_files=True,
                enable_reassign=True,
                enable_print_and_sign=False,
                enable_signing_order=True,
                brand_id=TestTemplateApi.created_brand_id
            )

            # Attempt to create the template
            response = self.template_api.create_template(create_template_request=template_data)
            TestTemplateApi.created_template_id1 = response.template_id

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=74)
    def test_create_template_negative_with_missing_document_title(self):
        try:
            roles = [
                boldsign.TemplateRole(
                    index=1,
                    name="Signer",
                    signer_type="Signer",
                    impose_authentication="None",
                    delivery_mode="Email",
                    signer_order=1
                )
            ]

            self.template_api = boldsign.TemplateApi(self.api_client)

            template_data = boldsign.CreateTemplateRequest(
                title="Valid Template",
                document_title="",
                description="Missing document title.",
                files=["tests/documents/input/doc_1.pdf"],
                roles=roles,
                allow_message_editing=True,
                allow_new_roles=True,
                allow_new_files=True,
                enable_reassign=True,
                enable_print_and_sign=False,
                enable_signing_order=True
            )

            response = self.template_api.create_template(create_template_request=template_data)
            assert False, "Expected ApiException due to missing document title, but the request succeeded."

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert "Document title or document info is required." in e.body
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=75)
    def test_create_template_negative_with_empty_roles(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            template_data = boldsign.CreateTemplateRequest(
                title="New Template",
                document_title="python_test_template",
                description="This is a new template with empty roles.",
                files=["tests/documents/input/doc_1.pdf"],
                roles=[],
                allow_message_editing=True,
                allow_new_roles=True,
                allow_new_files=True,
                enable_reassign=True,
                enable_print_and_sign=False,
                enable_signing_order=True
            )

            response = self.template_api.create_template(create_template_request=template_data)

            assert False, "Expected ApiException due to empty roles, but the request succeeded."

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert "Roles cannot be null or empty." in e.body
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=76)
    def test_create_template_with_multiple_files(self):
        try:
            roles = [
                boldsign.TemplateRole(
                    index=1,
                    name="Signer",
                    signer_type="Signer",
                    impose_authentication="None",
                    delivery_mode="Email",
                    signer_order=1
                )
            ]

            self.template_api = boldsign.TemplateApi(self.api_client)

            template_data = boldsign.CreateTemplateRequest(
                title="New Template",
                document_title="python_test_template",
                description="This is a new template with multiple files.",
                files=[
                    "tests/documents/input/doc_1.pdf",
                    "tests/documents/input/nda-document.pdf",
                    "tests/documents/input/doc_1.pdf",
                    "tests/documents/input/nda-document1.pdf"
                ],
                roles=roles,
                allow_message_editing=True,
                allow_new_roles=True,
                allow_new_files=True,
                enable_reassign=True,
                enable_print_and_sign=False,
                enable_signing_order=True
            )

            response = self.template_api.create_template(create_template_request=template_data)

            assert response is not None
            assert isinstance(response, boldsign.TemplateCreated)
            assert response.template_id is not None

            TestTemplateApi.created_template_id = response.template_id
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")

        except ApiException as e:
            print(f"\nException when calling BoldSign API: {e}")
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print(f"\nUnexpected exception when calling BoldSign: {e}")
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=77)
    def test_create_template_negative_with_empty_title(self):
        try:
            roles = [
                boldsign.TemplateRole(
                    index=1,
                    name="Signer",
                    signer_type="Signer",
                    impose_authentication="None",
                    delivery_mode="Email",
                    signer_order=1
                )
            ]

            self.template_api = boldsign.TemplateApi(self.api_client)

            template_data = boldsign.CreateTemplateRequest(
                title="",
                document_title="python_test_template",
                description="This is a new template with an empty title.",
                files=["tests/documents/input/doc_1.pdf"],
                roles=roles,
                allow_message_editing=True,
                allow_new_roles=True,
                allow_new_files=True,
                enable_reassign=True,
                enable_print_and_sign=False,
                enable_signing_order=True
            )

            response = self.template_api.create_template(create_template_request=template_data)

            assert False, "Expected ApiException due to empty title, but the request succeeded."

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=78)
    def test_edit_template_negative_empty_template_id(self):
        self.template_api = boldsign.TemplateApi(self.api_client)
        
        role = boldsign.TemplateRole(
            index=1,
            name="Manager",
            defaultSignerName="Alex Gayle",
            defaultSignerEmail="alexgayle@boldsign.dev",
            signerType="Signer",
        )
        
        edit_template_request = boldsign.EditTemplateRequest(
            title="A new title for template",
            enableSigningOrder=False,
            roles=[role]
        )
        
        template_id = ""
        try:
            response = self.template_api.edit_template(template_id=template_id, edit_template_request=edit_template_request)
            assert response is None
        
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 403
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=79)
    def test_edit_template_negative_invalid_template_id(self):
        self.template_api = boldsign.TemplateApi(self.api_client)
        
        role = boldsign.TemplateRole(
            index=1,
            name="Manager",
            defaultSignerName="Alex Gayle",
            defaultSignerEmail="alexgayle@boldsign.dev",
            signerType="Signer",
        )
        
        edit_template_request = boldsign.EditTemplateRequest(
            title="A new title for template",
            enableSigningOrder=False,
            roles=[role]
        )
        
        template_id = "invalid_template_id"
        try:
            response = self.template_api.edit_template(template_id=template_id, edit_template_request=edit_template_request)
            assert response is not None
        
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 403
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=80)
    def test_template_properties_integration(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            template_id = TestTemplateApi.created_template_id

            template_properties_response = self.template_api.get_properties(template_id=template_id)

            assert template_properties_response is not None, "Template properties retrieval failed"
            assert hasattr(template_properties_response, 'template_id'), "Response doesn't contain template_id"
            assert template_properties_response.template_id == template_id, f"Expected template ID {template_id}, but got {template_properties_response.template_id}"

        except ApiException as e:
            print(f"Exception when calling BoldSign API: {e}")
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print(f"Unexpected exception: {e}")
        finally:
            time.sleep(5)

    @pytest.mark.run(order=81)
    def test_template_properties_negative_invalid_template_id(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            invalid_template_id = "invalid-template-id-12345"

            template_properties_response = self.template_api.get_properties(template_id=invalid_template_id)

            assert False, "Expected an error for invalid template ID, but the request succeeded."

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=82)
    def test_template_properties_negative_empty_template_id(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            invalid_template_id = ""

            template_properties_response = self.template_api.get_properties(template_id=invalid_template_id)

            assert False, "Expected an error for invalid template ID, but the request succeeded."

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert "The templateId field is required." in e.body
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=83)
    def test_add_tag_to_template(self):
        try:
                self.template_api = boldsign.TemplateApi(self.api_client)

                template_id = TestTemplateApi.created_template_id

                template_tag = boldsign.TemplateTag(
                    templateId=template_id,
                    documentLabels=["test", "api"],
                    templateLabels=["test", "api"]
                )

                response = self.template_api.add_tag(template_tag)

                assert response is None
                print(f"Tag successfully added to template {template_id}")

        except ApiException as e:
            print(f"Exception when calling BoldSign API: {e}")
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print(f"Unexpected exception occurred: {e}")
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=84)
    def test_add_tag_to_template_negative_invalid_templateId(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            invalid_template_id = "INVALID_TEMPLATE_ID"

            template_tag = boldsign.TemplateTag(
                templateId=invalid_template_id,
                documentLabels=["test", "api"],
                templateLabels=["test", "api"]
            )

            response = self.template_api.add_tag(template_tag)

            assert response is not None
            print(f"Tag successfully added to template {invalid_template_id}")

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=85)
    def test_add_tag_to_template_negative_empty_documentLabels_and_templateLabels(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            invalid_template_id = TestTemplateApi.created_template_id

            template_tag = boldsign.TemplateTag(
                templateId=invalid_template_id,
                documentLabels=[],
                templateLabels=[]
            )

            response = self.template_api.add_tag(template_tag)

            assert response is not None
            print(f"Tag successfully added to template {invalid_template_id}")

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert "Template or Document Labels are required." in e.body
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=86)
    def test_delete_tag_to_template(self):
        try:
                self.template_api = boldsign.TemplateApi(self.api_client)

                template_id = TestTemplateApi.created_template_id

                template_tag = boldsign.TemplateTag(
                    templateId=template_id,
                    documentLabels=["test", "api"],
                    templateLabels=["test", "api"]
                )

                response = self.template_api.delete_tag(template_tag)

                assert response is None
                print(f"Tag successfully added to template {template_id}")

        except ApiException as e:
            print(f"Exception when calling BoldSign API: {e}")
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print(f"Unexpected exception occurred: {e}")
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=87)
    def test_delete_tag_to_template_negative_empty_documentLabels_and_templateLabels(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            invalid_template_id = TestTemplateApi.created_template_id

            template_tag = boldsign.TemplateTag(
                templateId=invalid_template_id,
                documentLabels=[],
                templateLabels=[]
            )

            response = self.template_api.delete_tag(template_tag)

            assert response is not None
            print(f"Tag successfully added to template {invalid_template_id}")

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert "Template or Document Labels are required." in e.body
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=88)
    def test_delete_tag_to_template_negative_invalid_templateId(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            invalid_template_id = "INVALID_TEMPLATE_ID"

            template_tag = boldsign.TemplateTag(
                templateId=invalid_template_id,
                documentLabels=["test", "api"],
                templateLabels=["test", "api"]
            )

            response = self.template_api.delete_tag(template_tag)

            assert response is not None
            print(f"Tag successfully added to template {invalid_template_id}")

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=89)
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
                enable_print_and_sign=False,
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

    @pytest.mark.run(order=90)
    def test_create_template_negative_with_form_field_invalid_email(self):
        try:
            roles = [
                boldsign.TemplateRole(
                    index=1,
                    name="Signer",
                    signer_type="Signer",
                    impose_authentication="None",
                    delivery_mode="Email",
                    signer_order=1,
                    defaultSignerEmail="invalid-email",
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
                title="New Template with Invalid Email",
                document_title="python_test_template",
                description="This is a new template with invalid email in form field.",
                files=["tests/documents/input/nda-document.pdf"],
                roles=roles,
                allow_message_editing=True,
                allow_new_roles=True,
                allow_new_files=True,
                enable_reassign=True,
                enable_print_and_sign=False,
                enable_signing_order=True
            )

            response = self.template_api.create_template(create_template_request=template_data)
            assert False, "Expected ApiException due to invalid email format in role."
        
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
            assert e.reason == "Bad Request"
            assert "The field DefaultSignerEmail is invalid." in e.body
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=91)
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
                enable_print_and_sign=False,
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

    @pytest.mark.run(order=92)
    def test_create_template_with_multiple_roles(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
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
                enable_print_and_sign=False,
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
        finally:
            time.sleep(5)

    @pytest.mark.run(order=93)
    def test_create_template_negative_with_duplicate_role_index(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
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
                    index=2,
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
                title="Duplicate Role Index Test",
                document_title="python_test_template_duplicate_index",
                description="Template with duplicate role index.",
                files=["tests/documents/input/nda-document.pdf", "tests/documents/input/nda-document1.pdf"],
                roles=roles,
                allow_message_editing=True,
                allow_new_roles=True,
                allow_new_files=True,
                enable_reassign=True,
                enable_print_and_sign=False,
                enable_signing_order=True
            )

            response = self.template_api.create_template(create_template_request=template_data)
            assert False, "Expected ApiException due to duplicate role index."
        
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
            assert e.reason == "Bad Request"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=94)
    def testTemplateDownload(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
            self.template_api = boldsign.TemplateApi(self.api_client)

            template_id = TestTemplateApi.created_template_id
            on_behalf_of = None

            template_file = self.template_api.download(
                template_id=template_id,
                on_behalf_of=on_behalf_of
            )

            assert template_file is not None
            assert len(template_file) > 0

            filename = f"downloaded_template_{template_id}.pdf"
            full_file_name = self.save_file(filename, template_file)

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

    @pytest.mark.run(order=95)
    def testTemplateDownload_negative(self):
        try:
            invalid_template_id = "invalid-template-id"
            self.template_api = boldsign.TemplateApi(self.api_client)

            on_behalf_of = None

            template_file = self.template_api.download(
                template_id=invalid_template_id,
                on_behalf_of=on_behalf_of
            )

            assert template_file is None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert e.status == 400
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=96)
    def test_send_using_template_best_case(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
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
                        "signerType":"Signer",
                        "authenticationType":"AccessCode",
                        "authenticationCode":"123456",
                        "authenticationSettings":boldsign.AuthenticationSettings(
                            authenticationFrequency="EveryAccess"
                        ),
                        "deliveryMode": "Email",
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

    @pytest.mark.run(order=97)
    def test_send_using_template_with_multiple_cc(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
            self.template_api = boldsign.TemplateApi(self.api_client)
            
            cc_recipients = [
                {"emailAddress": "mohammedmushraf.abuthakir+5@syncfusion.com", "name": "CC User 1"},
                {"emailAddress": "mohammedmushraf.abuthakir+8@syncfusion.com", "name": "CC User 2"},
                {"emailAddress": "mohammedmushraf.abuthakir+9@syncfusion.com", "name": "CC User 3"}
            ]

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
                        "deliveryMode": "Email",
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
                                "bounds": {"x": 100, "y": 100, "width": 200, "height": 200}
                            }
                        ]
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
                "ReminderSettings.ReminderCount": "3",
                "cc": cc_recipients
            }

            response = self.template_api.send_using_template(
                template_id=TestTemplateApi.created_template_id,
                send_for_sign_from_template_form=template_data
            )

            assert response is not None, "Response should not be None"
            assert isinstance(response, boldsign.DocumentCreated), "Response should be of type DocumentCreated"
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

    @pytest.mark.run(order=98)
    def test_send_using_template_worst_case(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
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
            assert e.status == 400
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=99)
    def test_send_document_from_template_with_filePath(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
            self.template_api = boldsign.TemplateApi(self.api_client)
            
            file_path = "tests/documents/input/nda-document.pdf"

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
                        "deliveryMode": "Email",
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
                                "bounds": {"x": 100, "y": 100, "width": 200, "height": 200}
                            }
                        ]
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
                "ReminderSettings.ReminderCount": "3",
                "files": [file_path]
            }

            response = self.template_api.send_using_template(
                template_id=TestTemplateApi.created_template_id,
                send_for_sign_from_template_form=template_data
            )

            assert response is not None, "Response should not be None"
            assert isinstance(response, boldsign.DocumentCreated), "Response should be of type DocumentCreated"
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

    @pytest.mark.run(order=100)
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
                            "number": "6381261236"
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

    @pytest.mark.run(order=101)
    def test_send_using_template_with_invalid_email_and_missing_phone(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)
            template_data = {
                "document_id": TestTemplateApi.created_template_id,
                "title": "Invalid Template",
                "message": "Please sign this document.",
                "roles": [
                    {
                        "roleIndex": 1,
                        "role_name": "Signer",
                        "signer_name": "John Doe",
                        "signer_email": "invalid-email",
                        "phoneNumber": None,
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
                                "bounds": { "x": 100, "y": 100, "width": 200, "height": 200 }
                            }
                        ]
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
            assert False, "Expected ApiException due to invalid email and missing phone number."
        
        except ApiException as e:
            print(f"\nExpected API Exception occurred: {e}")
            assert e.status == 400, "Expected 400 Bad Request."
        except Exception as e:
            print(f"\nUnexpected exception: {e}")
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=102)
    def test_send_using_template_with_existing_form_fields(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id_from_field}")
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

    @pytest.mark.run(order=103)
    def test_send_using_template_with_invalid_formId_existing_form_field_id(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id_from_field}")
            self.template_api = boldsign.TemplateApi(self.api_client)
            
            template_data = {
                "document_id": TestTemplateApi.created_template_id_from_field,
                "title": "Invalid Form Field ID",
                "message": "Please sign this document.",
                "roles": [
                    {
                        "roleIndex": 1,
                        "role_name": "Signer",
                        "signer_name": "John Doe",
                        "signer_email": "john.doe@example.com",
                        "existingFormFields": [
                            {
                                "id": "InvalidFieldID",
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
            assert False, "Expected ApiException due to invalid form field ID."
        
        except ApiException as e:
            print(f"\nExpected API Exception: {e}")
            assert e.status == 400, "Expected 400 Bad Request."
        except Exception as e:
            print(f"\nUnexpected exception: {e}")
            assert False, f"Unexpected exception: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=104)
    def test_send_using_template_with_existing_image_field(self):
        try:
            image_path = "tests/documents/input/logo.png" 
            base64_image = self.image_to_base64(image_path)

            print(f"Using Created Template ID: {TestTemplateApi.created_template_id_image_field}")
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

    @pytest.mark.run(order=105)
    def test_send_using_template_with_invalid_existing_image_field(self):
        try:
            image_path = "tests/documents/input/logo.png"  # Corrected path separator
            base64_image = self.image_to_base64(image_path)

            print(f"Using Created Template ID: {TestTemplateApi.created_template_id_image_field}")
            self.template_api = boldsign.TemplateApi(self.api_client)
            
            # Using an invalid form field ID "InvalidImageID"
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
                                "id": "InvalidImageID",
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

            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
            assert response is not None, "Response should not be None"

        except ApiException as e:
            print(f"\nExpected API Exception when calling BoldSign API: {e}")
            assert e.status == 400
            
        except Exception as e:
            print(f"Unexpected exception when calling BoldSign: {e}")
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=106)
    def test_create_embedded_template(self):
        
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            role = boldsign.TemplateRole(
                index=1,
                name="Manager"
            )

            embedded_create_template_request = boldsign.EmbeddedCreateTemplateRequest(
                files = ["tests/documents/input/doc_1.pdf"],
                title="API template",
                description="API template description",
                document_title="API document title",
                document_message="API document message description",
                allow_message_editing=True,
                roles=[role],
                show_toolbar=True,
                show_navigation_buttons=True,
                show_preview_button=True,
                show_save_button=True,
                allow_new_files=True,
                locale="EN",
                show_tooltip=False,
                view_option="PreparePage"
            )

            response = self.template_api.create_embedded_template_url(embedded_create_template_request)
            TestTemplateApi.created_embedded_template_id = response.template_id
            print(f"Using Created Template ID: {TestTemplateApi.created_embedded_template_id}")

            assert response is not None
            print(f"Embedded Template URL: {response}")

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=107)
    def test_edit_embedded_template_positive(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)
            template_id = TestTemplateApi.created_template_id

            embedded_template_edit_request = boldsign.EmbeddedTemplateEditRequest(
                show_toolbar=True,
                show_navigation_buttons=False,
                show_save_button=False,
                show_preview_button=True,
                show_create_button=False,
                show_tooltip=False
            )

            response = self.template_api.get_embedded_template_edit_url(template_id, embedded_template_edit_request)

            print(f"Embedded Template Edit URL: {response.edit_url}")

            assert response.edit_url is not None
            assert response.edit_url == response.edit_url

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=108)
    def test_create_embedded_template_negative_missing_roles(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            embedded_create_template_request = boldsign.EmbeddedCreateTemplateRequest(
                files=["tests/documents/input/doc_1.pdf"],
                title="API template",
                description="API template description",
                document_title="API document title",
                document_message="API document message description",
                allow_message_editing=True,
                show_toolbar=True,
                show_navigation_buttons=True,
                show_preview_button=True,
                show_save_button=True,
                allow_new_files=True,
                locale="EN",
                show_tooltip=False,
                view_option="PreparePage"
            )

            response = self.template_api.create_embedded_template_url(embedded_create_template_request)
            
            assert response is not None

        except ApiException as e:
            print(f"\nExpected API Exception when calling BoldSign API: {e}")
            assert e.status == 400
            
        except Exception as e:
            print(f"Unexpected exception when calling BoldSign: {e}")
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=109)
    def test_create_embedded_template_negative_invalid_role(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            role = boldsign.TemplateRole(index=1)

            embedded_create_template_request = boldsign.EmbeddedCreateTemplateRequest(
                files=["tests/documents/input/doc_1.pdf"],
                title="API template",
                description="API template description",
                document_title="API document title",
                document_message="API document message description",
                allow_message_editing=True,
                roles=[role],  # Invalid role
                locale="EN",
                show_toolbar=True,
                show_navigation_buttons=True,
                show_preview_button=True,
                show_save_button=True,
            )

            response = self.template_api.create_embedded_template_url(embedded_create_template_request)
            assert response is not None

        except ApiException as e:
            print(f"Expected API Exception: {e}")
            assert e.status == 400

        except Exception as e:
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=110)
    def test_create_embedded_template_request_link(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            template_role = boldsign.TemplateRole(
                index=1,
                name="Manager"
            )

            embedded_create_template_request = boldsign.EmbeddedCreateTemplateRequest(
                title="API template",
                description="API template description",
                document_title="API document title",
                document_message="API document message description",
                allow_message_editing=True,
                roles=[template_role],
                show_toolbar=True,
                show_navigation_buttons=True,
                show_preview_button=True,
                show_send_button=True,
                show_save_button=True,
                locale="EN",
                show_tooltip=False,
                view_option="PreparePage"
            )

            file_path = "tests/documents/input/doc_1.pdf"
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File {file_path} not found")

            embedded_create_template_request.files = [file_path]

            response = self.template_api.create_embedded_template_url(embedded_create_template_request)

            embedded_template_url = response.create_url
            print(f"Embedded Template URL: {embedded_template_url}")

            assert embedded_template_url is not None, "Embedded template URL is None"
            assert isinstance(embedded_template_url, str), "Embedded template URL is not a string"

        except ApiException as e:
                print("\nException when calling BoldSign API: %s" % e)
                assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
                print("\nException when calling BoldSign: %s" % e)
                assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
                time.sleep(5)

    @pytest.mark.run(order=111)
    def test_merge_create_embedded_template_request_url(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)
            file_path = "tests/documents/input/doc_1.pdf"
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            role1 = Role(
                signerEmail="sivaramani.sivaraj@syncfusion.com",
                signerName="sivaramani",
                signerRole="Manager",
                signerOrder=1,
                roleIndex=1,
                signerType="Signer",
                authenticationType="AccessCode",
                authenticationCode="123456",
                authenticationSettings=boldsign.AuthenticationSettings(
                    authenticationFrequency="EveryAccess"
                ),
            )

            request = EmbeddedMergeTemplateFormRequest(
                title="Merged Template Embedded Request",
                roles=[role1],
                files=[file_path],  # Pass the file path as a list
                templateIds=[TestTemplateApi.created_template_id,TestTemplateApi.created_template_id1],
                showToolbar=True,
                showNavigationButtons=True,
                showPreviewButton=True,
                showSaveButton=True,
                locale="EN",
                showTooltip=False,
                sendViewOption="PreparePage"
            )

            response = self.template_api.merge_create_embedded_request_url_template(request)
            embedded_url = response.send_url

            print(f"Embedded Merge Template URL: {embedded_url}")
            self.assertIsNotNone(embedded_url, "Embedded URL should not be None")
            self.assertIsInstance(embedded_url, str, "Embedded URL should be a string")

        except ApiException as e:
            print(f"API Exception occurred: {e}")
            self.fail(f"API Exception: {str(e)}")
        except Exception as e:
            print(f"Unexpected Exception occurred: {e}")
            self.fail(f"Unexpected Exception: {str(e)}")
        finally:
            time.sleep(5)

    @pytest.mark.run(order=112)
    def test_merge_create_embedded_template_request_url_negative(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)
            file_path = "tests/documents/input/doc_1.pdf"
            assert os.path.exists(file_path), f"File not found: {file_path}"

            role1 = Role(
                signerEmail="invalid-email-format",
                signerName="",
                signerRole="Manager",
                signerOrder=1,
                roleIndex=1,
                signerType="Signer"
            )

            request = EmbeddedMergeTemplateFormRequest(
                title="",
                roles=[role1],
                files=[file_path],
                templateIds=["invalid-template-id1", "invalid-template-id2"],
                showToolbar=True,
                showNavigationButtons=True,
                showPreviewButton=True,
                showSaveButton=True,
                locale="EN",
                showTooltip=False,
                sendViewOption="PreparePage"
            )

            response = self.template_api.merge_create_embedded_request_url_template(request)
            assert response is not None

        except ApiException as e:
            print(f"Expected ApiException occurred: {e}")
            assert e.status == 400
        except Exception as e:
            pytest.fail(f"Unexpected Exception occurred: {str(e)}")
        finally:
            time.sleep(5)

    @pytest.mark.run(order=113)
    def test_merge_and_send_using_template_best_case(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
            self.template_api = boldsign.TemplateApi(self.api_client)
            # Create form field with bounds
            form_field = FormField(
                name="textbox",
                field_type="TextBox",
                required=True,
                read_only=False,
                page_number=1,
                value="string",
                font_size=12,
                font="Helvetica",
                language=0,
                locale="EN",
                bounds=Rectangle(x=100, y=100, width=200, height=200)
            )

            # Create role with the form field
            role = Role(
                role_index=1,
                signer_name="John Doe",
                signer_email="john.doe@example.com",
                signer_type="Signer",
                authenticationType="AccessCode",
                authenticationCode="123456",
                authenticationSettings=boldsign.AuthenticationSettings(
                    authenticationFrequency="EveryAccess"
                ),
                signer_role="Signer",
                delivery_mode="Email",
                form_fields=[form_field]
            )

            # Create merge and send form
            merge_and_send_form = MergeAndSendForSignForm(
                title="Sample Template",
                message="Please sign this document.",
                roles=[role],
                template_ids=[TestTemplateApi.created_template_id, TestTemplateApi.created_template_id1],
                labels=["label1", "label2"],
                disable_emails=False,
                disable_sms=False,
                hide_document_id=False,
                expiry_days=30,
                expiry_date_type="Days",
                expiry_value=60,
                enable_print_and_sign=True,
                enable_reassign=True,
                enable_signing_order=True,
                use_text_tags=False,
                text_tag_definitions=[],
                document_info=[],
                on_behalf_of=None,
                is_sandbox=False,
                role_removal_indices=[],
                document_download_option="Combined",
                recipient_notification_settings=None,
                reminder_settings={
                    "EnableAutoReminder": True,
                    "ReminderDays": "4",
                    "ReminderCount": "3"
                }
            )

            # Call the merge and send endpoint
            response = self.template_api.merge_and_send(merge_and_send_form)

            assert response is not None

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nUnexpected exception when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=114)
    def test_delete_template_positive(self):
        try:
            print(f"Using Created Template ID: {TestTemplateApi.created_template_id}")
            self.template_api = boldsign.TemplateApi(self.api_client)
            template_id = TestTemplateApi.created_template_id
            self.template_api.delete_template(template_id=template_id)
        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(5)

    @pytest.mark.run(order=115)
    def test_delete_template_negative(self):
        try:
            self.template_api = boldsign.TemplateApi(self.api_client)

            non_existent_template_id = "non-existent-templateId"
            with self.assertRaises(ApiException) as context:
                self.template_api.delete_template(template_id=non_existent_template_id)
            self.assertEqual(context.exception.status, 400)

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