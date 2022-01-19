fexception
==========

fexception is designed to provide cleaner useable exceptions. The "f" in fexception represents formatted.

Description
===========

fexception includes every built-in Python exception and adds the ability to wrap a clean formatted structure around the exception. 
Each formatted ("f") exception can add up to five different types of exception input into the formatted exception. fexception has
multiple traceback return options.

fexception's operates like built-in Python exceptions. You raise the exception when needed, and the exception will get formatted. 
All raised exceptions will source and trackback from the original raised location. fexception supports nested formatted messages.

fexception offers three traceback options that can enable/disable with boolean attributes. 
  1. One level of traceback.
  2. Full traceback.
  3. No traceback information.

fexception offers five message keys to format any exception to your liking. Three keys provide string or list values to format multiple lines cleanly.
Each exception message must be in dictionary format. Use the table below to set the formatted exception message. 

| Key           			        | Type          | Optional | Value  									                                                            |
| --------------------------- |:-------------:|:--------:|------------------------------------------------------------------------------------- |
| main_message                | str           | no		   | The main exception message.				                                                  |
| expected_result             | str or list   | yes		   | The expected result message. (str: single line) or (list: individual split lines)    |
| returned_result			        | str or list   | yes      | The returned result message.	(str: single line) or (list: individual split lines)    |
| suggested_resolution		    | str or list   | yes      | A suggested resolution message. (str: single line) or (list: individual split lines) |
| original_exception		      | Exception     | yes      | A caught exception for additional details.                                           |

Installation
============

From PyPI
-------------------
You can find fexception on PyPI. https://pypi.org/project/fexception/ 
Install fexception to your Python environment. 

Usage
=====
Once installed, add fexception as a module and select the formatted
exception option from the import.

Note: You can use * to import all formatted exception options.
