"""Sanity test verifying environment and test harness."""
import unittest


class TestSanity(unittest.TestCase):
    def test_environment(self):
        """Verify basic math and test execution."""
        self.assertEqual(1 + 1, 2)


if __name__ == "__main__":
    unittest.main()
