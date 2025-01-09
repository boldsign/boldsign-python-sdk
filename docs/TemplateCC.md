# TemplateCC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_cc import TemplateCC

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateCC from a JSON string
template_cc_instance = TemplateCC.from_json(json)
# print the JSON string representation of the object
print(TemplateCC.to_json())

# convert the object into a dict
template_cc_dict = template_cc_instance.to_dict()
# create an instance of TemplateCC from a dict
template_cc_from_dict = TemplateCC.from_dict(template_cc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


