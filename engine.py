def simple_shift(text, shift):
    """
    Shift every character by 'shift' positions.

    This is a simple Caesar cipher that works on ALL printable characters,
    not just letters. It wraps around using modular arithmetic.

    Args:
        text: The string to encrypt
        shift: How many positions to shift (positive = forward)

    Returns:
        The encrypted string
    """
    result = ""

    for char in text:
        if 32 <= ord(char) <= 126:  # Printable ASCII range
            # Convert to 0-94 range
            position = ord(char) - 32
            # Shift and wrap
            new_position = (position + shift) % 95
            # Convert back to character
            result += chr(new_position + 32)
        else:
            # Keep non-printable characters unchanged
            result += char

    return result
