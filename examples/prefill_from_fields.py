import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

#Prefilling a textbox form field is a straightforward process. You need to provide the id of the form field and the value you want to assign to it.
with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)
    
    prefill_field = boldsign.PrefillField(
        id="textbox_mShRr",
        value="Prefill value"
    )
    
    prefill_field_requests = boldsign.PrefillFieldRequest(
        fields=[prefill_field]
    )
    
    documentId = "YOUR_DOCUMENT_ID"
    
    prefill_fields_response = document_api.prefill_fields(
        document_id=documentId,
        prefill_field_request =prefill_field_requests
    )

#To prefill a checkbox form field, you will need to provide the id of the form field and its value. The id must match exactly with the checkbox's id in your document, while the value should be either "ON" (to check the box) or "OFF" (to uncheck it).    
with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)
    
    prefill_field = boldsign.PrefillField(
        id="checkbox_b5yuo",
        value="ON"
    )
    
    prefill_field_requests = boldsign.PrefillFieldRequest(
        fields=[prefill_field]
    )
    
    documentId = "YOUR_DOCUMENT_ID"
    
    prefill_fields_response = document_api.prefill_fields(
        
        document_id=documentId,
        prefill_field_request =prefill_field_requests
    )

#Prefilling a Radio button form field 
with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)
    
    prefill_field = boldsign.PrefillField(
        id="radioChild_AknIg",
        value="ON"
    )
    
    prefill_field_requests = boldsign.PrefillFieldRequest(
        fields=[prefill_field]
    )
    
    documentId = "YOUR_DOCUMENT_ID"
    
    prefill_fields_response = document_api.prefill_fields(
        document_id=documentId,
        prefill_field_request =prefill_field_requests
    )

#Prefilling a Radio button form field 
with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)
    
    prefill_field = boldsign.PrefillField(
        id="radioChild_AknIg",
        value="ON"
    )
    
    prefill_field_requests = boldsign.PrefillFieldRequest(
        fields=[prefill_field]
    )
    
    documentId = "YOUR_DOCUMENT_ID"
    
    prefill_fields_response = document_api.prefill_fields(
        document_id=documentId,
        prefill_field_request =prefill_field_requests
    )

#Prefilling a Radio button with group name form field 
with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)
    
    prefill_field = boldsign.PrefillField(
        id="CodingExpertise",
        value="Intermediate"
    )
    prefill_field_requests = boldsign.PrefillFieldRequest(
        fields=[prefill_field]
    )
    
    documentId = "YOUR_DOCUMENT_ID"
    
    prefill_fields_response = document_api.prefill_fields(
        document_id=documentId,
        prefill_field_request =prefill_field_requests
    )

#Prefilling a Editable date form field 
with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)
    
    prefill_field = boldsign.PrefillField(
        id="editableDate_67P9d",
        value="02/19/2024"
    )
    
    prefill_field_requests = boldsign.PrefillFieldRequest(
        fields=[prefill_field]
    )
    
    documentId = "YOUR_DOCUMENT_ID"
    
    prefill_fields_response = document_api.prefill_fields(
        document_id=documentId,
        prefill_field_request =prefill_field_requests
    )

#Prefilling a Dropdown form field 
with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)
    
    prefill_field = boldsign.PrefillField(
        id="dropdown_qrsr1",
        value="option1"
    )
    
    prefill_field_requests = boldsign.PrefillFieldRequest(
        fields=[prefill_field]
    )
    
    documentId = "YOUR_DOCUMENT_ID"
    
    prefill_fields_response = document_api.prefill_fields(
        document_id=documentId,
        prefill_field_request =prefill_field_requests
    )

#Prefilling a Image form field 
with boldsign.ApiClient(configuration) as api_client:

    document_api = boldsign.DocumentApi(api_client)
    
    prefill_field = boldsign.PrefillField(
        id="image_6Ogud",
        value="YOUR_IMAGE_VALUE"
    )
    
    prefill_field_requests = boldsign.PrefillFieldRequest(
        fields=[prefill_field]
    )
    
    documentId = "YOUR_DOCUMENT_ID"
    
    prefill_fields_response = document_api.prefill_fields(
        document_id=documentId,
        prefill_field_request =prefill_field_requests
    )