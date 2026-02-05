# FormFieldPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_add** | **bool** |  | [optional] 
**can_modify** | **bool** |  | [optional] 
**can_modify_default_value** | **bool** |  | [optional] 

## Example

```python
from boldsign.models.form_field_permission import FormFieldPermission

# TODO update the JSON string below
json = "{}"
# create an instance of FormFieldPermission from a JSON string
form_field_permission_instance = FormFieldPermission.from_json(json)
# print the JSON string representation of the object
print(FormFieldPermission.to_json())

# convert the object into a dict
form_field_permission_dict = form_field_permission_instance.to_dict()
# create an instance of FormFieldPermission from a dict
form_field_permission_from_dict = FormFieldPermission.from_dict(form_field_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


