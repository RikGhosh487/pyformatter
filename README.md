# pyformatter

[![CI](https://github.com/RikGhosh487/pyformatter/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/RikGhosh487/pyformatter/actions)
[![CI](https://github.com/RikGhosh487/pyformatter/actions/workflows/pre-commit-checks.yml/badge.svg)](https://github.com/RikGhosh487/pyformatter/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**pyformatter** is a suite of Python formatting tools that automatically formats your docstrings and comments according to configurable style guidelines. It consists of two powerful formatters:

- **pydocfmt**: Formats Python docstrings with support for Google-style docstrings
- **pycommentfmt**: Formats Python comments to ensure proper line length and readability

---

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Command Line Usage](#command-line-usage)
  - [pydocfmt](#pydocfmt)
  - [pycommentfmt](#pycommentfmt)
- [Configuration](#configuration)
- [Examples](#examples)
- [Integration](#integration)
  - [Pre-commit](#pre-commit)
  - [Editor Integration](#editor-integration)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

Install pyformatter via pip:

```bash
pip install pyformatter
```

Or install from source:

```bash
git clone https://github.com/RikGhosh487/pyformatter.git
cd pyformatter
pip install -e .
```

---

## Quick Start

Format all Python files in your project:

```bash
# Format docstrings
pydocfmt src/

# Format comments  
pycommentfmt src/

# Check formatting without making changes
pydocfmt --check src/
pycommentfmt --check src/
```

---

## Command Line Usage

### pydocfmt

Format Python docstrings with intelligent Google-style docstring support.

```bash
pydocfmt [OPTIONS] [FILES/DIRECTORIES]
```

**Options:**
- `--line-length INTEGER`: Maximum line length for docstrings (default: 88)
- `--check`: Check if files are formatted correctly without modifying them
- `--include TEXT`: Regex pattern for files to include
- `--exclude TEXT`: Regex pattern for files to exclude
- `--help`: Show help message and exit

**Examples:**
```bash
# Format specific files
pydocfmt myfile.py another_file.py

# Format entire directory
pydocfmt src/

# Check formatting without changes
pydocfmt --check src/

# Custom line length
pydocfmt --line-length 100 src/

# Include/exclude patterns
pydocfmt --include ".*\.py$" --exclude "test_.*\.py$" src/
```

### pycommentfmt

Format Python comments to ensure proper line length and readability.

```bash
pycommentfmt [OPTIONS] [FILES/DIRECTORIES]
```

**Options:**
- `--line-length INTEGER`: Maximum line length for comments (default: 88)
- `--check`: Check if files are formatted correctly without modifying them
- `--include TEXT`: Regex pattern for files to include
- `--exclude TEXT`: Regex pattern for files to exclude
- `--help`: Show help message and exit

**Examples:**
```bash
# Format specific files
pycommentfmt myfile.py

# Format entire directory
pycommentfmt src/

# Check formatting without changes
pycommentfmt --check src/

# Custom line length
pycommentfmt --line-length 79 src/
```

---

## Configuration

pyformatter can be configured via `pyproject.toml`:

```toml
[tool.pydocfmt]
line_length = 88
exclude = '(^tests/data/|build/)'

[tool.pycommentfmt]
line_length = 88
exclude = '(^tests/data/|build/)'
```

**Configuration Options:**
- `line_length`: Maximum line length (default: 88)
- `exclude`: Regex pattern for files/directories to exclude

---

## Examples

### Before and After: pydocfmt

**Before:**
```python
def calculate_mean(numbers):
    """Calculate the arithmetic mean of a list of numbers.
    
    This function calculates the arithmetic mean of a list of numbers and returns the result as a float value."""
    return sum(numbers) / len(numbers)
```

**After:**
```python
def calculate_mean(numbers):
    """Calculate the arithmetic mean of a list of numbers.
    
    This function calculates the arithmetic mean of a list of numbers and returns the
    result as a float value.
    """
    return sum(numbers) / len(numbers)
```

### Before and After: pycommentfmt

**Before:**
```python
# This is a very long comment that exceeds the line length limit and should be wrapped to multiple lines for better readability
x = 42
```

**After:**
```python
# This is a very long comment that exceeds the line length limit and should be
# wrapped to multiple lines for better readability
x = 42
```

---

## Integration

### Pre-commit

Add pyformatter to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/RikGhosh487/pyformatter
    rev: v0.1.0
    hooks:
      - id: pydocfmt
        args: [--line-length=88]
      - id: pycommentfmt
        args: [--line-length=88]
```

### Editor Integration

pyformatter works great with:
- **VS Code**: Use with the Python extension
- **PyCharm**: Configure as an external tool
- **Vim/Neovim**: Integrate with formatting plugins

---

## Why pyformatter?

- **Uncompromising**: Consistent formatting across your entire codebase
- **Fast**: Efficiently processes large codebases
- **Configurable**: Adapt to your team's style preferences
- **Reliable**: Extensively tested with comprehensive test suite
- **Simple**: Easy to integrate into existing workflows

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Inspired by the excellent work of:
- [Black](https://github.com/psf/black) - The uncompromising Python code formatter
- [isort](https://github.com/PyCQA/isort) - A Python utility to sort imports
- [docformatter](https://github.com/PyCQA/docformatter) - Formats docstrings to follow conventions

---

*pyformatter: Because every comment and docstring deserves to be beautiful.*