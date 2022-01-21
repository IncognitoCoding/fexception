from typing import Union
from dataclasses import dataclass


class ErrorFormatFailure(Exception):
    """
    Exception raised for an issue formatting the exception message.

    Args:
        exception_message: The invalid key reason.
    """
    __module__ = 'builtins'

    exception_message: str

    def __init__(self, exception_message: str) -> None:
        self.exception_message = exception_message


class InputFailure(Exception):
    """
    Exception raised for an input exception message.

    Args:
        exception_message: The incorrect input reason.
    """
    __module__ = 'builtins'

    exception_message: str

    def __init__(self, exception_message: str) -> None:
        self.exception_message = exception_message


@dataclass
class ProcessedMessageArgs:
    """
    Processed exception info to format the exception message.

    Args:
        main_message (str): The main exception message.\\
        expected_result (Union[str, list], Optional): The expected result.\\
        \tstr vs list:
        \t\tA string will be a single formatted line.\\
        \t\tA list will be split into individual formatted lines.\\
        returned_result (Union[str, list], Optional): The returned result.\\
        \tstr vs list:
        \t\tA string will be a single formatted line.\\
        \t\tA list will be split into individual formatted lines.\\
        suggested_resolution (Union[str, list], Optional): A suggested resolution.\\
        \tstr vs list:
        \t\tA string will be a single formatted line.\\
        \t\tA list will be split into individual formatted lines.\\
        original_exception (any, Optional): The original exception.\\
    """
    __slots__ = ("main_message", "expected_result", "returned_result",
                 "suggested_resolution", "original_exception")

    main_message: str
    expected_result: Union[str, list]
    returned_result: Union[str, list]
    suggested_resolution: Union[str, list]
    original_exception: Exception


@dataclass
class ProcessedOverrideArgs:
    """
    Processed override info to format the exception message.

    Args:
        module (str): The caller module.\\
        name (str): The caller function or method name.\\
        line (int): The caller raised exception line number\\
    """
    __slots__ = "module", "name", "line"

    module: str
    name: str
    line: int


@dataclass
class ExceptionArgs:
    """
    Exception args to construct the formatted exception message.

    Args:
        exception_type (Exception): The exception type.
        caller_module (str): Exception caller module.
        caller_name (str): Exception function or class name.
        caller_line (int): Exception caller line.
        tb_limit (int): Traceback limit index at the most recent call. Defaults to None.
        caller_override (dict): Changed traceback details. Defaults to None.
    """
    __slots__ = "exception_type", "caller_module", "caller_line", "caller_name", "tb_limit", "caller_override"

    exception_type: Exception
    caller_module: str
    caller_line: int
    caller_name: str
    tb_limit: int
    caller_override: dict


@dataclass
class HookArgs:
    """
    Exception hook args used to return the formatted raised exception message.

    Args:
        formatted_exception (str): The formatted exception message.
        exception_args (ExceptionArgs): The exception constructor args.
    """
    __slots__ = "formatted_exception", "exception_args"

    formatted_exception: str
    exception_args: ExceptionArgs
