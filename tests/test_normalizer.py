"""Tests for Kashmiri text normalization."""
import unittest
from voice_assistant.asr.normalizer import KashmiriTextNormalizer


class TestKashmiriTextNormalizer(unittest.TestCase):
    def setUp(self):
        self.normalizer = KashmiriTextNormalizer()

    def test_empty_string(self):
        self.assertEqual(self.normalizer.normalize(""), "")

    def test_arabic_yeh_replacement(self):
        arabic_text = "\u064a"  # Arabic Yeh
        expected = "\u06cc"     # Kashmiri Yeh
        self.assertEqual(self.normalizer.normalize(arabic_text), expected)

    def test_whitespace_trim(self):
        text = "  کٲشُر   کَتھ  "
        self.assertEqual(self.normalizer.normalize(text), "کٲشُر کَتھ")


if __name__ == "__main__":
    unittest.main()
