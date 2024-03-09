def word_count(text: str) -> int:
  """Count the number of words in a string."""

  if not isinstance(text, str):
    raise TypeError('Input must be a string')

  return len(text.strip().split())


def word_count_file(file_path: str) -> int:
  """Count the number of words in a file."""

  if not isinstance(file_path, str):
    raise TypeError('Input must be a string')

  with open(file_path) as file:
    return word_count(file.read())
