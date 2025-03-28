# coding: utf-8

# flake8: noqa
"""
    BoldSign API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Contact: support@boldsign.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from boldsign.models.access_code_detail import AccessCodeDetail
from boldsign.models.access_code_details import AccessCodeDetails
from boldsign.models.attachment_info import AttachmentInfo
from boldsign.models.audit_trail import AuditTrail
from boldsign.models.base64_file import Base64File
from boldsign.models.behalf_document import BehalfDocument
from boldsign.models.behalf_document_records import BehalfDocumentRecords
from boldsign.models.behalf_of import BehalfOf
from boldsign.models.billing_view_model import BillingViewModel
from boldsign.models.brand_created import BrandCreated
from boldsign.models.brand_custom_field_details import BrandCustomFieldDetails
from boldsign.models.branding_message import BrandingMessage
from boldsign.models.branding_records import BrandingRecords
from boldsign.models.change_recipient import ChangeRecipient
from boldsign.models.conditional_rule import ConditionalRule
from boldsign.models.contact_created import ContactCreated
from boldsign.models.contact_details import ContactDetails
from boldsign.models.contact_page_details import ContactPageDetails
from boldsign.models.contacts_details import ContactsDetails
from boldsign.models.contacts_list import ContactsList
from boldsign.models.create_contact_response import CreateContactResponse
from boldsign.models.create_sender_identity_request import CreateSenderIdentityRequest
from boldsign.models.create_team_request import CreateTeamRequest
from boldsign.models.create_template_request import CreateTemplateRequest
from boldsign.models.create_user import CreateUser
from boldsign.models.custom_domain_settings import CustomDomainSettings
from boldsign.models.custom_field_collection import CustomFieldCollection
from boldsign.models.custom_field_message import CustomFieldMessage
from boldsign.models.custom_form_field import CustomFormField
from boldsign.models.delete_custom_field_reply import DeleteCustomFieldReply
from boldsign.models.document import Document
from boldsign.models.document_cc import DocumentCC
from boldsign.models.document_cc_details import DocumentCcDetails
from boldsign.models.document_created import DocumentCreated
from boldsign.models.document_expiry_settings import DocumentExpirySettings
from boldsign.models.document_files import DocumentFiles
from boldsign.models.document_form_fields import DocumentFormFields
from boldsign.models.document_info import DocumentInfo
from boldsign.models.document_properties import DocumentProperties
from boldsign.models.document_reassign import DocumentReassign
from boldsign.models.document_records import DocumentRecords
from boldsign.models.document_sender_detail import DocumentSenderDetail
from boldsign.models.document_signer import DocumentSigner
from boldsign.models.document_signer_details import DocumentSignerDetails
from boldsign.models.document_tags import DocumentTags
from boldsign.models.edit_sender_identity_request import EditSenderIdentityRequest
from boldsign.models.edit_template_request import EditTemplateRequest
from boldsign.models.editable_date_field_settings import EditableDateFieldSettings
from boldsign.models.embedded_create_template_request import EmbeddedCreateTemplateRequest
from boldsign.models.embedded_custom_field_created import EmbeddedCustomFieldCreated
from boldsign.models.embedded_document_request import EmbeddedDocumentRequest
from boldsign.models.embedded_send_created import EmbeddedSendCreated
from boldsign.models.embedded_send_template_form_request import EmbeddedSendTemplateFormRequest
from boldsign.models.embedded_signing_link import EmbeddedSigningLink
from boldsign.models.embedded_template_created import EmbeddedTemplateCreated
from boldsign.models.embedded_template_edit_request import EmbeddedTemplateEditRequest
from boldsign.models.embedded_template_edited import EmbeddedTemplateEdited
from boldsign.models.error_result import ErrorResult
from boldsign.models.existing_form_field import ExistingFormField
from boldsign.models.extend_expiry import ExtendExpiry
from boldsign.models.file_info import FileInfo
from boldsign.models.font import Font
from boldsign.models.form_field import FormField
from boldsign.models.form_group import FormGroup
from boldsign.models.formula_field_settings import FormulaFieldSettings
from boldsign.models.id_verification import IdVerification
from boldsign.models.identity_verification_settings import IdentityVerificationSettings
from boldsign.models.image_info import ImageInfo
from boldsign.models.merge_and_send_for_sign_form import MergeAndSendForSignForm
from boldsign.models.notification_settings import NotificationSettings
from boldsign.models.page_details import PageDetails
from boldsign.models.phone_number import PhoneNumber
from boldsign.models.prefill_field import PrefillField
from boldsign.models.prefill_field_request import PrefillFieldRequest
from boldsign.models.recipient_notification_settings import RecipientNotificationSettings
from boldsign.models.rectangle import Rectangle
from boldsign.models.reminder_message import ReminderMessage
from boldsign.models.reminder_settings import ReminderSettings
from boldsign.models.remove_authentication import RemoveAuthentication
from boldsign.models.revoke_document import RevokeDocument
from boldsign.models.role import Role
from boldsign.models.roles import Roles
from boldsign.models.send_for_sign import SendForSign
from boldsign.models.send_for_sign_from_template_form import SendForSignFromTemplateForm
from boldsign.models.sender_identity_list import SenderIdentityList
from boldsign.models.sender_identity_view_model import SenderIdentityViewModel
from boldsign.models.size import Size
from boldsign.models.team_created import TeamCreated
from boldsign.models.team_document_records import TeamDocumentRecords
from boldsign.models.team_list_response import TeamListResponse
from boldsign.models.team_page_details import TeamPageDetails
from boldsign.models.team_response import TeamResponse
from boldsign.models.team_update_request import TeamUpdateRequest
from boldsign.models.team_users import TeamUsers
from boldsign.models.teams import Teams
from boldsign.models.template import Template
from boldsign.models.template_cc import TemplateCC
from boldsign.models.template_created import TemplateCreated
from boldsign.models.template_form_fields import TemplateFormFields
from boldsign.models.template_properties import TemplateProperties
from boldsign.models.template_records import TemplateRecords
from boldsign.models.template_role import TemplateRole
from boldsign.models.template_sender_detail import TemplateSenderDetail
from boldsign.models.template_sender_details import TemplateSenderDetails
from boldsign.models.template_shared_template_detail import TemplateSharedTemplateDetail
from boldsign.models.template_signer_details import TemplateSignerDetails
from boldsign.models.template_tag import TemplateTag
from boldsign.models.text_tag_definition import TextTagDefinition
from boldsign.models.text_tag_offset import TextTagOffset
from boldsign.models.update_user import UpdateUser
from boldsign.models.user_page_details import UserPageDetails
from boldsign.models.user_properties import UserProperties
from boldsign.models.user_records import UserRecords
from boldsign.models.users_details import UsersDetails
from boldsign.models.validation import Validation
from boldsign.models.view_brand_details import ViewBrandDetails
from boldsign.models.view_custom_field_details import ViewCustomFieldDetails
