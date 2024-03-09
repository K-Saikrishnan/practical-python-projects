import pytest

from src.text import word_count


class TestWordCount:
  def test_word_count(self):
    assert word_count.word_count('') == 0
    assert word_count.word_count('Hello') == 1
    assert word_count.word_count('Hello World') == 2
    assert word_count.word_count('Hello World!') == 2
    assert word_count.word_count('Hello World! ') == 2

  def test_raises_exception(self):
    with pytest.raises(TypeError) as exc:
      word_count.word_count(1)

    assert str(exc.value) == 'Input must be a string'


class TestWordCountFile:
  def test_word_count_file(self):
    assert word_count.word_count_file('./tests/mocks/lorem-ipsum.txt') == 1000

  def test_raises_exception(self):
    with pytest.raises(TypeError) as exc:
      word_count.word_count_file(1)

    assert str(exc.value) == 'Input must be a string'
