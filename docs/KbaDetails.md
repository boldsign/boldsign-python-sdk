# KbaDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**maximum_retry_count** | **int** |  | [optional] 
**name_matcher** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from boldsign.models.kba_details import KbaDetails

# TODO update the JSON string below
json = "{}"
# create an instance of KbaDetails from a JSON string
kba_details_instance = KbaDetails.from_json(json)
# print the JSON string representation of the object
print(KbaDetails.to_json())

# convert the object into a dict
kba_details_dict = kba_details_instance.to_dict()
# create an instance of KbaDetails from a dict
kba_details_from_dict = KbaDetails.from_dict(kba_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


