"""
Sample for nested test.
"""
from fexception import FTypeError

__author__ = 'IncognitoCoding'
__copyright__ = 'Copyright 2022, nested_override'
__credits__ = ['IncognitoCoding']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'IncognitoCoding'
__status__ = 'Beta'


def nested_override():

    x = 'Z'

    if not isinstance(x, int):
        exc_args = {
            'main_message': 'Sample problem with the nested module.',
            'expected_result': f'A {type(x)} was sent.',
            'returned_result': 'An <class \'int\'>',
            'suggested_resolution': 'Check input variable.'
        }
        raise FTypeError(exc_args, tb_limit=None, tb_remove_name='nested_override')


def nested_no_override():

    x = 'Z'

    if not isinstance(x, int):
        exc_args = {
            'main_message': 'Sample problem with the nested module.',
            'expected_result': f'A {type(x)} was sent.',
            'returned_result': 'An <class \'int\'>',
            'suggested_resolution': 'Check input variable.'
        }
        raise FTypeError(exc_args)


def nested_no_format():

    x = 'Z'

    if not isinstance(x, int):
        raise TypeError('Sample no format with the nested module')
