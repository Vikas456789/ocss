
# README.md
"""
# Example Project

This is a simple example of an open-source Python project.

## Installation

```bash
pip install .
```

## Usage

```python
from example_package.core import hello_world

print(hello_world())
```

## Contributing

Contributions are welcome! Please fork the repository and open a pull request with your changes.
"""

# LICENSE
"""
MIT License

Copyright (c) [year] [Full name]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
...
"""

# setup.py
from setuptools import setup, find_packages

setup(
    name="example_project",
    version="0.1",
    packages=find_packages(),
)

# example_package/__init__.py
# This file intentionally left blank to indicate a Python package.

# example_package/core.py
def hello_world():
    return "Hello, OSS world!"

# tests/__init__.py
# This file intentionally left blank to indicate a Python package.

# tests/test_core.py
from example_package.core import hello_world

def test_hello_world():
    assert hello_world() == "Hello, OSS world!"
