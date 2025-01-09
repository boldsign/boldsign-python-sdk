# BrandCustomFieldDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**field_description** | **str** |  | [optional] 
**field_order** | **int** |  | [optional] [default to 1]
**brand_id** | **str** |  | [optional] 
**shared_field** | **bool** |  | [optional] 
**form_field** | [**CustomFormField**](CustomFormField.md) |  | [optional] 

## Example

```python
from boldsign.models.brand_custom_field_details import BrandCustomFieldDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BrandCustomFieldDetails from a JSON string
brand_custom_field_details_instance = BrandCustomFieldDetails.from_json(json)
# print the JSON string representation of the object
print(BrandCustomFieldDetails.to_json())

# convert the object into a dict
brand_custom_field_details_dict = brand_custom_field_details_instance.to_dict()
# create an instance of BrandCustomFieldDetails from a dict
brand_custom_field_details_from_dict = BrandCustomFieldDetails.from_dict(brand_custom_field_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


