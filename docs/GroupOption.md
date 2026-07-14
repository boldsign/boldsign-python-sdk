# GroupOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**is_selected** | **bool** |  | [optional] 

## Example

```python
from boldsign.models.group_option import GroupOption

# TODO update the JSON string below
json = "{}"
# create an instance of GroupOption from a JSON string
group_option_instance = GroupOption.from_json(json)
# print the JSON string representation of the object
print(GroupOption.to_json())

# convert the object into a dict
group_option_dict = group_option_instance.to_dict()
# create an instance of GroupOption from a dict
group_option_from_dict = GroupOption.from_dict(group_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


