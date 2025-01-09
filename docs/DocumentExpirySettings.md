# DocumentExpirySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date_type** | **str** |  | [optional] 
**expiry_value** | **int** |  | [optional] 
**enable_default_expiry_alert** | **bool** |  | [optional] 
**enable_auto_reminder** | **bool** |  | [optional] 
**reminder_days** | **int** |  | [optional] 
**reminder_count** | **int** |  | [optional] 

## Example

```python
from boldsign.models.document_expiry_settings import DocumentExpirySettings

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentExpirySettings from a JSON string
document_expiry_settings_instance = DocumentExpirySettings.from_json(json)
# print the JSON string representation of the object
print(DocumentExpirySettings.to_json())

# convert the object into a dict
document_expiry_settings_dict = document_expiry_settings_instance.to_dict()
# create an instance of DocumentExpirySettings from a dict
document_expiry_settings_from_dict = DocumentExpirySettings.from_dict(document_expiry_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


