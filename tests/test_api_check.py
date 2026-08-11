import unittest

from Core.Support import ApiCheck


class ApiCheckFallbackTests(unittest.TestCase):
    def test_missing_api_key_returns_none_marker(self):
        self.assertEqual(ApiCheck.Check.WhoIs(), "None")


if __name__ == "__main__":
    unittest.main()
