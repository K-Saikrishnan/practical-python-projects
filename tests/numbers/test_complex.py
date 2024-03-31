import pytest

from src.numbers import complex


class TestComplex:
  def test_add(self):
    assert complex.add(1 + 2j, 3 + 4j) == 4 + 6j
    assert complex.add(1 + 2j, 3 - 4j) == 4 - 2j

  def test_sub(self):
    assert complex.sub(1 + 2j, 3 + 4j) == -2 - 2j
    assert complex.sub(1 + 2j, 3 - 4j) == -2 + 6j

  def test_mul(self):
    assert complex.mul(1 + 2j, 3 + 4j) == -5 + 10j
    assert complex.mul(1 + 2j, 3 - 4j) == 11 + 2j

  def test_inv(self):
    assert complex.inv(1 + 2j) == 0.2 - 0.4j
    assert complex.inv(3 - 4j) == 0.12 + 0.16j

  def test_div(self):
    assert complex.div(1 + 2j, 3 + 4j) == 0.44 + 0.08j
    assert complex.div(1 + 2j, 3 - 4j) == -0.2 + 0.4j

  def test_zero_division(self):
    with pytest.raises(ZeroDivisionError):
      complex.div(1 + 2j, 0 + 0j)

    with pytest.raises(ZeroDivisionError):
      complex.inv(0 + 0j)
