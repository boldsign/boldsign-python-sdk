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
        font="Courier",
         width= 60,
        height=60,
        isRequired=True,
        isReadOnly=True,
        value="string",
        fontSize=13,
        fontHexColor="string",
        isBoldFont=True,
        isItalicFont=True,
        isUnderLineFont=True,
        lineHeight=15,
        characterLimit=0,
        placeHolder="string",
        validationType="NumbersOnly",
        validationCustomRegex="string",
        validationCustomRegexMessage="string",
        dateFormat="string",
        timeFormat="string",
        imageInfo=boldsign.ImageInfo(
            allowedFileExtensions="string",
            title="string",
            description="string"
        ),
        attachmentInfo=boldsign.AttachmentInfo(
            allowedFileTypes="string",
            title="string",
            description="string",
            acceptedFileTypes=[
                "string",
                "string"
            ]
        ),
        hyperlinkText="string",
        dataSyncTag="string",
        dropdownOptions=[
            "string",
            "string"
        ],
        textAlign="Center",
        textDirection="LTR",
        characterSpacing=0,
        idPrefix="string",
        restrictIdPrefixChange=False,
         backgroundHexColor="string"
    )

    edit_custom_field_details_request = boldsign.BrandCustomFieldDetails(
        fieldName="string",
        fieldDescription="string",
        fieldOrder=1,
        brandId="YOUR_BRAND_ID",
        sharedField=True,
        formField=custom_form_fields
    )
    
    edit_custom_field_details_response = custom_field_api.edit_custom_field(
        custom_field_id="CUSTOM_FIELD_ID",
        brand_custom_field_details=edit_custom_field_details_request
    )
    
    print(f"Custom field successfully updated:{edit_custom_field_details_response}")