#!/usr/bin/env python3
"""Entry program for the make.fun bounty "One Emoji, One Smile".

Writes exactly one emoji to /output/entry.txt and nothing else:
no words, no caption, no trailing newline. The chosen emoji is the
face holding back tears (U+1F979), picked to read as warm at a glance.

The program verifies its own output before finishing: the file must
decode as UTF-8, hold exactly one character, contain no whitespace
or line breaks, and match the intended bytes exactly on read-back.
Only the Python standard library is used.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The entry itself: a single emoji, assembled from its code point so
# the source stays explicit about exactly which character is sent.
EMOJI_CODEPOINT = 0x1F979  # FACE HOLDING BACK TEARS
ENTRY = chr(EMOJI_CODEPOINT)


def validate(text: str) -> None:
    """Raise ValueError unless text is exactly the intended emoji."""
    if text != ENTRY:
        raise ValueError("entry text does not match the intended emoji")
    if len(text) != 1:
        raise ValueError("entry must be exactly one character")
    # Verify the code point itself, not just string equality: a single
    # character must be exactly U+1F979 and encode to the known 4-byte
    # UTF-8 sequence, so a look-alike or normalised variant cannot pass.
    if ord(text) != EMOJI_CODEPOINT:
        raise ValueError("entry code point is not U+1F979")
    if text.encode("utf-8") != b"\xf0\x9f\xa5\xb9":
        raise ValueError("entry UTF-8 bytes are not the expected 4 bytes")
    if text.strip() != text or any(ch.isspace() for ch in text):
        raise ValueError("entry must not contain whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must not contain line breaks")
    if not (1 <= len(text) <= 8):
        raise ValueError("entry is outside the gate's 1-8 character range")
    if text.encode("utf-8").decode("utf-8") != text:
        raise ValueError("entry does not survive a UTF-8 round trip")
    # Grapheme check: one code point with no combining marks, zero-width
    # joiner, or variation selector is exactly one grapheme cluster, so
    # the entry cannot render as (or be counted as) more than one emoji.
    import unicodedata

    if unicodedata.combining(text):
        raise ValueError("entry must not carry a combining mark")
    if any(ord(ch) in (0x200D, 0xFE0E, 0xFE0F) for ch in text):
        raise ValueError("entry must not contain a joiner or variation selector")


def main() -> None:
    validate(ENTRY)
    expected = ENTRY.encode("utf-8")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(expected)
    written = OUTPUT_PATH.read_bytes()
    if written != expected:
        raise ValueError("read-back bytes differ from the intended bytes")
    validate(written.decode("utf-8"))


if __name__ == "__main__":
    main()
