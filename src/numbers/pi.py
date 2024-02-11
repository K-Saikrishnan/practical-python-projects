import decimal
import math


def binary_split(a: int, b: int) -> tuple[int, int, int]:
  """Binary split algorithm used in Chudnovsky algorithm to compute pi."""

  if b == a + 1:
    Pab = -(6 * a - 5) * (2 * a - 1) * (6 * a - 1)
    Qab = 10939058860032000 * a**3
    Rab = Pab * (545140134 * a + 13591409)
  else:
    m = (a + b) // 2
    Pam, Qam, Ram = binary_split(a, m)
    Pmb, Qmb, Rmb = binary_split(m, b)

    Pab = Pam * Pmb
    Qab = Qam * Qmb
    Rab = Qmb * Ram + Pam * Rmb
  return Pab, Qab, Rab


def chudnovsky(digits: int) -> decimal.Decimal:
  """Compute pi upto nth digit using Chudnovsky algorithm."""
  decimal.getcontext().prec = digits + 2  # Add extra precision to avoid rounding errors

  _, Q1n, R1n = binary_split(1, digits)
  pi = (426880 * decimal.Decimal(10005).sqrt() * Q1n) / (13591409 * Q1n + R1n)
  return decimal.Decimal(str(pi)[:-2])  # Remove extra precision


def pi(digits: int = 15) -> decimal.Decimal:
  """Compute pi upto 1000 digits. Calculates the 1st 15 digits using math.pi builtin.  For >16 digits, uses the Chudnovsky algorithm."""

  BUILTIN_PI_DIGITS = 15

  if digits <= BUILTIN_PI_DIGITS:
    return decimal.Decimal(str(math.pi)[: digits + 1])  # Add 1 to include the dot

  return chudnovsky(digits)


def main() -> None:
  while True:
    inp = input('Enter number of digits (q or Q to quit): ')

    if inp.lower() == 'q':
      break

    MAX_DIGITS = 1000
    try:
      digits = int(inp)
      if not (0 < digits <= MAX_DIGITS):
        raise ValueError()
      print(pi(digits))
    except ValueError:
      print('digits must be a positive integer upto 1000')


if __name__ == '__main__':
  main()
