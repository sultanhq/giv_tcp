import unittest

from GivTCP.retry_utils import initial_connection_retry_delay


class RetryDelayTests(unittest.TestCase):
    def test_uses_refresh_period_when_in_range(self):
        self.assertEqual(30.0, initial_connection_retry_delay(30))

    def test_applies_minimum_delay(self):
        self.assertEqual(5.0, initial_connection_retry_delay(2))

    def test_applies_maximum_delay(self):
        self.assertEqual(60.0, initial_connection_retry_delay(120))

    def test_invalid_values_use_fallback(self):
        self.assertEqual(15.0, initial_connection_retry_delay("bad"))


if __name__ == "__main__":
    unittest.main()
