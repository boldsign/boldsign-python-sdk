# EditSenderIdentityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**notification_settings** | [**NotificationSettings**](NotificationSettings.md) |  | [optional] 
**redirect_url** | **str** |  | [optional] 

## Example

```python
from boldsign.models.edit_sender_identity_request import EditSenderIdentityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditSenderIdentityRequest from a JSON string
edit_sender_identity_request_instance = EditSenderIdentityRequest.from_json(json)
# print the JSON string representation of the object
print(EditSenderIdentityRequest.to_json())

# convert the object into a dict
edit_sender_identity_request_dict = edit_sender_identity_request_instance.to_dict()
# create an instance of EditSenderIdentityRequest from a dict
edit_sender_identity_request_from_dict = EditSenderIdentityRequest.from_dict(edit_sender_identity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


