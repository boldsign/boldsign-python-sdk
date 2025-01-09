# Template


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | [optional] 
**sender_detail** | [**TemplateSenderDetails**](TemplateSenderDetails.md) |  | [optional] 
**cc_details** | [**List[TemplateCC]**](TemplateCC.md) |  | [optional] 
**created_date** | **int** |  | [optional] 
**activity_date** | **int** |  | [optional] 
**activity_by** | **str** |  | [optional] 
**message_title** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**signer_details** | [**List[TemplateSignerDetails]**](TemplateSignerDetails.md) |  | [optional] 
**enable_signing_order** | **bool** |  | [optional] 
**template_name** | **str** |  | [optional] 
**template_description** | **str** |  | [optional] 
**access_type** | **str** |  | [optional] 
**access_tid** | **str** |  | [optional] 
**is_template** | **bool** |  | [optional] [default to False]
**behalf_of** | [**BehalfOf**](BehalfOf.md) |  | [optional] 
**template_labels** | **List[str]** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**brand_id** | **str** |  | [optional] 

## Example

```python
from boldsign.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


