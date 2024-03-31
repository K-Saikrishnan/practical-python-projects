import typing


def check_arg(value: typing.Any, expected_type: typing.Any) -> None:
  """Checks if the value is of the expected type."""

  if not isinstance(value, expected_type):
    raise TypeError(f'{value} must be a {expected_type.__name__}')
