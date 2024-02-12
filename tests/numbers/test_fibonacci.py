import pytest

from src.numbers import fibonacci


class TestFibonacci:
  def test_fibonacci(self):
    FIBONACCI_HUNDRED = 354224848179261915075
    assert fibonacci.fibonacci(0) == 0
    assert fibonacci.fibonacci(1) == 1
    assert fibonacci.fibonacci(2) == 1
    assert fibonacci.fibonacci(100) == FIBONACCI_HUNDRED


class TestMain:
  def test_main(self, mocker, capfd):
    mocker.patch('builtins.input', side_effect=['5', 'q'])
    fibonacci.main()
    out, err = capfd.readouterr()
    assert out == '0\n1\n1\n2\n3\n'
    assert err == ''

  @pytest.mark.parametrize('inp', ['-10', '0', '1001'])
  def test_main_invalid_input(self, mocker, capfd, inp):
    mocker.patch('builtins.input', side_effect=[inp, 'q'])
    fibonacci.main()
    out, err = capfd.readouterr()
    assert out == 'n must be a positive integer upto 1000\n'
    assert err == ''
