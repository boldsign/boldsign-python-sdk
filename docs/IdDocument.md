# IdDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**document_number** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**dob** | [**ModelDate**](ModelDate.md) |  | [optional] 
**issued_date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**expiration_date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**document_files** | **List[str]** |  | [optional] 
**selfie_file** | **str** |  | [optional] 

## Example

```python
from boldsign.models.id_document import IdDocument

# TODO update the JSON string below
json = "{}"
# create an instance of IdDocument from a JSON string
id_document_instance = IdDocument.from_json(json)
# print the JSON string representation of the object
print(IdDocument.to_json())

# convert the object into a dict
id_document_dict = id_document_instance.to_dict()
# create an instance of IdDocument from a dict
id_document_from_dict = IdDocument.from_dict(id_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


