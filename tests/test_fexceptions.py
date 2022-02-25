import pytest

# Local Exceptions
from fexception.fexception import *

# Local tests
from nested import (nested_override,
                    nested_no_override,
                    nested_no_format)


__author__ = 'IncognitoCoding'
__copyright__ = 'Copyright 2022, test_fexceptions'
__credits__ = ['IncognitoCoding']
__license__ = 'MIT'
__version__ = '0.0.2'
__maintainer__ = 'IncognitoCoding'
__status__ = 'Beta'


class MySampleException(Exception):
    __module__ = 'builtins'

    exception_message: str

    def __init__(self, exception_message: str) -> None:
        self.exception_message = exception_message


# ############################################################
# ######Section Test Part 1 (Successful Value Checking)#######
# ############################################################
#
# FGeneralError tests any specific backend calls.
# pytest-cov does not check some of the calls/checks because it does
# not look at some underlying info like traceback. These have been excluded.
#
#
def test_1_FKBaseException():
    """
    Tests formatting a FKBaseException exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FKBaseException(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FKBaseException' in str(excinfo.value)


def test_1_1_FKBaseException():
    """
    Tests formatting a FKBaseException exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FKBaseException(message_args=exc_args,
                              tb_limit=None,
                              tb_remove_name='test_1_1_FKBaseException')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FException():
    """
    Tests formatting a FException exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FException(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FException' in str(excinfo.value)


def test_1_1_FException():
    """
    Tests formatting a FException exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FException(message_args=exc_args,
                         tb_limit=None,
                         tb_remove_name='test_1_1_FException')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FArithmeticError():
    """
    Tests formatting a FArithmeticError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FArithmeticError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FArithmeticError' in str(excinfo.value)


def test_1_1_FArithmeticError():
    """
    Tests formatting a FArithmeticError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FArithmeticError(message_args=exc_args,
                               tb_limit=None,
                               tb_remove_name='test_1_1_FArithmeticError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FBufferError():
    """
    Tests formatting a FBufferError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FBufferError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FBufferError' in str(excinfo.value)


def test_1_1_FBufferError():
    """
    Tests formatting a FBufferError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FBufferError(message_args=exc_args,
                           tb_limit=None,
                           tb_remove_name='test_1_1_FBufferError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FLookupError():
    """
    Testing the a FLookupError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FLookupError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FLookupError' in str(excinfo.value)


def test_1_1_FLookupError():
    """
    Testing the a FLookupError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FLookupError(message_args=exc_args,
                           tb_limit=None,
                           tb_remove_name='test_1_1_FLookupError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FAssertionError():
    """
    Testing the a FAssertionError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FAssertionError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FAssertionError' in str(excinfo.value)


def test_1_1_FAssertionError():
    """
    Testing the a FAssertionError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FAssertionError(message_args=exc_args,
                              tb_limit=None,
                              tb_remove_name='test_1_1_FAssertionError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FAttributeError():
    """
    Tests formatting a FAttributeError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FAttributeError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FAttributeError' in str(excinfo.value)


def test_1_1_FAttributeError():
    """
    Tests formatting a FAttributeError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FAttributeError(message_args=exc_args,
                              tb_limit=None,
                              tb_remove_name='test_1_1_FAttributeError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FEOFError():
    """
    Tests formatting a FEOFError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FEOFError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FEOFError' in str(excinfo.value)


def test_1_1_FEOFError():
    """
    Tests formatting a FEOFError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FEOFError(message_args=exc_args,
                        tb_limit=None,
                        tb_remove_name='test_1_1_FEOFError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FFloatingPointError():
    """
    Tests formatting a FFloatingPointError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FFloatingPointError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FFloatingPointError' in str(excinfo.value)


def test_1_1_FFloatingPointError():
    """
    Tests formatting a FFloatingPointError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FFloatingPointError(message_args=exc_args,
                                  tb_limit=None,
                                  tb_remove_name='test_1_1_FFloatingPointError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FGeneratorExit():
    """
    Tests formatting a FGeneratorExit exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FGeneratorExit(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FGeneratorExit' in str(excinfo.value)


def test_1_1_FGeneratorExit():
    """
    Tests formatting a FGeneratorExit exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FGeneratorExit(message_args=exc_args,
                             tb_limit=None,
                             tb_remove_name='test_1_1_FGeneratorExit')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FImportError():
    """
    Tests formatting a FImportError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FImportError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FImportError' in str(excinfo.value)


def test_1_1_FImportError():
    """
    Tests formatting a FImportError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FImportError(message_args=exc_args,
                           tb_limit=None,
                           tb_remove_name='test_1_1_FImportError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FModuleNotFoundError():
    """
    Tests formatting a FModuleNotFoundError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FModuleNotFoundError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FModuleNotFoundError' in str(excinfo.value)


def test_1_1_FModuleNotFoundError():
    """
    Tests formatting a FModuleNotFoundError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FModuleNotFoundError(message_args=exc_args,
                                   tb_limit=None,
                                   tb_remove_name='test_1_1_FModuleNotFoundError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FIndexError():
    """
    Tests formatting a FIndexError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FIndexError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FIndexError' in str(excinfo.value)


def test_1_1_FIndexError():
    """
    Tests formatting a FIndexError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FIndexError(message_args=exc_args,
                          tb_limit=None,
                          tb_remove_name='test_1_1_FIndexError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FKeyError():
    """
    Tests formatting a FKeyError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FKeyError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FKeyError' in str(excinfo.value)


def test_1_1_FKeyError():
    """
    Tests formatting a FKeyError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FKeyError(message_args=exc_args,
                        tb_limit=None,
                        tb_remove_name='test_1_1_FKeyError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FKeyboardInterrupt():
    """
    Tests formatting a FKeyboardInterrupt exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FKeyboardInterrupt(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FKeyboardInterrupt' in str(excinfo.value)


def test_1_1_FKeyboardInterrupt():
    """
    Tests formatting a FKeyboardInterrupt exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FKeyboardInterrupt(message_args=exc_args,
                                 tb_limit=None,
                                 tb_remove_name='test_1_1_FKeyboardInterrupt')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FMemoryError():
    """
    Tests formatting a FMemoryError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FMemoryError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FMemoryError' in str(excinfo.value)


def test_1_1_FMemoryError():
    """
    Tests formatting a FMemoryError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FMemoryError(message_args=exc_args,
                           tb_limit=None,
                           tb_remove_name='test_1_1_FMemoryError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FNameError():
    """
    Tests formatting a FNameError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FNameError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FNameError' in str(excinfo.value)


def test_1_1_FNameError():
    """
    Tests formatting a FNameError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FNameError(message_args=exc_args,
                         tb_limit=None,
                         tb_remove_name='test_1_1_FNameError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FNotImplementedError():
    """
    Tests formatting a FNotImplementedError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FNotImplementedError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FNotImplementedError' in str(excinfo.value)


def test_1_1_FNotImplementedError():
    """
    Tests formatting a FNotImplementedError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FNotImplementedError(message_args=exc_args,
                                   tb_limit=None,
                                   tb_remove_name='test_1_1_FNotImplementedError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FOSError():
    """
    Tests formatting a FOSError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FOSError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FOSError' in str(excinfo.value)


def test_1_1_FOSError():
    """
    Tests formatting a FOSError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FOSError(message_args=exc_args,
                       tb_limit=None,
                       tb_remove_name='test_1_1_FOSError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FOverflowError():
    """
    Tests formatting a FOverflowError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FOverflowError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FOverflowError' in str(excinfo.value)


def test_1_1_FOverflowError():
    """
    Tests formatting a FOverflowError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FOverflowError(message_args=exc_args,
                             tb_limit=None,
                             tb_remove_name='test_1_1_FOverflowError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FRecursionError():
    """
    Tests formatting a FRecursionError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FRecursionError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FRecursionError' in str(excinfo.value)


def test_1_1_FRecursionError():
    """
    Tests formatting a FRecursionError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FRecursionError(message_args=exc_args,
                              tb_limit=None,
                              tb_remove_name='test_1_1_FRecursionError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FReferenceError():
    """
    Tests formatting a FReferenceError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FReferenceError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FReferenceError' in str(excinfo.value)


def test_1_1_FReferenceError():
    """
    Tests formatting a FReferenceError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FReferenceError(message_args=exc_args,
                              tb_limit=None,
                              tb_remove_name='test_1_1_FReferenceError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FRuntimeError():
    """
    Tests formatting a FRuntimeError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FRuntimeError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FRuntimeError' in str(excinfo.value)


def test_1_1_FRuntimeError():
    """
    Tests formatting a FRuntimeError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FRuntimeError(message_args=exc_args,
                            tb_limit=None,
                            tb_remove_name='test_1_1_FRuntimeError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FStopIteration():
    """
    Tests formatting a FStopIteration exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FStopIteration(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FStopIteration' in str(excinfo.value)


def test_1_1_FStopIteration():
    """
    Tests formatting a FStopIteration exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FStopIteration(message_args=exc_args,
                             tb_limit=None,
                             tb_remove_name='test_1_1_FStopIteration')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FStopAsyncIteration():
    """
    Tests formatting a FStopAsyncIteration exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FStopAsyncIteration(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FStopAsyncIteration' in str(excinfo.value)


def test_1_1_FStopAsyncIteration():
    """
    Tests formatting a FStopAsyncIteration exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FStopAsyncIteration(message_args=exc_args,
                                  tb_limit=None,
                                  tb_remove_name='test_1_1_FStopAsyncIteration')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FSyntaxError():
    """
    Tests formatting a FSyntaxError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FSyntaxError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FSyntaxError' in str(excinfo.value)


def test_1_1_FSyntaxError():
    """
    Tests formatting a FSyntaxError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FSyntaxError(message_args=exc_args,
                           tb_limit=None,
                           tb_remove_name='test_1_1_FSyntaxError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FIndentationError():
    """
    Tests formatting a FIndentationError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FIndentationError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FIndentationError' in str(excinfo.value)


def test_1_1_FIndentationError():
    """
    Tests formatting a FIndentationError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FIndentationError(message_args=exc_args,
                                tb_limit=None,
                                tb_remove_name='test_1_1_FIndentationError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FTabError():
    """
    Tests formatting a FTabError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FTabError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FTabError' in str(excinfo.value)


def test_1_1_FTabError():
    """
    Tests formatting a FTabError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FTabError(message_args=exc_args,
                        tb_limit=None,
                        tb_remove_name='test_1_1_FTabError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FSystemError():
    """
    Tests formatting a FSystemError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FSystemError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FSystemError' in str(excinfo.value)


def test_1_1_FSystemError():
    """
    Tests formatting a FSystemError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FSystemError(message_args=exc_args,
                           tb_limit=None,
                           tb_remove_name='test_1_1_FSystemError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FSystemExit():
    """
    Tests formatting a FSystemExit exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FSystemExit(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FSystemExit' in str(excinfo.value)


def test_1_1_FSystemExit():
    """
    Tests formatting a FSystemExit exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FSystemExit(message_args=exc_args,
                          tb_limit=None,
                          tb_remove_name='test_1_1_FSystemExit')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FTypeError():
    """
    Tests formatting a FTypeError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FTypeError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FTypeError' in str(excinfo.value)


def test_1_1_FTypeError():
    """
    Tests formatting a FTypeError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FTypeError(message_args=exc_args,
                         tb_limit=None,
                         tb_remove_name='test_1_1_FTypeError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FUnboundLocalError():
    """
    Tests formatting a FUnboundLocalError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnboundLocalError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FUnboundLocalError' in str(excinfo.value)


def test_1_1_FUnboundLocalError():
    """
    Tests formatting a FUnboundLocalError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnboundLocalError(message_args=exc_args,
                                 tb_limit=None,
                                 tb_remove_name='test_1_1_FUnboundLocalError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FUnicodeError():
    """
    Tests formatting a FUnicodeError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnicodeError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FUnicodeError' in str(excinfo.value)


def test_1_1_FUnicodeError():
    """
    Tests formatting a FUnicodeError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnicodeError(message_args=exc_args,
                            tb_limit=None,
                            tb_remove_name='test_1_1_FUnicodeError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FUnicodeEncodeError():
    """
    Tests formatting a FUnicodeEncodeError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnicodeEncodeError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FUnicodeEncodeError' in str(excinfo.value)


def test_1_1_FUnicodeEncodeError():
    """
    Tests formatting a FUnicodeEncodeError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnicodeEncodeError(message_args=exc_args,
                                  tb_limit=None,
                                  tb_remove_name='test_1_1_FUnicodeEncodeError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FUnicodeDecodeError():
    """
    Tests formatting a FUnicodeDecodeError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnicodeDecodeError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FUnicodeDecodeError' in str(excinfo.value)


def test_1_1_FUnicodeDecodeError():
    """
    Tests formatting a FUnicodeDecodeError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnicodeDecodeError(message_args=exc_args,
                                  tb_limit=None,
                                  tb_remove_name='test_1_1_FUnicodeDecodeError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FUnicodeTranslateError():
    """
    Tests formatting a FUnicodeTranslateError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnicodeTranslateError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FUnicodeTranslateError' in str(excinfo.value)


def test_1_1_FUnicodeTranslateError():
    """
    Tests formatting a FUnicodeTranslateError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnicodeTranslateError(message_args=exc_args,
                                     tb_limit=None,
                                     tb_remove_name='test_1_1_FUnicodeTranslateError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FValueError():
    """
    Tests formatting a FValueError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FValueError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FValueError' in str(excinfo.value)


def test_1_1_FValueError():
    """
    Tests formatting a FValueError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FValueError(message_args=exc_args,
                          tb_limit=None,
                          tb_remove_name='test_1_1_FValueError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FZeroDivisionError():
    """
    Tests formatting a FZeroDivisionError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FZeroDivisionError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FZeroDivisionError' in str(excinfo.value)


def test_1_1_FZeroDivisionError():
    """
    Tests formatting a FZeroDivisionError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FZeroDivisionError(message_args=exc_args,
                                 tb_limit=None,
                                 tb_remove_name='test_1_1_FZeroDivisionError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FEnvironmentError():
    """
    Tests formatting a FEnvironmentError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FEnvironmentError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FEnvironmentError' in str(excinfo.value)


def test_1_1_FEnvironmentError():
    """
    Tests formatting a FEnvironmentError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FEnvironmentError(message_args=exc_args,
                                tb_limit=None,
                                tb_remove_name='test_1_1_FEnvironmentError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FIOError():
    """
    Tests formatting a FIOError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FIOError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FIOError' in str(excinfo.value)


def test_1_1_FIOError():
    """
    Tests formatting a FIOError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FIOError(message_args=exc_args,
                       tb_limit=None,
                       tb_remove_name='test_1_1_FIOError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FWindowsError():
    """
    Tests formatting a FWindowsError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FWindowsError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FWindowsError' in str(excinfo.value)


def test_1_1_FWindowsError():
    """
    Tests formatting a FWindowsError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FWindowsError(message_args=exc_args,
                            tb_limit=None,
                            tb_remove_name='test_1_1_FWindowsError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FBlockingIOError():
    """
    Tests formatting a FBlockingIOError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FBlockingIOError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FBlockingIOError' in str(excinfo.value)


def test_1_1_FBlockingIOError():
    """
    Tests formatting a FBlockingIOError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FBlockingIOError(message_args=exc_args,
                               tb_limit=None,
                               tb_remove_name='test_1_1_FBlockingIOError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FChildProcessError():
    """
    Tests formatting a FChildProcessError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FChildProcessError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FChildProcessError' in str(excinfo.value)


def test_1_1_FChildProcessError():
    """
    Tests formatting a FChildProcessError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FChildProcessError(message_args=exc_args,
                                 tb_limit=None,
                                 tb_remove_name='test_1_1_FChildProcessError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FConnectionError():
    """
    Tests formatting a FConnectionError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FConnectionError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FConnectionError' in str(excinfo.value)


def test_1_1_FConnectionError():
    """
    Tests formatting a FConnectionError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FConnectionError(message_args=exc_args,
                               tb_limit=None,
                               tb_remove_name='test_1_1_FConnectionError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FBrokenPipeError():
    """
    Tests formatting a FBrokenPipeError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FBrokenPipeError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FBrokenPipeError' in str(excinfo.value)


def test_1_1_FBrokenPipeError():
    """
    Tests formatting a FBrokenPipeError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FBrokenPipeError(message_args=exc_args,
                               tb_limit=None,
                               tb_remove_name='test_1_1_FBrokenPipeError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FConnectionAbortedError():
    """
    Tests formatting a FConnectionAbortedError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FConnectionAbortedError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FConnectionAbortedError' in str(excinfo.value)


def test_1_1_FConnectionAbortedError():
    """
    Tests formatting a FConnectionAbortedError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FConnectionAbortedError(message_args=exc_args,
                                      tb_limit=None,
                                      tb_remove_name='test_1_1_FConnectionAbortedError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FConnectionRefusedError():
    """
    Tests formatting a FConnectionRefusedError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FConnectionRefusedError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FConnectionRefusedError' in str(excinfo.value)


def test_1_1_FConnectionRefusedError():
    """
    Tests formatting a FConnectionRefusedError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FConnectionRefusedError(message_args=exc_args,
                                      tb_limit=None,
                                      tb_remove_name='test_1_1_FConnectionRefusedError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FConnectionResetError():
    """
    Tests formatting a FConnectionResetError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FConnectionResetError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FConnectionResetError' in str(excinfo.value)


def test_1_1_FConnectionResetError():
    """
    Tests formatting a FConnectionResetError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FConnectionResetError(message_args=exc_args,
                                    tb_limit=None,
                                    tb_remove_name='test_1_1_FConnectionResetError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FFileExistsError():
    """
    Tests formatting a FFileExistsError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FFileExistsError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FFileExistsError' in str(excinfo.value)


def test_1_1_FFileExistsError():
    """
    Tests formatting a FFileExistsError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FFileExistsError(message_args=exc_args,
                               tb_limit=None,
                               tb_remove_name='test_1_1_FFileExistsError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FFileNotFoundError():
    """
    Tests formatting a FFileNotFoundError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FFileNotFoundError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FFileNotFoundError' in str(excinfo.value)


def test_1_1_FFileNotFoundError():
    """
    Tests formatting a FFileNotFoundError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FFileNotFoundError(message_args=exc_args,
                                 tb_limit=None,
                                 tb_remove_name='test_1_1_FFileNotFoundError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FInterruptedError():
    """
    Tests formatting a FInterruptedError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FInterruptedError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FInterruptedError' in str(excinfo.value)


def test_1_1_FInterruptedError():
    """
    Tests formatting a FInterruptedError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FInterruptedError(message_args=exc_args,
                                tb_limit=None,
                                tb_remove_name='test_1_1_FInterruptedError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FIsADirectoryError():
    """
    Tests formatting a FIsADirectoryError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FIsADirectoryError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FIsADirectoryError' in str(excinfo.value)


def test_1_1_FIsADirectoryError():
    """
    Tests formatting a FIsADirectoryError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FIsADirectoryError(message_args=exc_args,
                                 tb_limit=None,
                                 tb_remove_name='test_1_1_FIsADirectoryError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FNotADirectoryError():
    """
    Tests formatting a FNotADirectoryError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FNotADirectoryError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FNotADirectoryError' in str(excinfo.value)


def test_1_1_FNotADirectoryError():
    """
    Tests formatting a FNotADirectoryError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FNotADirectoryError(message_args=exc_args,
                                  tb_limit=None,
                                  tb_remove_name='test_1_1_FNotADirectoryError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FPermissionError():
    """
    Tests formatting a FPermissionError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FPermissionError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FPermissionError' in str(excinfo.value)


def test_1_1_FPermissionError():
    """
    Tests formatting a FPermissionError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FPermissionError(message_args=exc_args,
                               tb_limit=None,
                               tb_remove_name='test_1_1_FPermissionError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FProcessLookupError():
    """
    Tests formatting a FProcessLookupError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FProcessLookupError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FProcessLookupError' in str(excinfo.value)


def test_1_1_FProcessLookupError():
    """
    Tests formatting a FProcessLookupError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FProcessLookupError(message_args=exc_args,
                                  tb_limit=None,
                                  tb_remove_name='test_1_1_FProcessLookupError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FTimeoutError():
    """
    Tests formatting a FTimeoutError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FTimeoutError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FTimeoutError' in str(excinfo.value)


def test_1_1_FTimeoutError():
    """
    Tests formatting a FTimeoutError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FTimeoutError(message_args=exc_args,
                            tb_limit=None,
                            tb_remove_name='test_1_1_FTimeoutError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FWarning():
    """
    Tests formatting a FWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FWarning' in str(excinfo.value)


def test_1_1_FWarning():
    """
    Tests formatting a FWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FWarning(message_args=exc_args,
                       tb_limit=None,
                       tb_remove_name='test_1_1_FWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FUserWarning():
    """
    Tests formatting a FUserWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUserWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FUserWarning' in str(excinfo.value)


def test_1_1_FUserWarning():
    """
    Tests formatting a FUserWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUserWarning(message_args=exc_args,
                           tb_limit=None,
                           tb_remove_name='test_1_1_FUserWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FDeprecationWarning():
    """
    Tests formatting a FDeprecationWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FDeprecationWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FDeprecationWarning' in str(excinfo.value)


def test_1_1_FDeprecationWarning():
    """
    Tests formatting a FDeprecationWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FDeprecationWarning(message_args=exc_args,
                                  tb_limit=None,
                                  tb_remove_name='test_1_1_FDeprecationWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FPendingDeprecationWarning():
    """
    Tests formatting a FPendingDeprecationWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FPendingDeprecationWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FPendingDeprecationWarning' in str(excinfo.value)


def test_1_1_FPendingDeprecationWarning():
    """
    Tests formatting a FPendingDeprecationWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FPendingDeprecationWarning(message_args=exc_args,
                                         tb_limit=None,
                                         tb_remove_name='test_1_1_FPendingDeprecationWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FSyntaxWarning():
    """
    Tests formatting a FSyntaxWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FSyntaxWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FSyntaxWarning' in str(excinfo.value)


def test_1_1_FSyntaxWarning():
    """
    Tests formatting a FSyntaxWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FSyntaxWarning(message_args=exc_args,
                             tb_limit=None,
                             tb_remove_name='test_1_1_FSyntaxWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FRuntimeWarning():
    """
    Tests formatting a FRuntimeWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FRuntimeWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FRuntimeWarning' in str(excinfo.value)


def test_1_1_FRuntimeWarning():
    """
    Tests formatting a FRuntimeWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FRuntimeWarning(message_args=exc_args,
                              tb_limit=None,
                              tb_remove_name='test_1_1_FRuntimeWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FFutureWarning():
    """
    Tests formatting a FFutureWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FFutureWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FFutureWarning' in str(excinfo.value)


def test_1_1_FFutureWarning():
    """
    Tests formatting a FFutureWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FFutureWarning(message_args=exc_args,
                             tb_limit=None,
                             tb_remove_name='test_1_1_FFutureWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FImportWarning():
    """
    Tests formatting a FImportWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FImportWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FImportWarning' in str(excinfo.value)


def test_1_1_FImportWarning():
    """
    Tests formatting a FImportWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FImportWarning(message_args=exc_args,
                             tb_limit=None,
                             tb_remove_name='test_1_1_FImportWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FUnicodeWarning():
    """
    Tests formatting a FUnicodeWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnicodeWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FUnicodeWarning' in str(excinfo.value)


def test_1_1_FUnicodeWarning():
    """
    Tests formatting a FUnicodeWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FUnicodeWarning(message_args=exc_args,
                              tb_limit=None,
                              tb_remove_name='test_1_1_FUnicodeWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FEncodingWarning():
    """
    Tests formatting a FEncodingWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FEncodingWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FEncodingWarning' in str(excinfo.value)


def test_1_1_FEncodingWarning():
    """
    Tests formatting a FEncodingWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FEncodingWarning(message_args=exc_args,
                               tb_limit=None,
                               tb_remove_name='test_1_1_FEncodingWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FBytesWarning():
    """
    Tests formatting a FBytesWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FBytesWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FBytesWarning' in str(excinfo.value)


def test_1_1_FBytesWarning():
    """
    Tests formatting a FBytesWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FBytesWarning(message_args=exc_args,
                            tb_limit=None,
                            tb_remove_name='test_1_1_FBytesWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FResourceWarning():
    """
    Tests formatting a FResourceWarning exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FResourceWarning(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FResourceWarning' in str(excinfo.value)


def test_1_1_FResourceWarning():
    """
    Tests formatting a FResourceWarning exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FResourceWarning(message_args=exc_args,
                               tb_limit=None,
                               tb_remove_name='test_1_1_FResourceWarning')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_FCustomException():
    """
    Tests formatting a FCustomException exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'custom_type': MySampleException,
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FCustomException(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: MySampleException' in str(excinfo.value)


def test_1_1_FCustomException():
    """
    Tests formatting a FCustomException exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'custom_type': MySampleException,
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FCustomException(message_args=exc_args,
                               tb_limit=None,
                               tb_remove_name='test_1_1_FCustomException')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)
    assert 'Exception: MySampleException' in str(excinfo.value)


def test_1_2_FCustomException():
    """
    Tests formatting a custom type exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'custom_type': MySampleException,
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise MySampleException(FCustomException(message_args=exc_args))
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: MySampleException' in str(excinfo.value)


def test_1_FGeneralError():
    """
    Tests formatting a FGeneralError exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FGeneralError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FGeneralError' in str(excinfo.value)
    assert 'Module: test_fexceptions' in str(excinfo.value)
    assert 'Name: test_1_FGeneralError' in str(excinfo.value)


def test_1_1_FGeneralError():
    """
    Tests formatting a FGeneralError exception with adjusted traceback.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FGeneralError(message_args=exc_args,
                            tb_limit=None,
                            tb_remove_name='test_1_1_FGeneralError')
    assert 'Module: python' in str(excinfo.value)
    assert 'Name: pytest_pyfunc_call' in str(excinfo.value)
    assert 'Line: 183' in str(excinfo.value)


def test_1_2_FGeneralError():
    """
    Tests formatting a FGeneralError exception with lists.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': ['A door'],
            'returned_result': ['A window'],
            'suggested_resolution': ['Call contractor'],
        }
        raise FGeneralError(message_args=exc_args)
    assert 'Problem with the construction project.' in str(excinfo.value)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FGeneralError' in str(excinfo.value)
    assert 'Module: test_fexceptions' in str(excinfo.value)
    assert 'Name: test_1_2_FGeneralError' in str(excinfo.value)


def test_1_3_FGeneralError():
    """
    Tests formatting a FGeneralError exception with no main message.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FGeneralError(message_args=exc_args)
    assert 'A door' in str(excinfo.value)
    assert 'A window' in str(excinfo.value)
    assert 'Call contractor' in str(excinfo.value)
    assert 'Exception: FGeneralError' in str(excinfo.value)
    assert 'Module: test_fexceptions' in str(excinfo.value)
    assert 'Name: test_1_3_FGeneralError' in str(excinfo.value)


def test_1_nested_override():
    """
    Tests using the override by calling the nested.py sample.

    The adjusted traceback print can not be tested on the nested traceback because pytest
    prints the original traceback details. This tests to make sure the formatted message
    has the correct override output.
    """

    try:
        nested_override()
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
            raise FTypeError(message_args=exc_args)
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


def test_1_1_nested_no_override():
    """
    Tests formatting an exception with no override.
    """
    with pytest.raises(Exception) as excinfo:
        nested_no_override()
    assert 'Exception: FTypeError' in str(excinfo.value)
    assert 'Module: nested' in str(excinfo.value)
    assert 'Name: nested_no_override' in str(excinfo.value)


def test_1_1_nested_no_format():
    """
    Tests formatting a nested exception that is not formatted.

    Tests for the nested format wording.
    """
    try:
        nested_no_format()
    except Exception as exc:
        assert 'Sample no format with the nested module' in str(exc)

        # Checks that Trace Details returns.
        try:
            exc_args = {
                'main_message': 'Problem with the construction project.',
                'original_exception': exc
            }
            raise FTypeError(message_args=exc_args)
        except Exception as exc1:
            assert 'Problem with the construction project.' in str(exc1)
            assert 'Nested Exception:' in str(exc1)
            assert 'Sample no format with the nested module' in str(exc1)


# ############################################################
# ######Section Test Part 2 (Error/Catch Value Checking)######
# ############################################################
# All exceptions use similar back end creation calls. Only 1 Exception class will be used
# to trigger the exception testing.


def test_2_FGeneralError():
    """
    Tests an invalid message input key.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'bad_key': 'Problem with the construction project.',
        }
        raise FGeneralError(message_args=exc_args)
    assert 'does not match any expected match option key' in str(excinfo.value)


def test_2_1_FGeneralError():
    """
    Tests no keys.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
        }
        raise FGeneralError(message_args=exc_args)
    assert 'No key(s) were sent.' in str(excinfo.value)


def test_2_2_FGeneralError():
    """
    Tests sending a single line string.
    """
    with pytest.raises(Exception) as excinfo:
        raise FGeneralError(message_args='Single Line Exception')
    assert ('Dictionary format is the required input to format an exception message. '
            'Single line messages should use the built-in Python exceptions') in str(excinfo.value)


def test_2_3_FGeneralError():
    """
    Tests sending an invalid tb_limit type.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FGeneralError(message_args=exc_args, tb_limit={'invalid Type'})
    assert 'int format is the required input to set the traceback limit option.' in str(excinfo.value)


def test_2_4_FGeneralError():
    """
    Tests sending an invalid tb_remove_name type.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'Problem with the construction project.',
            'expected_result': 'A door',
            'returned_result': 'A window',
            'suggested_resolution': 'Call contractor',
        }
        raise FGeneralError(message_args=exc_args, tb_limit=None, tb_remove_name={'invalid Type'})
    assert """Invalid tb_remove_name type.""" in str(excinfo.value)
    assert """<class 'str'>""" in str(excinfo.value)
    assert """<class 'set'>""" in str(excinfo.value)


def test_2_FCustomException():
    """
    Tests an incorrect custom type exception.
    """
    with pytest.raises(Exception) as excinfo:
        exc_args = {
            'main_message': 'This is my test error message.',
            'custom_type': 'BAD VALUE ERROR',
        }
        raise MySampleException(FCustomException(message_args=exc_args))
    assert 'A pre-configured exception' in str(excinfo.value)
