# ImageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**allowed_file_extensions** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from boldsign.models.image_info import ImageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ImageInfo from a JSON string
image_info_instance = ImageInfo.from_json(json)
# print the JSON string representation of the object
print(ImageInfo.to_json())

# convert the object into a dict
image_info_dict = image_info_instance.to_dict()
# create an instance of ImageInfo from a dict
image_info_from_dict = ImageInfo.from_dict(image_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


