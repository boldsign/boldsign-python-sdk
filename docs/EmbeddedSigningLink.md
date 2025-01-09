# EmbeddedSigningLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_link** | **str** |  | [optional] 

## Example

```python
from boldsign.models.embedded_signing_link import EmbeddedSigningLink

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedSigningLink from a JSON string
embedded_signing_link_instance = EmbeddedSigningLink.from_json(json)
# print the JSON string representation of the object
print(EmbeddedSigningLink.to_json())

# convert the object into a dict
embedded_signing_link_dict = embedded_signing_link_instance.to_dict()
# create an instance of EmbeddedSigningLink from a dict
embedded_signing_link_from_dict = EmbeddedSigningLink.from_dict(embedded_signing_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


