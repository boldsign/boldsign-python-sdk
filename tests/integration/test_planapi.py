import unittest
import pytest
import boldsign
import os
import time
from boldsign.rest import ApiException

APIKey = os.getenv('BoldSignAPIKey')
url = os.getenv('BoldSignURL')

@pytest.mark.integration
class TestPlanApi(unittest.TestCase):
    
    def setUp(self):
        self.configuration = boldsign.Configuration(api_key=APIKey, host=url)
        self.api_client = boldsign.ApiClient(self.configuration)

    @pytest.mark.run(order=109)
    def test_api_credits_count_positive(self):
        try:
            self.plan_api = boldsign.PlanApi(self.api_client)
            
            plan_api_credits_count_get_response = self.plan_api.api_credits_count()        
            assert isinstance(plan_api_credits_count_get_response, boldsign.BillingViewModel)
            assert plan_api_credits_count_get_response is not None           

        except ApiException as e:
            print("\nException when calling BoldSign API: %s" % e)
            assert False, f"API Exception occurred: {str(e)}"
        except Exception as e:
            print("\nException when calling BoldSign: %s" % e)
            assert False, f"Unexpected exception occurred: {str(e)}"
        finally:
            time.sleep(10)


if __name__ == '__main__':
    unittest.main()