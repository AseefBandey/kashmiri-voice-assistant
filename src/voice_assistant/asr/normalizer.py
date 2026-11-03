"""Orthographic normalizer and text cleaning for Kashmiri ASR transcriptions."""
import re
import unicodedata


class KashmiriTextNormalizer:
    """Normalizes Arabic/Perso-Arabic script orthographic variations for Kashmiri."""

    CHAR_MAP = {
        "\u064a": "\u06cc",  # Arabic Yeh to Farsi/Kashmiri Yeh
        "\u0649": "\u06cc",  # Alef Maksura to Yeh
        "\u0643": "\u06a9",  # Arabic Kaf to Keheh
        "\u06c0": "\u06c1",  # Heh with Yeh above to Heh goal
    }

    def __init__(self, remove_diacritics: bool = False):
        self.remove_diacritics = remove_diacritics

    def normalize(self, text: str) -> str:
        """Clean and normalize transcript text."""
        if not text:
            return ""

        # Unicode normalization
        text = unicodedata.normalize("NFC", text)

        # Standardize characters
        for src, dst in self.CHAR_MAP.items():
            text = text.replace(src, dst)

        # Remove extra whitespace
        text = re.sub(r"\s+", " ", text).strip()

        return text
