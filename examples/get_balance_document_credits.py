import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import boldsign

configuration = boldsign.Configuration(
    api_key = os.getenv('BoldSignAPIKey'),
    host=os.getenv('BoldSignApiUrl')
)

with boldsign.ApiClient(configuration) as api_client:
    
    plan_api = boldsign.PlanApi(api_client)
    
    plan_api_credits_count_response = plan_api.api_credits_count()
    
    print(f"Plan api credits count:{plan_api_credits_count_response}")