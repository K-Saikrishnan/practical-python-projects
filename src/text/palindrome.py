from src.util import check_arg


def check_palindrome(text: str) -> bool:
  """Checks if a string is a palindrome."""

  check_arg(text, str)

  return text == text[::-1]
