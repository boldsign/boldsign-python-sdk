# SignatureFrameSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_signature_frame** | **bool** |  | [optional] [default to False]
**show_recipient_name** | **bool** |  | [optional] [default to False]
**show_recipient_email** | **bool** |  | [optional] [default to False]
**show_time_stamp** | **bool** |  | [optional] [default to False]

## Example

```python
from boldsign.models.signature_frame_settings import SignatureFrameSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureFrameSettings from a JSON string
signature_frame_settings_instance = SignatureFrameSettings.from_json(json)
# print the JSON string representation of the object
print(SignatureFrameSettings.to_json())

# convert the object into a dict
signature_frame_settings_dict = signature_frame_settings_instance.to_dict()
# create an instance of SignatureFrameSettings from a dict
signature_frame_settings_from_dict = SignatureFrameSettings.from_dict(signature_frame_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


