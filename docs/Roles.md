# Roles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**default_signer_name** | **str** |  | [optional] 
**default_signer_email** | **str** |  | [optional] 
**phone_number** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 
**signer_order** | **int** |  | [optional] 
**signer_type** | **str** |  | [optional] 
**host_email** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**language** | **int** | &lt;p&gt;Description:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;&lt;i&gt;0&lt;/i&gt; - None&lt;/li&gt;&lt;li&gt;&lt;i&gt;1&lt;/i&gt; - English&lt;/li&gt;&lt;li&gt;&lt;i&gt;2&lt;/i&gt; - Spanish&lt;/li&gt;&lt;li&gt;&lt;i&gt;3&lt;/i&gt; - German&lt;/li&gt;&lt;li&gt;&lt;i&gt;4&lt;/i&gt; - French&lt;/li&gt;&lt;li&gt;&lt;i&gt;5&lt;/i&gt; - Romanian&lt;/li&gt;&lt;li&gt;&lt;i&gt;6&lt;/i&gt; - Norwegian&lt;/li&gt;&lt;li&gt;&lt;i&gt;7&lt;/i&gt; - Bulgarian&lt;/li&gt;&lt;li&gt;&lt;i&gt;8&lt;/i&gt; - Italian&lt;/li&gt;&lt;li&gt;&lt;i&gt;9&lt;/i&gt; - Danish&lt;/li&gt;&lt;li&gt;&lt;i&gt;10&lt;/i&gt; - Polish&lt;/li&gt;&lt;li&gt;&lt;i&gt;11&lt;/i&gt; - Portuguese&lt;/li&gt;&lt;li&gt;&lt;i&gt;12&lt;/i&gt; - Czech&lt;/li&gt;&lt;li&gt;&lt;i&gt;13&lt;/i&gt; - Dutch&lt;/li&gt;&lt;li&gt;&lt;i&gt;14&lt;/i&gt; - Swedish&lt;/li&gt;&lt;li&gt;&lt;i&gt;15&lt;/i&gt; - Russian&lt;/li&gt;&lt;/ul&gt; | [optional] 
**locale** | **str** |  | [optional] 
**allow_role_edit** | **bool** |  | [optional] 
**allow_role_delete** | **bool** |  | [optional] 
**enable_access_code** | **bool** |  | [optional] 
**enable_email_otp** | **bool** |  | [optional] 
**impose_authentication** | **str** |  | [optional] 
**delivery_mode** | **str** |  | [optional] 
**allow_field_configuration** | **bool** |  | [optional] 
**form_fields** | [**List[TemplateFormFields]**](TemplateFormFields.md) |  | [optional] 
**enable_edit_recipients** | **bool** |  | [optional] 
**enable_delete_recipients** | **bool** |  | [optional] 
**recipient_notification_settings** | [**RecipientNotificationSettings**](RecipientNotificationSettings.md) |  | [optional] 
**enable_qes** | **bool** |  | [optional] 

## Example

```python
from boldsign.models.roles import Roles

# TODO update the JSON string below
json = "{}"
# create an instance of Roles from a JSON string
roles_instance = Roles.from_json(json)
# print the JSON string representation of the object
print(Roles.to_json())

# convert the object into a dict
roles_dict = roles_instance.to_dict()
# create an instance of Roles from a dict
roles_from_dict = Roles.from_dict(roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


