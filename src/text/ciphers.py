import random
import string

from src.util import check_arg


def caesar_encode(plain_text: str, key: int) -> str:
  """Encodes text using the Caesar cipher."""

  check_arg(plain_text, str)
  check_arg(key, int)

  result = ''

  for char in plain_text:
    if char.isalpha():
      start = ord('a') if char.islower() else ord('A')
      result += chr((ord(char) + key - start) % 26 + start)
    else:
      result += char

  return result


def caesar_decode(cipher_text: str, key: int) -> str:
  """Decodes text using the Caesar cipher."""

  return caesar_encode(cipher_text, -key)


def vigenere_key_ord(key: str, length: int) -> list[int]:
  """Repeats the key and returns the key shifted ordinals."""

  check_arg(key, str)
  check_arg(length, int)

  key = key.lower()
  key_repeated = repeat_key(key, length)
  return [ord(char) - ord('a') for char in key_repeated]


def vigenere_encode(plain_text: str, key: str) -> str:
  """Encodes text using the Vigenère cipher."""

  check_arg(plain_text, str)
  check_arg(key, str)

  key_ord = vigenere_key_ord(key, len(plain_text))
  cipher_text_chars = [caesar_encode(plain_char, key_char) for plain_char, key_char in zip(plain_text, key_ord)]
  return ''.join(cipher_text_chars)


def vigenere_decode(cipher_text: str, key: str) -> str:
  """Decodes text using the Vigenère cipher."""

  check_arg(cipher_text, str)
  check_arg(key, str)

  key_ord = vigenere_key_ord(key, len(cipher_text))
  plain_text_chars = [caesar_decode(cipher_char, key_char) for cipher_char, key_char in zip(cipher_text, key_ord)]
  return ''.join(plain_text_chars)


def vernam_key(length: int) -> str:
  """Generates a random key of the specified length for Vernam Cipher."""

  check_arg(length, int)

  return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def vernam(text: str, key: str) -> str:
  """Encodes/Decodes text using the Vernam cipher."""

  check_arg(text, str)
  check_arg(key, str)

  if len(text) != len(key):
    key = repeat_key(key, len(text))

  cipher_text = ''.join(str(chr(ord(plain_char) ^ ord(key_char))) for plain_char, key_char in zip(text, key))
  return cipher_text


def repeat_key(key: str, length: int) -> str:
  """Repeats the key to match the length of the text."""

  check_arg(key, str)
  check_arg(length, int)

  return key * (length // len(key)) + key[: length % len(key)]
