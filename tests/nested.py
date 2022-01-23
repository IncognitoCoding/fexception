"""
Sample for nested test.
"""
from fexception import FTypeError
import inspect
from pathlib import Path


def type_validate_override():

    x = 'Z'

    if not isinstance(x, int):
        exc_args = {
            'main_message': 'Sample problem with the nested module.',
            'expected_result': f'A {type(x)} was sent.',
            'returned_result': 'An <class \'int\'>',
            'suggested_resolution': 'Check input variable.'
        }
        caller_override = {
            'module': Path(inspect.currentframe().f_back.f_code.co_filename).stem,
            'name': inspect.currentframe().f_back.f_code.co_name,
            'line': inspect.currentframe().f_back.f_lineno,
            'tb_remove': 'nested'
        }
        raise FTypeError(exc_args, tb_limit=None, caller_override=caller_override)


def type_validate_no_override():

    x = 'Z'

    if not isinstance(x, int):
        exc_args = {
            'main_message': 'Sample problem with the nested module.',
            'expected_result': f'A {type(x)} was sent.',
            'returned_result': 'An <class \'int\'>',
            'suggested_resolution': 'Check input variable.'
        }
        raise FTypeError(exc_args)
