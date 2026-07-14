# PhoneNumberWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] 
**number** | **str** |  | [optional] 

## Example

```python
from boldsign.models.phone_number_webhook_model import PhoneNumberWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberWebhookModel from a JSON string
phone_number_webhook_model_instance = PhoneNumberWebhookModel.from_json(json)
# print the JSON string representation of the object
print(PhoneNumberWebhookModel.to_json())

# convert the object into a dict
phone_number_webhook_model_dict = phone_number_webhook_model_instance.to_dict()
# create an instance of PhoneNumberWebhookModel from a dict
phone_number_webhook_model_from_dict = PhoneNumberWebhookModel.from_dict(phone_number_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


