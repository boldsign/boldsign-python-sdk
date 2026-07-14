# FormFieldPermissionWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_add** | **bool** |  | [optional] 
**can_modify** | **bool** |  | [optional] 
**can_modify_default_value** | **bool** |  | [optional] 

## Example

```python
from boldsign.models.form_field_permission_webhook_model import FormFieldPermissionWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of FormFieldPermissionWebhookModel from a JSON string
form_field_permission_webhook_model_instance = FormFieldPermissionWebhookModel.from_json(json)
# print the JSON string representation of the object
print(FormFieldPermissionWebhookModel.to_json())

# convert the object into a dict
form_field_permission_webhook_model_dict = form_field_permission_webhook_model_instance.to_dict()
# create an instance of FormFieldPermissionWebhookModel from a dict
form_field_permission_webhook_model_from_dict = FormFieldPermissionWebhookModel.from_dict(form_field_permission_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


