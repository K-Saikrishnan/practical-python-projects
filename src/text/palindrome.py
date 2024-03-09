def check_palindrome(text: str) -> bool:
  """Checks if a string is a palindrome."""

  if not isinstance(text, str):
    raise TypeError('Input must be a string')
  return text == text[::-1]
