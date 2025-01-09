# RecipientChangeLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | [**List[Added]**](Added.md) |  | [optional] 
**removed** | [**List[Removed]**](Removed.md) |  | [optional] 

## Example

```python
from boldsign.models.recipient_change_log import RecipientChangeLog

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientChangeLog from a JSON string
recipient_change_log_instance = RecipientChangeLog.from_json(json)
# print the JSON string representation of the object
print(RecipientChangeLog.to_json())

# convert the object into a dict
recipient_change_log_dict = recipient_change_log_instance.to_dict()
# create an instance of RecipientChangeLog from a dict
recipient_change_log_from_dict = RecipientChangeLog.from_dict(recipient_change_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


