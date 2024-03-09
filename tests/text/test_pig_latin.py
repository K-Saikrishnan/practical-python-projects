import pytest

from src.text import pig_latin


class TestPigLatinWord:
  def test_empty(self):
    assert pig_latin.word('') == ''

  def test_single_letter(self):
    assert pig_latin.word('a') == 'away'
    assert pig_latin.word('b') == 'bay'

  def test_vowels(self):
    assert pig_latin.word('eat') == 'eatway'
    assert pig_latin.word('omelet') == 'omeletway'
    assert pig_latin.word('are') == 'areway'

  def test_consonants(self):
    assert pig_latin.word('pig') == 'igpay'
    assert pig_latin.word('latin') == 'atinlay'
    assert pig_latin.word('banana') == 'ananabay'

  def test_consonant_cluster(self):
    assert pig_latin.word('friends') == 'iendsfray'
    assert pig_latin.word('smile') == 'ilesmay'
    assert pig_latin.word('string') == 'ingstray'
    assert pig_latin.word('dry') == 'dryay'

  def test_raises_exception(self):
    with pytest.raises(TypeError) as err:
      pig_latin.word(123)

    assert str(err.value) == 'Input must be a string'


class TestPigLatinSentence:
  def test_empty(self):
    assert pig_latin.sentence('') == ''

  def test_single_word(self):
    assert pig_latin.sentence('hello') == 'ellohay'

  def test_multiple_words(self):
    assert pig_latin.sentence('hello world') == 'ellohay orldway'

  def test_raises_exception(self):
    with pytest.raises(TypeError) as err:
      pig_latin.sentence(123)

    assert str(err.value) == 'Input must be a string'
