# IdReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_result** | **str** |  | [optional] 
**verified_date** | **datetime** |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**document** | [**IdDocument**](IdDocument.md) |  | [optional] 

## Example

```python
from boldsign.models.id_report import IdReport

# TODO update the JSON string below
json = "{}"
# create an instance of IdReport from a JSON string
id_report_instance = IdReport.from_json(json)
# print the JSON string representation of the object
print(IdReport.to_json())

# convert the object into a dict
id_report_dict = id_report_instance.to_dict()
# create an instance of IdReport from a dict
id_report_from_dict = IdReport.from_dict(id_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


