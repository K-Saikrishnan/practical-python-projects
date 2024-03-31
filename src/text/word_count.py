from src.util import check_arg


def word_count(text: str) -> int:
  """Count the number of words in a string."""

  check_arg(text, str)

  return len(text.strip().split())


def word_count_file(file_path: str) -> int:
  """Count the number of words in a file."""

  check_arg(file_path, str)

  with open(file_path) as file:
    return word_count(file.read())
