# SenderIdentityViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**approved_date** | **str** |  | [optional] 
**notification_settings** | [**NotificationSettings**](NotificationSettings.md) |  | [optional] 
**brand_id** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**meta_data** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from boldsign.models.sender_identity_view_model import SenderIdentityViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of SenderIdentityViewModel from a JSON string
sender_identity_view_model_instance = SenderIdentityViewModel.from_json(json)
# print the JSON string representation of the object
print(SenderIdentityViewModel.to_json())

# convert the object into a dict
sender_identity_view_model_dict = sender_identity_view_model_instance.to_dict()
# create an instance of SenderIdentityViewModel from a dict
sender_identity_view_model_from_dict = SenderIdentityViewModel.from_dict(sender_identity_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


