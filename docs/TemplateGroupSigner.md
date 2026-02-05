# TemplateGroupSigner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_email** | **str** |  | [optional] 
**signer_name** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_group_signer import TemplateGroupSigner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateGroupSigner from a JSON string
template_group_signer_instance = TemplateGroupSigner.from_json(json)
# print the JSON string representation of the object
print(TemplateGroupSigner.to_json())

# convert the object into a dict
template_group_signer_dict = template_group_signer_instance.to_dict()
# create an instance of TemplateGroupSigner from a dict
template_group_signer_from_dict = TemplateGroupSigner.from_dict(template_group_signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


