# DocumentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | 
**title** | **str** |  | 
**language** | **int** | &lt;p&gt;Description:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;&lt;i&gt;0&lt;/i&gt; - None&lt;/li&gt;&lt;li&gt;&lt;i&gt;1&lt;/i&gt; - English&lt;/li&gt;&lt;li&gt;&lt;i&gt;2&lt;/i&gt; - Spanish&lt;/li&gt;&lt;li&gt;&lt;i&gt;3&lt;/i&gt; - German&lt;/li&gt;&lt;li&gt;&lt;i&gt;4&lt;/i&gt; - French&lt;/li&gt;&lt;li&gt;&lt;i&gt;5&lt;/i&gt; - Romanian&lt;/li&gt;&lt;li&gt;&lt;i&gt;6&lt;/i&gt; - Norwegian&lt;/li&gt;&lt;li&gt;&lt;i&gt;7&lt;/i&gt; - Bulgarian&lt;/li&gt;&lt;li&gt;&lt;i&gt;8&lt;/i&gt; - Italian&lt;/li&gt;&lt;li&gt;&lt;i&gt;9&lt;/i&gt; - Danish&lt;/li&gt;&lt;li&gt;&lt;i&gt;10&lt;/i&gt; - Polish&lt;/li&gt;&lt;li&gt;&lt;i&gt;11&lt;/i&gt; - Portuguese&lt;/li&gt;&lt;li&gt;&lt;i&gt;12&lt;/i&gt; - Czech&lt;/li&gt;&lt;li&gt;&lt;i&gt;13&lt;/i&gt; - Dutch&lt;/li&gt;&lt;li&gt;&lt;i&gt;14&lt;/i&gt; - Swedish&lt;/li&gt;&lt;li&gt;&lt;i&gt;15&lt;/i&gt; - Russian&lt;/li&gt;&lt;li&gt;&lt;i&gt;16&lt;/i&gt; - Japanese&lt;/li&gt;&lt;li&gt;&lt;i&gt;17&lt;/i&gt; - Thai&lt;/li&gt;&lt;li&gt;&lt;i&gt;18&lt;/i&gt; - SimplifiedChinese&lt;/li&gt;&lt;li&gt;&lt;i&gt;19&lt;/i&gt; - TraditionalChinese&lt;/li&gt;&lt;li&gt;&lt;i&gt;20&lt;/i&gt; - Korean&lt;/li&gt;&lt;/ul&gt; | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from boldsign.models.document_info import DocumentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentInfo from a JSON string
document_info_instance = DocumentInfo.from_json(json)
# print the JSON string representation of the object
print(DocumentInfo.to_json())

# convert the object into a dict
document_info_dict = document_info_instance.to_dict()
# create an instance of DocumentInfo from a dict
document_info_from_dict = DocumentInfo.from_dict(document_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


