import pytest

from fexception import FCustomException, FValueError


class MySampleException(Exception):
    __module__ = 'builtins'

    exception_message: str

    def __init__(self, exception_message: str) -> None:
        self.exception_message = exception_message


# ############################################################
# ######Section Test Part 1 (Successful Value Checking)#######
# ############################################################


def test_success_1_FValueError():
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
    assert 'Name: test_success_1_FValueError' in str(excinfo.value)


def test_success_1_FCustomException():
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


def test_failure_1_FCustomException():
    with pytest.raises(Exception) as excinfo:
        exec_args = {
            'main_message': 'This is my test error message.',
            'custom_type': 'BAD VALUE ERROR',
        }
        raise FCustomException(exec_args)
    assert 'A pre-configured exception' in str(excinfo.value)


def test_failure_1_FValueError():
    with pytest.raises(Exception) as excinfo:
        exec_args = {
            'bad_key': 'Problem with the construction project.',
        }
        raise FValueError(exec_args)
    assert 'does not match any expected match option key' in str(excinfo.value)
