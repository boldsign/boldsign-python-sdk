# Base64File


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_base64** | **str** |  | 
**file_name** | **str** |  | [optional] 

## Example

```python
from boldsign.models.base64_file import Base64File

# TODO update the JSON string below
json = "{}"
# create an instance of Base64File from a JSON string
base64_file_instance = Base64File.from_json(json)
# print the JSON string representation of the object
print(Base64File.to_json())

# convert the object into a dict
base64_file_dict = base64_file_instance.to_dict()
# create an instance of Base64File from a dict
base64_file_from_dict = Base64File.from_dict(base64_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


