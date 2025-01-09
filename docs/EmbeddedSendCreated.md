# EmbeddedSendCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | [optional] 
**send_url** | **str** |  | [optional] 

## Example

```python
from boldsign.models.embedded_send_created import EmbeddedSendCreated

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedSendCreated from a JSON string
embedded_send_created_instance = EmbeddedSendCreated.from_json(json)
# print the JSON string representation of the object
print(EmbeddedSendCreated.to_json())

# convert the object into a dict
embedded_send_created_dict = embedded_send_created_instance.to_dict()
# create an instance of EmbeddedSendCreated from a dict
embedded_send_created_from_dict = EmbeddedSendCreated.from_dict(embedded_send_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


