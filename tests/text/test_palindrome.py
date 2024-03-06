import pytest

from src.text import palindrome


@pytest.mark.parametrize(
  'text, expected',
  [
    ('', True),
    ('a', True),
    ('abba', True),
    ('madam', True),
    ('racecar', True),
    ('12321', True),
    ('hello', False),
    ('ab', False),
    ('123', False),
  ],
)
def test_check_palindrome(text, expected):
  assert palindrome.check_palindrome(text) == expected


def test_check_palindrome_type_error():
  with pytest.raises(TypeError) as err:
    palindrome.check_palindrome(123)
  with pytest.raises(TypeError):
    palindrome.check_palindrome(['hello'])
  with pytest.raises(TypeError):
    palindrome.check_palindrome({'hello': 'world'})

  assert str(err.value) == 'Input must be a string'
