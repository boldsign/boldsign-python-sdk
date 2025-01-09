# ConditionalRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** |  | [optional] 
**is_checked** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from boldsign.models.conditional_rule import ConditionalRule

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionalRule from a JSON string
conditional_rule_instance = ConditionalRule.from_json(json)
# print the JSON string representation of the object
print(ConditionalRule.to_json())

# convert the object into a dict
conditional_rule_dict = conditional_rule_instance.to_dict()
# create an instance of ConditionalRule from a dict
conditional_rule_from_dict = ConditionalRule.from_dict(conditional_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


