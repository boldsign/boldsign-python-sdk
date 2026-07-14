# GroupSignerSettingsWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**allowed_directories** | **List[str]** |  | [optional] 

## Example

```python
from boldsign.models.group_signer_settings_webhook_model import GroupSignerSettingsWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSignerSettingsWebhookModel from a JSON string
group_signer_settings_webhook_model_instance = GroupSignerSettingsWebhookModel.from_json(json)
# print the JSON string representation of the object
print(GroupSignerSettingsWebhookModel.to_json())

# convert the object into a dict
group_signer_settings_webhook_model_dict = group_signer_settings_webhook_model_instance.to_dict()
# create an instance of GroupSignerSettingsWebhookModel from a dict
group_signer_settings_webhook_model_from_dict = GroupSignerSettingsWebhookModel.from_dict(group_signer_settings_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


