# BillingViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_credits** | **float** |  | [optional] 

## Example

```python
from boldsign.models.billing_view_model import BillingViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of BillingViewModel from a JSON string
billing_view_model_instance = BillingViewModel.from_json(json)
# print the JSON string representation of the object
print(BillingViewModel.to_json())

# convert the object into a dict
billing_view_model_dict = billing_view_model_instance.to_dict()
# create an instance of BillingViewModel from a dict
billing_view_model_from_dict = BillingViewModel.from_dict(billing_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


