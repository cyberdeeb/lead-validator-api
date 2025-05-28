from django.test import TestCase
from api.utils import verify_email, verify_phone_number

class VerifyUtilsTests(TestCase):
    def test_verify_email_valid(self):
        result = verify_email("test@example.com")
        self.assertIsInstance(result, dict)
        # Optionally check expected keys
        self.assertIn("is_valid", result)

    def test_verify_phone_valid(self):
        result = verify_phone_number("+14155552671")
        self.assertIsInstance(result, dict)
        self.assertIn("carrier", result)  # Example expected key
