# SenderIdentityEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**approved_date_time** | **datetime** |  | [optional] 
**brand_id** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**meta_data** | **Dict[str, Optional[str]]** |  | [optional] 
**created_by** | [**SenderIdentityCreator**](SenderIdentityCreator.md) |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from boldsign.models.sender_identity_event import SenderIdentityEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SenderIdentityEvent from a JSON string
sender_identity_event_instance = SenderIdentityEvent.from_json(json)
# print the JSON string representation of the object
print(SenderIdentityEvent.to_json())

# convert the object into a dict
sender_identity_event_dict = sender_identity_event_instance.to_dict()
# create an instance of SenderIdentityEvent from a dict
sender_identity_event_from_dict = SenderIdentityEvent.from_dict(sender_identity_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


