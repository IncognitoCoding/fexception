import pytest

# Local Functions
from fexception.util import set_caller_override

# Local Methods
from fexception.util import KeyCheck


__author__ = 'IncognitoCoding'
__copyright__ = 'Copyright 2022, test_util'
__credits__ = ['IncognitoCoding']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'IncognitoCoding'
__status__ = 'Beta'


# ############################################################
# ######Section Test Part 1 (Successful Value Checking)#######
# ############################################################


def test_1_set_caller_override():
    """
    Tests an setting a caller_override with the module name.
    """
    caller_override = set_caller_override(tb_remove_name='test_1_set_caller_override')
    assert 'python' == str(caller_override.get('module'))
    assert 'pytest_pyfunc_call' == str(caller_override.get('name'))
    # This line number can change if pytest updates code.
    assert 183 == int(caller_override.get('line'))
    assert 'test_1_set_caller_override' == str(caller_override.get('tb_remove'))


def test_1_keycheck() -> None:
    """
    Tests key check success.
    """
    key_check = KeyCheck(values={'key1': 'value1', 'key3': 'value2'},
                         caller_module='sample_module',
                         caller_name='sample_name',
                         caller_line='sample_line')
    key_check.all_keys(required_keys=['key1', 'key3'])


def test_1_2_keycheck() -> None:
    """
    Tests key check success.
    """
    key_check = KeyCheck(values={'key1': 'value1', 'key3': 'value2'},
                         caller_module='sample_module',
                         caller_name='sample_name',
                         caller_line='sample_line')
    key_check.contains_keys(required_keys=['key1'])


def test_3_keycheck() -> None:
    """
    Tests key check success in reverse.
    """
    key_check = KeyCheck(values={'key1': 'value1', 'key3': 'value2'},
                         caller_module='sample_module',
                         caller_name='sample_name',
                         caller_line='sample_line')
    key_check.all_keys(required_keys=['key1', 'key3'])


def test_1_4_keycheck() -> None:
    """
    Tests key check success in reverse.
    """
    key_check = KeyCheck(values={'key1': 'value1', 'key3': 'value2'},
                         caller_module='sample_module',
                         caller_name='sample_name',
                         caller_line='sample_line')
    key_check.contains_keys(required_keys=['key1'], reverse_output=True)


# ############################################################
# ######Section Test Part 2 (Error/Catch Value Checking)######
# ############################################################


def test_2_set_caller_override():
    """
    Tests a non-matching tb_remove name.
    """
    with pytest.raises(Exception) as excinfo:
        set_caller_override(tb_remove_name='invalid_name')
    assert ('The function or method name did not match any co_name '
            'in the inspect.currentframe()') in str(excinfo.value)
    assert """'invalid_name' matching co_name""" in str(excinfo.value)


def test_2_keycheck():
    """
    Tests missing key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={'Green': None, 'Blue': None, 'Red': None},
                             caller_module='sample_module',
                             caller_name='sample_name',
                             caller_line='sample_line')
        key_check.all_keys(required_keys=['Yellow', 'Blue'])
    assert 'The input keys have inconsistent value and requirement keys.' in str(excinfo.value)


def test_2_1_keycheck():
    """
    Tests duplicate key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={'Green': None, 'Blue': None, 'Green': None},
                             caller_module='sample_module',
                             caller_name='sample_name',
                             caller_line='sample_line')
        key_check.contains_keys(required_keys=['Yellow', 'Blue', 'Blue'])
    assert 'The required key list contains duplicate keys. All keys must be unique.' in str(excinfo.value)


def test_2_2_keycheck():
    """
    Tests incorrect type input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={'Green': None, 'Blue': None, 'Green': None},
                             caller_module='sample_module',
                             caller_name='sample_name',
                             caller_line='sample_line')
        key_check.contains_keys(required_keys={'Bad Type'})
    assert """The dictionary key ('{'Bad Type'}') does not match any expected match option key(s).""" in str(excinfo.value)
    assert """Match Option Key(s) = {'Bad Type'}""" in str(excinfo.value)
    assert """Failed Key(s) = ['Green', 'Blue']""" in str(excinfo.value)


def test_2_3_reverse_keycheck():
    """
    Tests duplicate key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={'Green': None, 'Blue': None, 'Red': None},
                             caller_module='sample_module',
                             caller_name='sample_name',
                             caller_line='sample_line')
        key_check.contains_keys(required_keys=['Yellow', 'Blue', 'Blue'], reverse_output=True)
    assert 'The required key list contains duplicate keys. All keys must be unique.' in str(excinfo.value)


def test_2_4_reverse_keycheck():
    """
    Tests duplicate key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={'Green': None, 'Blue': None, 'Red': None},
                             caller_module='sample_module',
                             caller_name='sample_name',
                             caller_line='sample_line')
        key_check.all_keys(required_keys=[], reverse_output=True)
    assert 'No key(s) were sent' in str(excinfo.value)
    assert """Expected Key(s) = ['Green', 'Blue', 'Red']""" in str(excinfo.value)


def test_2_41_reverse_keycheck():
    """
    Tests duplicate key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={'Green': None, 'Blue': None, 'Red': None},
                             caller_module='sample_module',
                             caller_name='sample_name',
                             caller_line='sample_line')
        key_check.all_keys(required_keys='Red', reverse_output=True)
    assert 'The input keys have inconsistent value and requirement keys.' in str(excinfo.value)
    assert """Required Key(s) = ['Green', 'Blue', 'Red']""" in str(excinfo.value)


def test_2_5_keycheck() -> None:
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={'key1': 'value1', 'key3': 'value2'},
                             caller_module='sample_module',
                             caller_name='sample_name',
                             caller_line='sample_line')
        key_check.all_keys(required_keys=['key1', 'key2'])
    assert """The dictionary key ('key2') does not exist in the expected required key(s).""" in str(excinfo.value)
    assert """Expected Key(s) = ['key1', 'key2']""" in str(excinfo.value)
    assert """Failed Key(s) = ['key1', 'key3']""" in str(excinfo.value)


def test_2_6_keycheck() -> None:
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={'key2': 'value1', 'key3': 'value2'},
                             caller_module='sample_module',
                             caller_name='sample_name',
                             caller_line='sample_line')
        key_check.contains_keys(required_keys=['key5'])
    assert """Match Option Key(s) = ['key5']""" in str(excinfo.value)


def test_2_7_keycheck():
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={'key1': 'value1', 'key3': 'value2'},
                             caller_module='sample_module',
                             caller_name='sample_name',
                             caller_line='sample_line')
        key_check.all_keys(required_keys=['key1', 'key2'])
    assert """Expected Key(s) = ['key1', 'key2']""" in str(excinfo.value)


def test_2_8_reverse_keycheck():
    """
    Tests reverse key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={'key1': 'value1', 'key3': 'value2'},
                             caller_module='sample_module',
                             caller_name='sample_name',
                             caller_line='sample_line')
        key_check.all_keys(required_keys=['key1', 'key2'], reverse_output=True)
    assert """Expected Key(s) = ['key1', 'key3']""" in str(excinfo.value)


def test_2_9_reverse_keycheck():
    """
    Tests reverse key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={'Green': None, 'Blue': None, 'Green': None},
                             caller_module='sample_module',
                             caller_name='sample_name',
                             caller_line='sample_line')
        key_check.contains_keys(required_keys=['Yellow', 'Blue'], reverse_output=True)
    assert """Match Option Key(s) = ['Green', 'Blue']""" in str(excinfo.value)
