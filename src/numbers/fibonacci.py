import functools

MAX_COUNT = 1000


@functools.lru_cache(maxsize=MAX_COUNT)
def fibonacci(n: int) -> int:
  """Return the nth Fibonacci number."""

  if n < 2:  # noqa: PLR2004
    return n

  return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
  while True:
    inp = input(f'Enter n upto {MAX_COUNT} (q to quit): ')

    if inp.lower() == 'q':
      break

    try:
      n = int(inp)
      if not (0 < n <= MAX_COUNT):
        raise ValueError()
      for i in range(n):
        print(fibonacci(i))
    except ValueError:
      print(f'n must be a positive integer upto {MAX_COUNT}')


if __name__ == '__main__':
  main()
