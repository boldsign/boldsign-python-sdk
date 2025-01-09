# TeamDocumentRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_details** | [**PageDetails**](PageDetails.md) |  | [optional] 
**result** | [**List[Document]**](Document.md) |  | [optional] 

## Example

```python
from boldsign.models.team_document_records import TeamDocumentRecords

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDocumentRecords from a JSON string
team_document_records_instance = TeamDocumentRecords.from_json(json)
# print the JSON string representation of the object
print(TeamDocumentRecords.to_json())

# convert the object into a dict
team_document_records_dict = team_document_records_instance.to_dict()
# create an instance of TeamDocumentRecords from a dict
team_document_records_from_dict = TeamDocumentRecords.from_dict(team_document_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


