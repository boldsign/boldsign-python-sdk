# TemplateSenderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template_sender_details import TemplateSenderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSenderDetails from a JSON string
template_sender_details_instance = TemplateSenderDetails.from_json(json)
# print the JSON string representation of the object
print(TemplateSenderDetails.to_json())

# convert the object into a dict
template_sender_details_dict = template_sender_details_instance.to_dict()
# create an instance of TemplateSenderDetails from a dict
template_sender_details_from_dict = TemplateSenderDetails.from_dict(template_sender_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


