# NotificationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewed** | **bool** |  | [optional] [default to True]
**sent** | **bool** |  | [optional] [default to False]
**delivery_failed** | **bool** |  | [optional] [default to True]
**declined** | **bool** |  | [optional] [default to True]
**revoked** | **bool** |  | [optional] [default to True]
**reassigned** | **bool** |  | [optional] [default to True]
**completed** | **bool** |  | [optional] [default to True]
**signed** | **bool** |  | [optional] [default to True]
**expired** | **bool** |  | [optional] [default to True]
**authentication_failed** | **bool** |  | [optional] [default to True]
**reminders** | **bool** |  | [optional] [default to True]

## Example

```python
from boldsign.models.notification_settings import NotificationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSettings from a JSON string
notification_settings_instance = NotificationSettings.from_json(json)
# print the JSON string representation of the object
print(NotificationSettings.to_json())

# convert the object into a dict
notification_settings_dict = notification_settings_instance.to_dict()
# create an instance of NotificationSettings from a dict
notification_settings_from_dict = NotificationSettings.from_dict(notification_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


