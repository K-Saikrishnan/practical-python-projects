from src.text import word_count


class TestWordCount:
  def test_word_count(self):
    assert word_count.word_count('') == 0
    assert word_count.word_count('Hello') == 1
    assert word_count.word_count('Hello World') == 2
    assert word_count.word_count('Hello World!') == 2
    assert word_count.word_count('Hello World! ') == 2


class TestWordCountFile:
  def test_word_count_file(self):
    assert word_count.word_count_file('./tests/mocks/lorem-ipsum.txt') == 1000
