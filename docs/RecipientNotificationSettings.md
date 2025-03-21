# RecipientNotificationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature_request** | **bool** |  | [optional] [default to True]
**declined** | **bool** |  | [optional] [default to True]
**revoked** | **bool** |  | [optional] [default to True]
**signed** | **bool** |  | [optional] [default to True]
**completed** | **bool** |  | [optional] [default to True]
**expired** | **bool** |  | [optional] [default to True]
**reassigned** | **bool** |  | [optional] [default to True]
**deleted** | **bool** |  | [optional] [default to True]
**reminders** | **bool** |  | [optional] [default to True]
**edit_recipient** | **bool** |  | [optional] [default to True]
**edit_document** | **bool** |  | [optional] [default to True]
**viewed** | **bool** |  | [optional] 

## Example

```python
from boldsign.models.recipient_notification_settings import RecipientNotificationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientNotificationSettings from a JSON string
recipient_notification_settings_instance = RecipientNotificationSettings.from_json(json)
# print the JSON string representation of the object
print(RecipientNotificationSettings.to_json())

# convert the object into a dict
recipient_notification_settings_dict = recipient_notification_settings_instance.to_dict()
# create an instance of RecipientNotificationSettings from a dict
recipient_notification_settings_from_dict = RecipientNotificationSettings.from_dict(recipient_notification_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


