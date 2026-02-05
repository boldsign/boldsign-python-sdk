# IdVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**maximum_retry_count** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**name_matcher** | **str** |  | [optional] 
**require_live_capture** | **bool** |  | [optional] 
**require_matching_selfie** | **bool** |  | [optional] 
**hold_for_prefill** | **bool** |  | [optional] 
**prefill_completed** | **bool** |  | [optional] 
**allowed_document_types** | **List[str]** |  | [optional] 

## Example

```python
from boldsign.models.id_verification import IdVerification

# TODO update the JSON string below
json = "{}"
# create an instance of IdVerification from a JSON string
id_verification_instance = IdVerification.from_json(json)
# print the JSON string representation of the object
print(IdVerification.to_json())

# convert the object into a dict
id_verification_dict = id_verification_instance.to_dict()
# create an instance of IdVerification from a dict
id_verification_from_dict = IdVerification.from_dict(id_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


