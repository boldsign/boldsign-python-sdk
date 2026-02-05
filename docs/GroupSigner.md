# GroupSigner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**signer_email** | **str** |  | [optional] 
**signer_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**is_viewed** | **bool** |  | [optional] 
**is_delivery_failed** | **bool** |  | [optional] 
**is_authentication_failed** | **bool** |  | [optional] 

## Example

```python
from boldsign.models.group_signer import GroupSigner

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSigner from a JSON string
group_signer_instance = GroupSigner.from_json(json)
# print the JSON string representation of the object
print(GroupSigner.to_json())

# convert the object into a dict
group_signer_dict = group_signer_instance.to_dict()
# create an instance of GroupSigner from a dict
group_signer_from_dict = GroupSigner.from_dict(group_signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


