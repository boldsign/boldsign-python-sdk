import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:

    template_api = boldsign.TemplateApi(api_client)
    
    templateTag = boldsign.TemplateTag(
        templateId="c7de007a-3a19-4f5d-bd37-994d2186a2b3",
        documentLabels=[
            "test",
            "api"
        ],        
        templateLabels=[
            "test",
            "api"
        ]
    )
    templates = template_api.add_tag(template_tag=templateTag)

    print(f"Templates tags successfully added")