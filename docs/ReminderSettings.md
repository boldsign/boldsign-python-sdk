# ReminderSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_auto_reminder** | **bool** |  | [optional] [default to False]
**reminder_days** | **int** |  | [optional] [default to 3]
**reminder_count** | **int** |  | [optional] [default to 3]

## Example

```python
from boldsign.models.reminder_settings import ReminderSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderSettings from a JSON string
reminder_settings_instance = ReminderSettings.from_json(json)
# print the JSON string representation of the object
print(ReminderSettings.to_json())

# convert the object into a dict
reminder_settings_dict = reminder_settings_instance.to_dict()
# create an instance of ReminderSettings from a dict
reminder_settings_from_dict = ReminderSettings.from_dict(reminder_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


