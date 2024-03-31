from src.util import check_arg


def reverse_string(text: str) -> str:
  """Reverses a string. Raises TypeError if input is not a string."""

  check_arg(text, str)

  return text[::-1]
