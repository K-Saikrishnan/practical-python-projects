from collections import Counter

VOWELS = 'aeiou'


def vowels_frequency(text: str) -> dict[str, int]:
  """Returns the frequency split of vowels in a text."""
  return dict(Counter(char for char in text.lower() if char in VOWELS))


def count_vowels(text: str) -> int:
  """Returns the total count of vowels in a text."""
  return sum(1 for char in text.lower() if char in VOWELS)


if __name__ == '__main__':
  while True:
    text = input('Enter text (q to quit): ')

    if text.lower() == 'q':
      break
    if text == '':
      continue

    print(f'Frequency: {vowels_frequency(text)}')
    print(f'Count: {count_vowels(text)}')
