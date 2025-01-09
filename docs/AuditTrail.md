# AuditTrail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**to_name** | **str** |  | [optional] 
**to_email** | **str** |  | [optional] 
**ipaddress** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from boldsign.models.audit_trail import AuditTrail

# TODO update the JSON string below
json = "{}"
# create an instance of AuditTrail from a JSON string
audit_trail_instance = AuditTrail.from_json(json)
# print the JSON string representation of the object
print(AuditTrail.to_json())

# convert the object into a dict
audit_trail_dict = audit_trail_instance.to_dict()
# create an instance of AuditTrail from a dict
audit_trail_from_dict = AuditTrail.from_dict(audit_trail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


