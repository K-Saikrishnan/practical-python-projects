def reverse_string(text: str) -> str:
  """Reverses a string. Raises TypeError if input is not a string."""

  if not isinstance(text, str):
    raise TypeError('Input must be a string')
  return text[::-1]
