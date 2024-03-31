import pytest

from src.util import check_arg


def test_check_arg():
  check_arg(1, int)
  check_arg(1.0, float)
  check_arg('1', str)

  with pytest.raises(TypeError):
    check_arg(1, float)
  with pytest.raises(TypeError):
    check_arg(1.0, int)
