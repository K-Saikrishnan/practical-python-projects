import pytest

from src.numbers import e


@pytest.fixture()
def e_1000_digits():
  return '2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819025515108657463772111252389784425056953696770785449969967946864454905987931636889230098793127736178215424999229576351482208269895193668033182528869398496465105820939239829488793320362509443117301238197068416140397019837679320683282376464804295311802328782509819455815301756717361332069811250996181881593041690351598888519345807273866738589422879228499892086805825749279610484198444363463244968487560233624827041978623209002160990235304369941849146314093431738143640546253152096183690888707016768396424378140592714563549061303107208510383750510115747704171898610687396965521267154688957035035'  # noqa: E501


def test_e_precomputed(e_1000_digits):
  PRECISION = 3000
  e_value = e.get_e_pre_computed()
  assert len(str(e_value)) == PRECISION + 1
  assert str(e_value)[:1001] == e_1000_digits


class TestE:
  def test_e_1(self, e_1000_digits):
    assert e.e(1) == e_1000_digits[:1]

  def test_e_2(self, e_1000_digits):
    assert e.e(2) == e_1000_digits[:3]

  def test_e_5(self, e_1000_digits):
    assert e.e(5) == e_1000_digits[:6]

  def test_e_100(self, e_1000_digits):
    assert e.e(100) == e_1000_digits[:101]

  def test_e_1000(self, e_1000_digits):
    assert e.e(1000) == e_1000_digits[:1001]


class TestMain:
  def test_main(self, mocker, capfd, e_1000_digits):
    mocker.patch('builtins.input', side_effect=['10', 'q'])
    e.main()
    out, err = capfd.readouterr()
    assert out == f'{e_1000_digits[: 11]}\n'
    assert err == ''

  @pytest.mark.parametrize('inp', ['-10', '0', '1001'])
  def test_main_invalid_input(self, mocker, capfd, inp):
    mocker.patch('builtins.input', side_effect=[inp, 'q'])
    e.main()
    out, err = capfd.readouterr()
    assert out == 'digits must be a positive integer upto 1000\n'
    assert err == ''