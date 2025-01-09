import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:
    
    custom_field_api = boldsign.CustomFieldApi(api_client)
    
    custom_form_fields = boldsign.CustomFormField(
        fieldType="Signature",
        width= 60,
        height=60,
        isRequired=True,
        isReadOnly=True,
        value="string",
        lineHeight=15,
        characterLimit=0,
        placeHolder="string",
        validationType="NumbersOnly",
        validationCustomRegex="string",
        validationCustomRegexMessage="string",
        textAlign="Center",
        textDirection="LTR",
        characterSpacing=0,
        idPrefix="string",
        restrictIdPrefixChange=False,
    )
    
    brand_custom_field_details_request = boldsign.BrandCustomFieldDetails(
        fieldName="string",
        fieldDescription="string",
        fieldOrder=1,
        brandId="a10f3ce5-03c1-4bf7-bc71-4a36cf97de0f",
        sharedField=True,
        formField=custom_form_fields
    )   
    
    create_custom_field_details_response = custom_field_api.create_custom_field(
        brand_custom_field_details=brand_custom_field_details_request
    )
    
    print(f"Custom field successfully created:{create_custom_field_details_response}")