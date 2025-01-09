# TemplateSenderDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_sender_detail import TemplateSenderDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSenderDetail from a JSON string
template_sender_detail_instance = TemplateSenderDetail.from_json(json)
# print the JSON string representation of the object
print(TemplateSenderDetail.to_json())

# convert the object into a dict
template_sender_detail_dict = template_sender_detail_instance.to_dict()
# create an instance of TemplateSenderDetail from a dict
template_sender_detail_from_dict = TemplateSenderDetail.from_dict(template_sender_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


