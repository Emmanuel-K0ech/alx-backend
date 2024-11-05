# 0x02. i18n

## Resources
Read or watch:
- [Flask-Babel](https://flask-babel.tkte.ch/)
- [Flask i18n tutorial](https://flask.palletsprojects.com/en/2.0.x/patterns/i18n/)
- [pytz](https://pytz.sourceforge.net/)

## Learning Objectives
- Learn how to parametrize Flask templates to display different languages.
- Learn how to infer the correct locale based on URL parameters, user settings, or request headers.
- Learn how to localize timestamps.

## Requirements
- All files will be interpreted/compiled on **Ubuntu 18.04 LTS** using **Python 3** (version 3.7).
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Code should follow the **pycodestyle** style (version 2.5).
- The first line of all Python files should be exactly `#!/usr/bin/env python3`.
- All `.py` files should be executable.
- All modules should have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
  ```
- All classes should have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").MyClass.__doc__)'
  ```
- All functions and methods should have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  ```
  ```bash
  python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
  ```
  - Documentation should be a real sentence explaining the purpose of the module, class, or method (length will be verified).
- All functions and coroutines must be **type-annotated**.
