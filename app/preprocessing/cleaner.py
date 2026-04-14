import re
import unicodedata


class TextCleaner:
    """
    Normalizes input text to reduce obfuscation and improve rule matching.
    """

    def clean(self, text: str) -> str:
        if not text:
            return ""

        # --- Explicit homoglyph normalization ---
        homoglyph_map = str.maketrans({
            "ø": "o",
            "ñ": "n",
            "ï": "i",
            "ö": "o",
            "ä": "a",
            "é": "e",
            "è": "e",
            "ê": "e",
            "á": "a",
            "à": "a",
            "â": "a",
            "ú": "u",
            "ù": "u",
            "û": "u",
            "ß": "ss",
            "æ": "ae",
        })
        text = text.translate(homoglyph_map)

        # --- Unicode normalization ---
        text = unicodedata.normalize("NFKD", text)
        text = text.encode("ascii", "ignore").decode("ascii")

        # --- Lowercase ---
        text = text.lower()

        # --- Leetspeak normalization (EXTENDED) ---
        leet_map = str.maketrans({
            "0": "o",
            "1": "i",
            "3": "e",
            "4": "a",
            "5": "s",
            "7": "t",
            "$": "s",
            "@": "a",
            "!": "i",
        })
        text = text.translate(leet_map)

        # --- Normalize whitespace ---
        text = re.sub(r"\s+", " ", text)

        # --- Join spaced-out words (robust) ---
        text = re.sub(
            r"(\b[a-z]\s+){2,}[a-z]\b",
            lambda m: m.group(0).replace(" ", ""),
            text
        )

        # --- Preserve separators for obfuscation detection ---
        # (do NOT remove dots/underscores/hyphens completely)
        text = re.sub(r"[^\w\s\.\-\_]", "", text)

        return text.strip()