# TemplateShareErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | **List[str]** |  | [optional] 
**template_id** | **str** |  | [optional] 
**error_type** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_share_error_response import TemplateShareErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateShareErrorResponse from a JSON string
template_share_error_response_instance = TemplateShareErrorResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateShareErrorResponse.to_json())

# convert the object into a dict
template_share_error_response_dict = template_share_error_response_instance.to_dict()
# create an instance of TemplateShareErrorResponse from a dict
template_share_error_response_from_dict = TemplateShareErrorResponse.from_dict(template_share_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


