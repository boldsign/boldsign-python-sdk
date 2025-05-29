# EmbeddedFileDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_id** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from boldsign.models.embedded_file_details import EmbeddedFileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedFileDetails from a JSON string
embedded_file_details_instance = EmbeddedFileDetails.from_json(json)
# print the JSON string representation of the object
print(EmbeddedFileDetails.to_json())

# convert the object into a dict
embedded_file_details_dict = embedded_file_details_instance.to_dict()
# create an instance of EmbeddedFileDetails from a dict
embedded_file_details_from_dict = EmbeddedFileDetails.from_dict(embedded_file_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


