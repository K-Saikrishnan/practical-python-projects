from src.util import check_arg


def word(word: str) -> str:
  """Converts a word to Pig Latin."""

  check_arg(word, str)

  if not word:
    return ''

  word = word.lower()

  VOWELS = 'aeiou'

  if word[0] in VOWELS:
    return word + 'way'
  else:
    for i, letter in enumerate(word):
      if letter in VOWELS:
        return word[i:] + word[:i] + 'ay'
    return word + 'ay'


def sentence(sentence: str) -> str:
  """Converts a sentence to Pig Latin."""

  check_arg(sentence, str)

  if not sentence:
    return ''

  return ' '.join(word(each) for each in sentence.split())
