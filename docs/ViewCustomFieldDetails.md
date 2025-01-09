# ViewCustomFieldDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_id** | **str** |  | [optional] 
**field_name** | **str** |  | [optional] 
**field_description** | **str** |  | [optional] 
**field_order** | **int** |  | [optional] 
**brand_id** | **str** |  | [optional] 
**shared_field** | **bool** |  | [optional] 
**form_field** | [**CustomFormField**](CustomFormField.md) |  | [optional] 

## Example

```python
from boldsign.models.view_custom_field_details import ViewCustomFieldDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ViewCustomFieldDetails from a JSON string
view_custom_field_details_instance = ViewCustomFieldDetails.from_json(json)
# print the JSON string representation of the object
print(ViewCustomFieldDetails.to_json())

# convert the object into a dict
view_custom_field_details_dict = view_custom_field_details_instance.to_dict()
# create an instance of ViewCustomFieldDetails from a dict
view_custom_field_details_from_dict = ViewCustomFieldDetails.from_dict(view_custom_field_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


