import string

import pytest

from src.text import ciphers


class TestCaesar:
  def test_caesar_invalid_input(self):
    with pytest.raises(TypeError):
      ciphers.caesar_encode(3, 3)
    with pytest.raises(TypeError):
      ciphers.caesar_encode('Hello, World!', '3')
    with pytest.raises(TypeError):
      ciphers.caesar_decode(3, 3)
    with pytest.raises(TypeError):
      ciphers.caesar_decode('Hello, World!', '3')

  def test_caesar_encode_no_shift(self):
    assert ciphers.caesar_encode('', 3) == ''
    assert ciphers.caesar_encode('Hello, World!', 0) == 'Hello, World!'
    assert ciphers.caesar_encode('Hello, World!', 26) == 'Hello, World!'
    assert ciphers.caesar_encode('Hello, World!', 52) == 'Hello, World!'

  def test_caesar_encode_shift(self):
    assert ciphers.caesar_encode('Hello, World!', 3) == 'Khoor, Zruog!'
    assert ciphers.caesar_encode('Hello, World!', -3) == 'Ebiil, Tloia!'

  def test_caesar_decode_no_shift(self):
    assert ciphers.caesar_decode('', 3) == ''
    assert ciphers.caesar_decode('Hello, World!', 0) == 'Hello, World!'
    assert ciphers.caesar_decode('Hello, World!', 26) == 'Hello, World!'
    assert ciphers.caesar_decode('Hello, World!', 52) == 'Hello, World!'

  def test_caesar_decode_shift(self):
    assert ciphers.caesar_decode('Khoor, Zruog!', 3) == 'Hello, World!'
    assert ciphers.caesar_decode('Hello, World!', -3) == 'Khoor, Zruog!'


class TestVigenere:
  def test_vigenere_invalid_input(self):
    with pytest.raises(TypeError):
      ciphers.vigenere_encode(3, 3)
    with pytest.raises(TypeError):
      ciphers.vigenere_encode('3', 3)
    with pytest.raises(TypeError):
      ciphers.vigenere_decode(3, 3)
    with pytest.raises(TypeError):
      ciphers.vigenere_decode('3', 3)

  def test_vigenere_encode(self):
    assert ciphers.vigenere_encode('Hello, World!', 'a') == 'Hello, World!'
    assert ciphers.vigenere_encode('Hello, World!', 'abc') == 'Hfnlp, Xqrmf!'
    assert ciphers.vigenere_encode('Hello, World!', 'abcabc') == 'Hfnlp, Xqrmf!'

  def test_vigenere_decode(self):
    assert ciphers.vigenere_decode('Hello, World!', 'a') == 'Hello, World!'
    assert ciphers.vigenere_decode('Hfnlp, Xqrmf!', 'abc') == 'Hello, World!'
    assert ciphers.vigenere_decode('Hfnlp, Xqrmf!', 'abcabc') == 'Hello, World!'
    assert ciphers.vigenere_decode('lxfopvefrnhr', 'LEMONLEMONLE') == 'attackatdawn'


class TestVernam:
  def test_vernam_invalid_input(self):
    with pytest.raises(TypeError):
      ciphers.vernam(3, 3)
    with pytest.raises(TypeError):
      ciphers.vernam('3', 3)

  def test_vernam_key(self):
    assert ciphers.vernam_key(0) == ''
    assert len(ciphers.vernam_key(100)) == 100
    assert all(char in string.ascii_lowercase for char in ciphers.vernam_key(100))

  def test_vernam(self):
    assert ciphers.vernam('Hello, world!', 'a') == ')\x04\r\r\x0eMA\x16\x0e\x13\r\x05@'
    assert ciphers.vernam(')\x04\r\r\x0eMA\x16\x0e\x13\r\x05@', 'a') == 'Hello, world!'
