def fizzbuzz() -> list[str]:
  """Returns FizzBuzz values from 1 to 100."""

  output = []
  for i in range(1, 101):
    value = ''
    if i % 3 == 0:
      value += 'Fizz'
    if i % 5 == 0:
      value += 'Buzz'
    if value == '':
      value = str(i)
    output.append(value)
  return output


if __name__ == '__main__':
  print('\n'.join(fizzbuzz()))
