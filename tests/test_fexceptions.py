import pytest

from fexception import FCustomException, FValueError, FTypeError
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

    Tests if the "Trace Details" being added into the exception message.

    The adjusted traceback print can not be tested on the nested traceback because pytest
    prints the original traceback details. This tests to make sure the formatted message
    has the correct override output.
    """
    try:
        type_validate_override()
    except Exception as exc:
        assert 'Exception: FTypeError' in str(exc)
        assert 'Module: test_fexceptions' in str(exc)
        assert 'Name: test_1_nested_override' in str(exc)

        # Checks that Trace Details returns.
        try:
            exc_args = {
                'main_message': 'Problem with the construction project.',
                'original_exception': exc
            }
            raise FTypeError(exc_args)
        except Exception as exc1:
            assert 'Problem with the construction project.' in str(exc1)
            assert '- Name:' in str(exc1).split('\n')[-5]
            assert '- Line:' in str(exc1).split('\n')[-4]

        # Checks that Trace Details returns.
        try:
            exc_args = {
                'main_message': 'Problem with the construction project.',
                'original_exception': exc
            }
            raise FTypeError(exc_args, tb_limit=2)
        except Exception as exc1:
            assert 'Problem with the construction project.' in str(exc1)
            assert '- Name:' in str(exc1).split('\n')[-5]
            assert '- Line:' in str(exc1).split('\n')[-4]

        # Checks that Trace Details does not return.
        try:
            exc_args = {
                'main_message': 'Problem with the construction project.',
                'original_exception': exc
            }
            raise FTypeError(exc_args, tb_limit=0)
        except Exception as exc2:
            assert 'Problem with the construction project.' in str(exc2)
            assert '- Name:' not in str(exc2).split('\n')[-5]
            assert '- Line:' not in str(exc2).split('\n')[-4]


def test_1_nested_no_override():
    """
    Tests formatting an error with no override.
    """
    try:
        type_validate_no_override()
    except Exception as exc:
        assert 'Exception: FTypeError' in str(exc)
        assert 'Module: nested' in str(exc)
        assert 'Name: type_validate_no_override' in str(exc)
        assert 'Module: nested' in str(exc)


def test_1_FValueError():
    """
    Tests formatting a standard exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FValueError(exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Exception: FValueError' in str(excinfo.value)
    assert 'Module: test_fexceptions' in str(excinfo.value)
    assert 'Name: test_1_FValueError' in str(excinfo.value)


def test_1_FCustomException():
    """
    Tests formatting a custom type exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Testing the FCustomException exception.',
            'custom_type': MySampleException,
        }
        raise MySampleException(FCustomException(exc_args))
    assert 'Testing the FCustomException exception.' in str(excinfo.value)
    assert 'Exception: MySampleException' in str(excinfo.value)

# ############################################################
# ######Section Test Part 2 (Error/Catch Value Checking)######
# ############################################################


def test_2_FCustomException():
    """
    Tests an incorrect custom type exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'This is my test error message.',
            'custom_type': 'BAD VALUE ERROR',
        }
        raise MySampleException(FCustomException(exc_args))
    assert 'A pre-configured exception' in str(excinfo.value)


def test_2_FValueError():
    """
    Tests a bad input key in teh caller_override dictionary.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'bad_key': 'Problem with the construction project.',
        }
        raise FValueError(exc_args)
    assert 'does not match any expected match option key' in str(excinfo.value)


def test_2_1_FValueError():
    """
    Tests no keys.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
        }
        raise FValueError(exc_args)
    assert 'No key(s) were sent.' in str(excinfo.value)


def test_2_2_FValueError():
    """
    Tests removing the key tb_remove to trigger the failure.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Sample nested failure.',
            'expected_result': 'Sample 1',
            'returned_result': 'Sample 2',
            'suggested_resolution': 'Check submitted sample.'
        }
        caller_override = {
            'module': 'my_sample',
            'name': 'sample',
            'line': 1000,
        }
        raise FValueError(exc_args, tb_limit=None, caller_override=caller_override)
    assert 'The input keys have inconsistent value and requirement keys' in str(excinfo.value)


def test_2_3_FValueError():
    """
    Tests a bad input key in teh caller_override dictionary.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
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
        raise FValueError(exc_args, tb_limit=None, caller_override=caller_override)
    assert """The dictionary key ('bad_key') does not exist in the expected required key(s)""" in str(excinfo.value)
