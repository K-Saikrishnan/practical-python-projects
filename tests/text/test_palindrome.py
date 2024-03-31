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
