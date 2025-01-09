# CreateSenderIdentityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** |  | [optional] 
**notification_settings** | [**NotificationSettings**](NotificationSettings.md) |  | [optional] 
**brand_id** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 

## Example

```python
from boldsign.models.create_sender_identity_request import CreateSenderIdentityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSenderIdentityRequest from a JSON string
create_sender_identity_request_instance = CreateSenderIdentityRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSenderIdentityRequest.to_json())

# convert the object into a dict
create_sender_identity_request_dict = create_sender_identity_request_instance.to_dict()
# create an instance of CreateSenderIdentityRequest from a dict
create_sender_identity_request_from_dict = CreateSenderIdentityRequest.from_dict(create_sender_identity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


