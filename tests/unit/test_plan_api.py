import unittest
from unittest.mock import patch, MagicMock
import pytest
import boldsign
from boldsign.models.billing_view_model import BillingViewModel
from boldsign.rest import ApiException

class TestPlanApi(unittest.TestCase):

    def setUp(self):
        self.api_client = MagicMock()
        self.plan_api = boldsign.PlanApi(api_client=self.api_client)

    @patch('boldsign.PlanApi.api_credits_count')
    @pytest.mark.unit
    def test_api_credits_count_success(self, mock_credits_count_get):
        # Mocking the response
        mock_response = BillingViewModel(balance_credits=100)
        mock_credits_count_get.return_value = mock_response

        # Call the method
        response = self.plan_api.api_credits_count()

        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(response.balance_credits, 100)
        mock_credits_count_get.assert_called_once()

    @patch('boldsign.PlanApi.api_credits_count')
    @pytest.mark.unit
    def test_api_credits_count_unauthorized(self, mock_credits_count_get):
        # Mocking the ApiException for unauthorized access
        mock_credits_count_get.side_effect = ApiException(status=401, reason="Unauthorized")

        # Call the method and assert exception
        with self.assertRaises(ApiException) as context:
            self.plan_api.api_credits_count()

        self.assertEqual(context.exception.status, 401)
        self.assertEqual(context.exception.reason, "Unauthorized")
        mock_credits_count_get.assert_called_once()

    @patch('boldsign.PlanApi.api_credits_count')
    @pytest.mark.unit
    def test_api_credits_count_server_error(self, mock_credits_count_get):
        # Mocking the ApiException for server error
        mock_credits_count_get.side_effect = ApiException(status=500, reason="Internal Server Error")

        # Call the method and assert exception
        with self.assertRaises(ApiException) as context:
            self.plan_api.api_credits_count()

        self.assertEqual(context.exception.status, 500)
        self.assertEqual(context.exception.reason, "Internal Server Error")
        mock_credits_count_get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
