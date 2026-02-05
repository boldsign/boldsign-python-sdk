# DocumentSigner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**private_message** | **str** |  | [optional] 
**authentication_type** | **str** |  | [optional] 
**phone_number** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 
**delivery_mode** | **str** |  | [optional] 
**authentication_code** | **str** |  | [optional] 
**identity_verification_settings** | [**IdentityVerificationSettings**](IdentityVerificationSettings.md) |  | [optional] 
**signer_order** | **int** |  | [optional] 
**enable_email_otp** | **bool** |  | [optional] 
**signer_type** | **str** |  | [optional] 
**host_email** | **str** |  | [optional] 
**signer_role** | **str** |  | [optional] 
**allow_field_configuration** | **bool** |  | [optional] 
**form_fields** | [**List[FormField]**](FormField.md) |  | [optional] 
**language** | **int** | &lt;p&gt;Description:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;&lt;i&gt;0&lt;/i&gt; - None&lt;/li&gt;&lt;li&gt;&lt;i&gt;1&lt;/i&gt; - English&lt;/li&gt;&lt;li&gt;&lt;i&gt;2&lt;/i&gt; - Spanish&lt;/li&gt;&lt;li&gt;&lt;i&gt;3&lt;/i&gt; - German&lt;/li&gt;&lt;li&gt;&lt;i&gt;4&lt;/i&gt; - French&lt;/li&gt;&lt;li&gt;&lt;i&gt;5&lt;/i&gt; - Romanian&lt;/li&gt;&lt;li&gt;&lt;i&gt;6&lt;/i&gt; - Norwegian&lt;/li&gt;&lt;li&gt;&lt;i&gt;7&lt;/i&gt; - Bulgarian&lt;/li&gt;&lt;li&gt;&lt;i&gt;8&lt;/i&gt; - Italian&lt;/li&gt;&lt;li&gt;&lt;i&gt;9&lt;/i&gt; - Danish&lt;/li&gt;&lt;li&gt;&lt;i&gt;10&lt;/i&gt; - Polish&lt;/li&gt;&lt;li&gt;&lt;i&gt;11&lt;/i&gt; - Portuguese&lt;/li&gt;&lt;li&gt;&lt;i&gt;12&lt;/i&gt; - Czech&lt;/li&gt;&lt;li&gt;&lt;i&gt;13&lt;/i&gt; - Dutch&lt;/li&gt;&lt;li&gt;&lt;i&gt;14&lt;/i&gt; - Swedish&lt;/li&gt;&lt;li&gt;&lt;i&gt;15&lt;/i&gt; - Russian&lt;/li&gt;&lt;li&gt;&lt;i&gt;16&lt;/i&gt; - Japanese&lt;/li&gt;&lt;li&gt;&lt;i&gt;17&lt;/i&gt; - Thai&lt;/li&gt;&lt;li&gt;&lt;i&gt;18&lt;/i&gt; - SimplifiedChinese&lt;/li&gt;&lt;li&gt;&lt;i&gt;19&lt;/i&gt; - TraditionalChinese&lt;/li&gt;&lt;li&gt;&lt;i&gt;20&lt;/i&gt; - Korean&lt;/li&gt;&lt;/ul&gt; | [optional] 
**locale** | **str** |  | [optional] 
**sign_type** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**recipient_notification_settings** | [**RecipientNotificationSettings**](RecipientNotificationSettings.md) |  | [optional] 
**authentication_retry_count** | **int** |  | [optional] 
**enable_qes** | **bool** |  | [optional] 
**authentication_settings** | [**AuthenticationSettings**](AuthenticationSettings.md) |  | [optional] 

## Example

```python
from boldsign.models.document_signer import DocumentSigner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSigner from a JSON string
document_signer_instance = DocumentSigner.from_json(json)
# print the JSON string representation of the object
print(DocumentSigner.to_json())

# convert the object into a dict
document_signer_dict = document_signer_instance.to_dict()
# create an instance of DocumentSigner from a dict
document_signer_from_dict = DocumentSigner.from_dict(document_signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


