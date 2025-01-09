# BehalfDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**behalf_of** | [**BehalfOf**](BehalfOf.md) |  | [optional] 
**document_id** | **str** |  | [optional] 
**sender_detail** | [**DocumentSenderDetail**](DocumentSenderDetail.md) |  | [optional] 
**cc_details** | [**List[DocumentCcDetails]**](DocumentCcDetails.md) |  | [optional] 
**created_date** | **int** |  | [optional] 
**activity_date** | **int** |  | [optional] 
**activity_by** | **str** |  | [optional] 
**message_title** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**signer_details** | [**List[DocumentSignerDetails]**](DocumentSignerDetails.md) |  | [optional] 
**expiry_date** | **int** |  | [optional] 
**enable_signing_order** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**cursor** | **int** |  | [optional] 
**brand_id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.behalf_document import BehalfDocument

# TODO update the JSON string below
json = "{}"
# create an instance of BehalfDocument from a JSON string
behalf_document_instance = BehalfDocument.from_json(json)
# print the JSON string representation of the object
print(BehalfDocument.to_json())

# convert the object into a dict
behalf_document_dict = behalf_document_instance.to_dict()
# create an instance of BehalfDocument from a dict
behalf_document_from_dict = BehalfDocument.from_dict(behalf_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


