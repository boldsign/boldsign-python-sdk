# BoldSign

Easily integrate BoldSign's e-signature features into your Python applications. This package simplifies sending documents for signature, embedding signing ceremonies, tracking document status, downloading signed documents, and managing e-signature workflows.

## Prerequisites

- Python 3.7+
- Free [developer account](https://boldsign.com/esignature-api/)

## Documentation

- [Official API documentation](https://developers.boldsign.com/)

## Installation & Usage

You can install this package by using the pip tool: 
```sh
pip install boldsign
```
(You may need to run pip with root permission: sudo pip install boldsign)

Then import the package:
```python
import boldsign
```

## Dependencies

This package requires the following dependencies to function properly. They will be installed automatically when you install the package:
 
- urllib3>=1.25.3 
- python-dateutil 
- pydantic>=2 
- typing-extensions>=4.7.1 

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import boldsign

configuration = boldsign.Configuration(
    api_key = "***your_api_key***"
)

# Enter a context with an instance of the API client
with boldsign.ApiClient(configuration) as api_client:
    # Create an instance of the DocumentApi class
    document_api = boldsign.DocumentApi(api_client)

    # Define the signature field to be added to the document
    signatureField = boldsign.FormField(
        fieldType="Signature",  # Field type is Signature
        pageNumber=1,  # Specify the page number
        bounds=boldsign.Rectangle(x=100, y=100, width=100, height=50),  # Position and size of the signature field
    )

    # Define the signer with a name and email address
    signer = boldsign.DocumentSigner(
        name="David",  # Name of the signer
        emailAddress="david@example.com",  # Signer's email address
        signerType="Signer",  # Specify the signer type
        formFields=[signatureField]  # Assign the signature field to the signer
    )

    # Prepare the request body for sending the document for signature
    send_for_sign = boldsign.SendForSign(
        title="Agreement",  # Title of the document
        signers=[signer],  # List of signers
        files=["/documents/agreement.pdf"]  # Path to the document file to be signed
    )
    
    # Send the document for signature and capture the response
    api_response = document_api.send_document(send_for_sign=send_for_sign)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.boldsign.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrandingApi* | [**brand_list**](docs/BrandingApi.md#brand_list) | **GET** /v1/brand/list | List all the brands.
*BrandingApi* | [**create_brand**](docs/BrandingApi.md#create_brand) | **POST** /v1/brand/create | Create the brand.
*BrandingApi* | [**delete_brand**](docs/BrandingApi.md#delete_brand) | **DELETE** /v1/brand/delete | Delete the brand.
*BrandingApi* | [**edit_brand**](docs/BrandingApi.md#edit_brand) | **POST** /v1/brand/edit | Edit the brand.
*BrandingApi* | [**get_brand**](docs/BrandingApi.md#get_brand) | **GET** /v1/brand/get | Get the specific brand details.
*BrandingApi* | [**reset_default_brand**](docs/BrandingApi.md#reset_default_brand) | **POST** /v1/brand/resetdefault | Reset default brand.
*ContactsApi* | [**contact_user_list**](docs/ContactsApi.md#contact_user_list) | **GET** /v1/contacts/list | List Contact document.
*ContactsApi* | [**create_contact**](docs/ContactsApi.md#create_contact) | **POST** /v1/contacts/create | Create the new Contact.
*ContactsApi* | [**delete_contacts**](docs/ContactsApi.md#delete_contacts) | **DELETE** /v1/contacts/delete | Deletes a contact.
*ContactsApi* | [**get_contact**](docs/ContactsApi.md#get_contact) | **GET** /v1/contacts/get | Get summary of the contact.
*ContactsApi* | [**update_contact**](docs/ContactsApi.md#update_contact) | **PUT** /v1/contacts/update | Update the contact.
*CustomFieldApi* | [**create_custom_field**](docs/CustomFieldApi.md#create_custom_field) | **POST** /v1/customField/create | Create the custom field.
*CustomFieldApi* | [**custom_fields_list**](docs/CustomFieldApi.md#custom_fields_list) | **GET** /v1/customField/list | List the custom fields respective to the brand id.
*CustomFieldApi* | [**delete_custom_field**](docs/CustomFieldApi.md#delete_custom_field) | **DELETE** /v1/customField/delete | Delete the custom field.
*CustomFieldApi* | [**edit_custom_field**](docs/CustomFieldApi.md#edit_custom_field) | **POST** /v1/customField/edit | Edit the custom field.
*CustomFieldApi* | [**embed_custom_field**](docs/CustomFieldApi.md#embed_custom_field) | **POST** /v1/customField/createEmbeddedCustomFieldUrl | Generates a URL for creating or modifying custom fields within your application&#39;s embedded Designer.
*DocumentApi* | [**add_authentication**](docs/DocumentApi.md#add_authentication) | **PATCH** /v1/document/addAuthentication | The add authentication to recipient.
*DocumentApi* | [**add_tag**](docs/DocumentApi.md#add_tag) | **PATCH** /v1/document/addTags | Add the Tags in Documents.
*DocumentApi* | [**behalf_documents**](docs/DocumentApi.md#behalf_documents) | **GET** /v1/document/behalfList | Gets the behalf documents.
*DocumentApi* | [**change_access_code**](docs/DocumentApi.md#change_access_code) | **PATCH** /v1/document/changeAccessCode | Changes the access code for the given document signer.
*DocumentApi* | [**change_recipient**](docs/DocumentApi.md#change_recipient) | **PATCH** /v1/document/changeRecipient | Change recipient details of a document.
*DocumentApi* | [**create_embedded_request_url_document**](docs/DocumentApi.md#create_embedded_request_url_document) | **POST** /v1/document/createEmbeddedRequestUrl | Generates a send URL which embeds document sending process into your application.
*DocumentApi* | [**delete_document**](docs/DocumentApi.md#delete_document) | **DELETE** /v1/document/delete | Delete the document.
*DocumentApi* | [**delete_tag**](docs/DocumentApi.md#delete_tag) | **DELETE** /v1/document/deleteTags | Delete the Tags in Documents.
*DocumentApi* | [**download_attachment**](docs/DocumentApi.md#download_attachment) | **GET** /v1/document/downloadAttachment | Download the Attachment.
*DocumentApi* | [**download_audit_log**](docs/DocumentApi.md#download_audit_log) | **GET** /v1/document/downloadAuditLog | Download the audit trail document.
*DocumentApi* | [**download_document**](docs/DocumentApi.md#download_document) | **GET** /v1/document/download | Download the document.
*DocumentApi* | [**extend_expiry**](docs/DocumentApi.md#extend_expiry) | **PATCH** /v1/document/extendExpiry | Extends the expiration date of the document.
*DocumentApi* | [**get_embedded_sign_link**](docs/DocumentApi.md#get_embedded_sign_link) | **GET** /v1/document/getEmbeddedSignLink | Get sign link for Embedded Sign.
*DocumentApi* | [**get_properties**](docs/DocumentApi.md#get_properties) | **GET** /v1/document/properties | Get summary of the document.
*DocumentApi* | [**list_documents**](docs/DocumentApi.md#list_documents) | **GET** /v1/document/list | List user documents.
*DocumentApi* | [**prefill_fields**](docs/DocumentApi.md#prefill_fields) | **PATCH** /v1/document/prefillFields | Updates the value (prefill) of the fields in the document.
*DocumentApi* | [**remind_document**](docs/DocumentApi.md#remind_document) | **POST** /v1/document/remind | Send reminder to pending signers.
*DocumentApi* | [**remove_authentication**](docs/DocumentApi.md#remove_authentication) | **PATCH** /v1/document/RemoveAuthentication | Remove the access code for the given document signer.
*DocumentApi* | [**revoke_document**](docs/DocumentApi.md#revoke_document) | **POST** /v1/document/revoke | Revoke the document.
*DocumentApi* | [**send_document**](docs/DocumentApi.md#send_document) | **POST** /v1/document/send | Sends the document for sign.
*DocumentApi* | [**team_documents**](docs/DocumentApi.md#team_documents) | **GET** /v1/document/teamlist | Get user Team documents.
*PlanApi* | [**api_credits_count**](docs/PlanApi.md#api_credits_count) | **GET** /v1/plan/apiCreditsCount | Gets the Api credits details.
*SenderIdentitiesApi* | [**create_sender_identities**](docs/SenderIdentitiesApi.md#create_sender_identities) | **POST** /v1/senderIdentities/create | Creates sender identity.
*SenderIdentitiesApi* | [**delete_sender_identities**](docs/SenderIdentitiesApi.md#delete_sender_identities) | **DELETE** /v1/senderIdentities/delete | Deletes sender identity.
*SenderIdentitiesApi* | [**list_sender_identities**](docs/SenderIdentitiesApi.md#list_sender_identities) | **GET** /v1/senderIdentities/list | Lists sender identity.
*SenderIdentitiesApi* | [**re_request_sender_identities**](docs/SenderIdentitiesApi.md#re_request_sender_identities) | **POST** /v1/senderIdentities/rerequest | Rerequests denied sender identity.
*SenderIdentitiesApi* | [**resend_invitation_sender_identities**](docs/SenderIdentitiesApi.md#resend_invitation_sender_identities) | **POST** /v1/senderIdentities/resendInvitation | Resends sender identity invitation.
*SenderIdentitiesApi* | [**update_sender_identities**](docs/SenderIdentitiesApi.md#update_sender_identities) | **POST** /v1/senderIdentities/update | Updates sender identity.
*TeamsApi* | [**create_team**](docs/TeamsApi.md#create_team) | **POST** /v1/teams/create | Create Team.
*TeamsApi* | [**get_team**](docs/TeamsApi.md#get_team) | **GET** /v1/teams/get | Get Team details.
*TeamsApi* | [**list_teams**](docs/TeamsApi.md#list_teams) | **GET** /v1/teams/list | List Teams.
*TeamsApi* | [**update_team**](docs/TeamsApi.md#update_team) | **PUT** /v1/teams/update | Update Team.
*TemplateApi* | [**add_tag**](docs/TemplateApi.md#add_tag) | **PATCH** /v1/template/addTags | Add the Tags in Templates.
*TemplateApi* | [**create_embedded_request_url_template**](docs/TemplateApi.md#create_embedded_request_url_template) | **POST** /v1/template/createEmbeddedRequestUrl | Generates a send URL using a template which embeds document sending process into your application.
*TemplateApi* | [**create_embedded_template_url**](docs/TemplateApi.md#create_embedded_template_url) | **POST** /v1/template/createEmbeddedTemplateUrl | Generates a create URL to embeds template create process into your application.
*TemplateApi* | [**create_template**](docs/TemplateApi.md#create_template) | **POST** /v1/template/create | Creates a new template.
*TemplateApi* | [**delete_tag**](docs/TemplateApi.md#delete_tag) | **DELETE** /v1/template/deleteTags | Delete the Tags in Templates.
*TemplateApi* | [**delete_template**](docs/TemplateApi.md#delete_template) | **DELETE** /v1/template/delete | Deletes a template.
*TemplateApi* | [**download**](docs/TemplateApi.md#download) | **GET** /v1/template/download | Download the template.
*TemplateApi* | [**edit_template**](docs/TemplateApi.md#edit_template) | **PUT** /v1/template/edit | Edit and updates an existing template.
*TemplateApi* | [**get_embedded_template_edit_url**](docs/TemplateApi.md#get_embedded_template_edit_url) | **POST** /v1/template/getEmbeddedTemplateEditUrl | Generates a edit URL to embeds template edit process into your application.
*TemplateApi* | [**get_properties**](docs/TemplateApi.md#get_properties) | **GET** /v1/template/properties | Get summary of the template.
*TemplateApi* | [**list_templates**](docs/TemplateApi.md#list_templates) | **GET** /v1/template/list | List all the templates.
*TemplateApi* | [**merge_and_send**](docs/TemplateApi.md#merge_and_send) | **POST** /v1/template/mergeAndSend | Send the document by merging multiple templates.
*TemplateApi* | [**send_using_template**](docs/TemplateApi.md#send_using_template) | **POST** /v1/template/send | Send a document for signature using a Template.
*UserApi* | [**cancel_invitation**](docs/UserApi.md#cancel_invitation) | **POST** /v1/users/cancelInvitation | Cancel the users invitation.
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /v1/users/create | Create the user.
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /v1/users/get | Get summary of the user.
*UserApi* | [**list_users**](docs/UserApi.md#list_users) | **GET** /v1/users/list | List user documents.
*UserApi* | [**resend_invitation**](docs/UserApi.md#resend_invitation) | **POST** /v1/users/resendInvitation | Resend the users invitation.
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /v1/users/update | Update new User role.


## Documentation For Models

 - [AccessCodeDetail](docs/AccessCodeDetail.md)
 - [AccessCodeDetails](docs/AccessCodeDetails.md)
 - [AttachmentInfo](docs/AttachmentInfo.md)
 - [AuditTrail](docs/AuditTrail.md)
 - [BehalfDocument](docs/BehalfDocument.md)
 - [BehalfDocumentRecords](docs/BehalfDocumentRecords.md)
 - [BehalfOf](docs/BehalfOf.md)
 - [BillingViewModel](docs/BillingViewModel.md)
 - [BrandCreated](docs/BrandCreated.md)
 - [BrandCustomFieldDetails](docs/BrandCustomFieldDetails.md)
 - [BrandingMessage](docs/BrandingMessage.md)
 - [BrandingRecords](docs/BrandingRecords.md)
 - [ChangeRecipient](docs/ChangeRecipient.md)
 - [ConditionalRule](docs/ConditionalRule.md)
 - [ContactCreated](docs/ContactCreated.md)
 - [ContactDetails](docs/ContactDetails.md)
 - [ContactPageDetails](docs/ContactPageDetails.md)
 - [ContactsDetails](docs/ContactsDetails.md)
 - [ContactsList](docs/ContactsList.md)
 - [CreateContactResponse](docs/CreateContactResponse.md)
 - [CreateSenderIdentityRequest](docs/CreateSenderIdentityRequest.md)
 - [CreateTeamRequest](docs/CreateTeamRequest.md)
 - [CreateTemplateRequest](docs/CreateTemplateRequest.md)
 - [CreateUser](docs/CreateUser.md)
 - [CustomDomainSettings](docs/CustomDomainSettings.md)
 - [CustomFieldCollection](docs/CustomFieldCollection.md)
 - [CustomFieldMessage](docs/CustomFieldMessage.md)
 - [CustomFormField](docs/CustomFormField.md)
 - [DeleteCustomFieldReply](docs/DeleteCustomFieldReply.md)
 - [Document](docs/Document.md)
 - [DocumentCC](docs/DocumentCC.md)
 - [DocumentCcDetails](docs/DocumentCcDetails.md)
 - [DocumentCreated](docs/DocumentCreated.md)
 - [DocumentExpirySettings](docs/DocumentExpirySettings.md)
 - [DocumentFiles](docs/DocumentFiles.md)
 - [DocumentFormFields](docs/DocumentFormFields.md)
 - [DocumentInfo](docs/DocumentInfo.md)
 - [DocumentProperties](docs/DocumentProperties.md)
 - [DocumentReassign](docs/DocumentReassign.md)
 - [DocumentRecords](docs/DocumentRecords.md)
 - [DocumentSenderDetail](docs/DocumentSenderDetail.md)
 - [DocumentSigner](docs/DocumentSigner.md)
 - [DocumentSignerDetails](docs/DocumentSignerDetails.md)
 - [DocumentTags](docs/DocumentTags.md)
 - [EditSenderIdentityRequest](docs/EditSenderIdentityRequest.md)
 - [EditTemplateRequest](docs/EditTemplateRequest.md)
 - [EditableDateFieldSettings](docs/EditableDateFieldSettings.md)
 - [EmbeddedCreateTemplateRequest](docs/EmbeddedCreateTemplateRequest.md)
 - [EmbeddedCustomFieldCreated](docs/EmbeddedCustomFieldCreated.md)
 - [EmbeddedDocumentRequest](docs/EmbeddedDocumentRequest.md)
 - [EmbeddedSendCreated](docs/EmbeddedSendCreated.md)
 - [EmbeddedSendTemplateFormRequest](docs/EmbeddedSendTemplateFormRequest.md)
 - [EmbeddedSigningLink](docs/EmbeddedSigningLink.md)
 - [EmbeddedTemplateCreated](docs/EmbeddedTemplateCreated.md)
 - [EmbeddedTemplateEditRequest](docs/EmbeddedTemplateEditRequest.md)
 - [EmbeddedTemplateEdited](docs/EmbeddedTemplateEdited.md)
 - [ErrorResult](docs/ErrorResult.md)
 - [ExistingFormField](docs/ExistingFormField.md)
 - [ExtendExpiry](docs/ExtendExpiry.md)
 - [FileInfo](docs/FileInfo.md)
 - [Font](docs/Font.md)
 - [FormField](docs/FormField.md)
 - [FormGroup](docs/FormGroup.md)
 - [IdVerification](docs/IdVerification.md)
 - [IdentityVerificationSettings](docs/IdentityVerificationSettings.md)
 - [ImageInfo](docs/ImageInfo.md)
 - [MergeAndSendForSignForm](docs/MergeAndSendForSignForm.md)
 - [NotificationSettings](docs/NotificationSettings.md)
 - [PageDetails](docs/PageDetails.md)
 - [PhoneNumber](docs/PhoneNumber.md)
 - [PrefillField](docs/PrefillField.md)
 - [PrefillFieldRequest](docs/PrefillFieldRequest.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [RecipientNotificationSettings](docs/RecipientNotificationSettings.md)
 - [Rectangle](docs/Rectangle.md)
 - [ReminderMessage](docs/ReminderMessage.md)
 - [ReminderSettings](docs/ReminderSettings.md)
 - [RemoveAuthentication](docs/RemoveAuthentication.md)
 - [RevokeDocument](docs/RevokeDocument.md)
 - [Role](docs/Role.md)
 - [Roles](docs/Roles.md)
 - [SendForSign](docs/SendForSign.md)
 - [SendForSignFromTemplateForm](docs/SendForSignFromTemplateForm.md)
 - [SenderIdentityList](docs/SenderIdentityList.md)
 - [SenderIdentityViewModel](docs/SenderIdentityViewModel.md)
 - [Size](docs/Size.md)
 - [TeamCreated](docs/TeamCreated.md)
 - [TeamDocumentRecords](docs/TeamDocumentRecords.md)
 - [TeamListResponse](docs/TeamListResponse.md)
 - [TeamPageDetails](docs/TeamPageDetails.md)
 - [TeamResponse](docs/TeamResponse.md)
 - [TeamUpdateRequest](docs/TeamUpdateRequest.md)
 - [TeamUsers](docs/TeamUsers.md)
 - [Teams](docs/Teams.md)
 - [Template](docs/Template.md)
 - [TemplateCC](docs/TemplateCC.md)
 - [TemplateCreated](docs/TemplateCreated.md)
 - [TemplateFormFields](docs/TemplateFormFields.md)
 - [TemplateProperties](docs/TemplateProperties.md)
 - [TemplateRecords](docs/TemplateRecords.md)
 - [TemplateRole](docs/TemplateRole.md)
 - [TemplateSenderDetail](docs/TemplateSenderDetail.md)
 - [TemplateSenderDetails](docs/TemplateSenderDetails.md)
 - [TemplateSharedTemplateDetail](docs/TemplateSharedTemplateDetail.md)
 - [TemplateSignerDetails](docs/TemplateSignerDetails.md)
 - [TemplateTag](docs/TemplateTag.md)
 - [TextTagDefinition](docs/TextTagDefinition.md)
 - [TextTagOffset](docs/TextTagOffset.md)
 - [UpdateUser](docs/UpdateUser.md)
 - [UserPageDetails](docs/UserPageDetails.md)
 - [UserProperties](docs/UserProperties.md)
 - [UserRecords](docs/UserRecords.md)
 - [UsersDetails](docs/UsersDetails.md)
 - [Validation](docs/Validation.md)
 - [ViewBrandDetails](docs/ViewBrandDetails.md)
 - [ViewCustomFieldDetails](docs/ViewCustomFieldDetails.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Bearer"></a>
### Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="X-API-KEY"></a>
### X-API-KEY

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author

support@boldsign.com


