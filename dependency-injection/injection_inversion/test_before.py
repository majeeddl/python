import unittest
from io import StringIO
from unittest.mock import patch
from before import *


class Authorizer_SMS_TestCase(unittest.TestCase):

    def test_init_authorized(self):
        auth = Authorizer_SMS()
        self.assertFalse(auth.is_authorized())

    def test_code_decimal(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        self.assertTrue(auth.code.isdecimal())

    def test_authorize_success(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()

        with patch('builtins.input', return_value=auth.code):
            auth.authorize()
            self.assertTrue(auth.is_authorized())

    @patch('builtins.input', return_value='1234567')
    def test_authorized_fail(self, mock_input):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        auth.authorize()

        self.assertFalse(auth.is_authorized())


class PaymentProcessor_TestCase(unittest.TestCase):

    def test_payment_success(self):
        # ???
        self.assertTrue(True)

    def test_payment(self):
        # ???
        self.assertTrue(True)
