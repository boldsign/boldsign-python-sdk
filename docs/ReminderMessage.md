# ReminderMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 
**reminder_phone_numbers** | [**List[PhoneNumber]**](PhoneNumber.md) |  | [optional] 

## Example

```python
from boldsign.models.reminder_message import ReminderMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderMessage from a JSON string
reminder_message_instance = ReminderMessage.from_json(json)
# print the JSON string representation of the object
print(ReminderMessage.to_json())

# convert the object into a dict
reminder_message_dict = reminder_message_instance.to_dict()
# create an instance of ReminderMessage from a dict
reminder_message_from_dict = ReminderMessage.from_dict(reminder_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


