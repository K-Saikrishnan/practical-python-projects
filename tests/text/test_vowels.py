from src.text import vowels


class TestVowels:
  def test_vowels_frequency(self):
    assert vowels.vowels_frequency('Hello World!') == {'e': 1, 'o': 2}
    assert vowels.vowels_frequency('') == {}
    assert vowels.vowels_frequency('123') == {}
    assert vowels.vowels_frequency('aeiou') == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

  def test_count_vowels(self):
    assert vowels.count_vowels('Hello World!') == 3
    assert vowels.count_vowels('') == 0
    assert vowels.count_vowels('123') == 0
    assert vowels.count_vowels('aeiou') == 5
