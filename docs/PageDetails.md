# PageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**total_records_count** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**sorted_column** | **str** |  | [optional] 
**sort_direction** | **str** |  | [optional] 

## Example

```python
from boldsign.models.page_details import PageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PageDetails from a JSON string
page_details_instance = PageDetails.from_json(json)
# print the JSON string representation of the object
print(PageDetails.to_json())

# convert the object into a dict
page_details_dict = page_details_instance.to_dict()
# create an instance of PageDetails from a dict
page_details_from_dict = PageDetails.from_dict(page_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


