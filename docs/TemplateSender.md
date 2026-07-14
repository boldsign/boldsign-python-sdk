# TemplateSender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_sender import TemplateSender

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSender from a JSON string
template_sender_instance = TemplateSender.from_json(json)
# print the JSON string representation of the object
print(TemplateSender.to_json())

# convert the object into a dict
template_sender_dict = template_sender_instance.to_dict()
# create an instance of TemplateSender from a dict
template_sender_from_dict = TemplateSender.from_dict(template_sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


