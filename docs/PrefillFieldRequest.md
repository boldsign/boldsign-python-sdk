# PrefillFieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[PrefillField]**](PrefillField.md) |  | 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from boldsign.models.prefill_field_request import PrefillFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrefillFieldRequest from a JSON string
prefill_field_request_instance = PrefillFieldRequest.from_json(json)
# print the JSON string representation of the object
print(PrefillFieldRequest.to_json())

# convert the object into a dict
prefill_field_request_dict = prefill_field_request_instance.to_dict()
# create an instance of PrefillFieldRequest from a dict
prefill_field_request_from_dict = PrefillFieldRequest.from_dict(prefill_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


