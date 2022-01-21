import traceback
import pytest

from fexception import FCustomException, FValueError
from nested import type_validate_override, type_validate_no_override


class MySampleException(Exception):
    __module__ = 'builtins'

    exception_message: str

    def __init__(self, exception_message: str) -> None:
        self.exception_message = exception_message


# ############################################################
# ######Section Test Part 1 (Successful Value Checking)#######
# ############################################################


def test_1_nested_override():
    """
    Tests using the override by calling the nested.py sample.

    This is a less common usage, but may be used for anyone creating custom validation
    modules that do not need to report traceback information.

    The adjusted traceback print can not be tested because the nested traceback, but the user
    gets the limited traceback in the console. This tests to make sure the formatted message
    has the correct override output.
    """
    try:
        type_validate_override()
    except Exception as exec:
        tb_output = traceback.format_exception(type(exec), exec, exec.__traceback__)
        assert 'Exception: FValueError' in str(tb_output)
        assert 'Module: test_fexceptions' in str(tb_output)
        assert 'Name: test_1_nested_override' in str(tb_output)


def test_1_nested_no_override():
    """
    Tests formatting an error with no override.
    """
    try:
        type_validate_no_override()
    except Exception as exec:
        tb_output = traceback.format_exception(type(exec), exec, exec.__traceback__)
        assert 'Exception: FValueError' in str(tb_output)
        assert 'Module: nested' in str(tb_output)
        assert 'Name: type_validate_no_override' in str(tb_output)
        assert 'nested.py' in str(tb_output)


def test_1_FValueError():
    with pytest.raises(Exception) as excinfo:
        exec_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FValueError(exec_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Exception: FValueError' in str(excinfo.value)
    assert 'Module: test_fexceptions' in str(excinfo.value)
    assert 'Name: test_1_FValueError' in str(excinfo.value)


def test_1_FCustomException():
    with pytest.raises(Exception) as excinfo:
        exec_args = {
            'main_message': 'Testing the FCustomException exception.',
            'custom_type': MySampleException,
        }
        raise FCustomException(exec_args)
    assert 'Testing the FCustomException exception.' in str(excinfo.value)
    assert 'Exception: MySampleException' in str(excinfo.value)

# ############################################################
# ######Section Test Part 2 (Error/Catch Value Checking)######
# ############################################################


def test_2_FCustomException():
    with pytest.raises(Exception) as excinfo:
        exec_args = {
            'main_message': 'This is my test error message.',
            'custom_type': 'BAD VALUE ERROR',
        }
        raise FCustomException(exec_args)
    assert 'A pre-configured exception' in str(excinfo.value)


def test_2_FValueError():
    with pytest.raises(Exception) as excinfo:
        exec_args = {
            'bad_key': 'Problem with the construction project.',
        }
        raise FValueError(exec_args)
    assert 'does not match any expected match option key' in str(excinfo.value)


def test_2_1_FValueError():
    with pytest.raises(Exception) as excinfo:
        exec_args = {
            'main_message': 'Sample nested failure.',
            'expected_result': 'Sample 1',
            'returned_result': 'Sample 2',
            'suggested_resolution': 'Check submitted sample.'
        }
        caller_override = {
            'module': 'my_sample',
            'name': 'sample',
            'line': 1000,
            # tb_remove is removed to trigger the failure.
        }
        raise FValueError(exec_args, None, caller_override)
    assert 'The input keys have inconsistent value and requirement keys' in str(excinfo.value)


def test_2_2_FValueError():
    with pytest.raises(Exception) as excinfo:
        exec_args = {
            'main_message': 'Sample nested failure.',
            'expected_result': 'Sample 1',
            'returned_result': 'Sample 2',
            'suggested_resolution': 'Check submitted sample.'
        }
        caller_override = {
            'module': 'my_sample',
            'name': 'sample',
            'line': 1000,
            'bad_key': 'my_sample'
        }
        raise FValueError(exec_args, None, caller_override)
    assert """The dictionary key ('bad_key') does not exist in the expected required key(s)""" in str(excinfo.value)
