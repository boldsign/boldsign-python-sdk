# DownloadImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_id** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**file_id** | **str** |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from boldsign.models.download_image_request import DownloadImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadImageRequest from a JSON string
download_image_request_instance = DownloadImageRequest.from_json(json)
# print the JSON string representation of the object
print(DownloadImageRequest.to_json())

# convert the object into a dict
download_image_request_dict = download_image_request_instance.to_dict()
# create an instance of DownloadImageRequest from a dict
download_image_request_from_dict = DownloadImageRequest.from_dict(download_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


