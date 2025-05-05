import decimal
import functools

from src.util import check_arg


@functools.cache
def get_e_pre_computed() -> decimal.Decimal:
  """Compute e with 3000 digit precision using Taylor series."""
  PRECISION = 3000

  decimal.getcontext().prec = PRECISION
  e_value = decimal.Decimal(1)

  factorial = decimal.Decimal(1)
  for i in range(1, PRECISION):
    factorial *= i
    e_value += decimal.Decimal(1) / factorial
  return e_value


@functools.cache
def e(digits: int) -> str:
  """Return e upto nth digit using precomputed value."""

  check_arg(digits, int)

  e_value = get_e_pre_computed()

  digits = abs(digits)
  if digits == 1:
    return str(e_value)[0]

  return str(e_value)[: digits + 1]


def main() -> None:
  while True:
    inp = input('Enter number of digits upto 1000 (q to quit): ')

    if inp.lower() == 'q':
      break

    MAX_DIGITS = 1000
    try:
      digits = int(inp)
      if not (0 < digits <= MAX_DIGITS):
        raise ValueError()
      print(e(digits))
    except ValueError:
      print('digits must be a positive integer upto 1000')


if __name__ == '__main__':
  main()
