# VerificationDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_id** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from boldsign.models.verification_data_request import VerificationDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationDataRequest from a JSON string
verification_data_request_instance = VerificationDataRequest.from_json(json)
# print the JSON string representation of the object
print(VerificationDataRequest.to_json())

# convert the object into a dict
verification_data_request_dict = verification_data_request_instance.to_dict()
# create an instance of VerificationDataRequest from a dict
verification_data_request_from_dict = VerificationDataRequest.from_dict(verification_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


