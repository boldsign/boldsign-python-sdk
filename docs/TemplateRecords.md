# TemplateRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_details** | [**PageDetails**](PageDetails.md) |  | [optional] 
**result** | [**List[Template]**](Template.md) |  | [optional] 

## Example

```python
from boldsign.models.template_records import TemplateRecords

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateRecords from a JSON string
template_records_instance = TemplateRecords.from_json(json)
# print the JSON string representation of the object
print(TemplateRecords.to_json())

# convert the object into a dict
template_records_dict = template_records_instance.to_dict()
# create an instance of TemplateRecords from a dict
template_records_from_dict = TemplateRecords.from_dict(template_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


