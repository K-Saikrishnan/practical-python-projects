from src.text.reverse_string import reverse_string


class TestReverseString:
  def test_reverse_string(self):
    assert reverse_string('') == ''
    assert reverse_string('1') == '1'
    assert reverse_string('hello') == 'olleh'
    assert reverse_string('hello world') == 'dlrow olleh'
    assert reverse_string('1234567890') == '0987654321'
    assert reverse_string('h') == 'h'

  def test_reverse_string_raises_type_error(self):
    try:
      reverse_string(1)
    except TypeError as e:
      assert str(e) == 'Input must be a string'
