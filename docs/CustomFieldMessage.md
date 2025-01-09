# CustomFieldMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from boldsign.models.custom_field_message import CustomFieldMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldMessage from a JSON string
custom_field_message_instance = CustomFieldMessage.from_json(json)
# print the JSON string representation of the object
print(CustomFieldMessage.to_json())

# convert the object into a dict
custom_field_message_dict = custom_field_message_instance.to_dict()
# create an instance of CustomFieldMessage from a dict
custom_field_message_from_dict = CustomFieldMessage.from_dict(custom_field_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


