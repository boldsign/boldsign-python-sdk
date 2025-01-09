# FormGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_names** | **List[str]** |  | 
**group_validation** | **str** |  | 
**minimum_count** | **int** |  | [optional] 
**maximum_count** | **int** |  | [optional] 
**data_sync_tag** | **str** |  | [optional] 

## Example

```python
from boldsign.models.form_group import FormGroup

# TODO update the JSON string below
json = "{}"
# create an instance of FormGroup from a JSON string
form_group_instance = FormGroup.from_json(json)
# print the JSON string representation of the object
print(FormGroup.to_json())

# convert the object into a dict
form_group_dict = form_group_instance.to_dict()
# create an instance of FormGroup from a dict
form_group_from_dict = FormGroup.from_dict(form_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


