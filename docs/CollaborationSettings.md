# CollaborationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_required** | **bool** |  | [optional] 
**require_signer_approval** | **bool** |  | [optional] 
**require_initial** | **bool** |  | [optional] 
**allowed_signers** | **List[str]** |  | [optional] 

## Example

```python
from boldsign.models.collaboration_settings import CollaborationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CollaborationSettings from a JSON string
collaboration_settings_instance = CollaborationSettings.from_json(json)
# print the JSON string representation of the object
print(CollaborationSettings.to_json())

# convert the object into a dict
collaboration_settings_dict = collaboration_settings_instance.to_dict()
# create an instance of CollaborationSettings from a dict
collaboration_settings_from_dict = CollaborationSettings.from_dict(collaboration_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


