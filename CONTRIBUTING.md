# Contributing to pyformatter

Thank you for your interest in contributing to pyformatter! We welcome contributions from everyone and are grateful for every pull request, bug report, and feature suggestion.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Code Style](#code-style)
- [Submitting Changes](#submitting-changes)
- [Release Process](#release-process)
- [Getting Help](#getting-help)

## Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow. Please be respectful and constructive in all interactions.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Git
- A GitHub account

### Types of Contributions

We welcome several types of contributions:

- **🐛 Bug Reports**: Help us identify and fix issues
- **✨ Feature Requests**: Suggest new functionality
- **📝 Documentation**: Improve or add documentation
- **🔧 Code**: Fix bugs or implement features
- **🧪 Tests**: Add or improve test coverage
- **🎨 Examples**: Provide usage examples

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/pyformatter.git
cd pyformatter
```

### 2. Set Up Development Environment

```bash
# Create a virtual environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Activate it (macOS/Linux)
source .venv/bin/activate

# Install development dependencies
pip install -e .[dev]
```

### 3. Set Up Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Test the hooks
pre-commit run --all-files
```

### 4. Verify Installation

```bash
# Test the CLI tools
pydocfmt --help
pycommentfmt --help

# Run tests
python -m unittest discover -s tests -v
```

## Making Changes

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-description
```

### Branch Naming Convention

- **Features**: `feature/description-of-feature`
- **Bug fixes**: `bugfix/issue-description`
- **Documentation**: `docs/what-you-are-documenting`
- **Tests**: `test/what-you-are-testing`

### 2. Make Your Changes

#### For Bug Fixes:
1. Write a test that reproduces the bug
2. Fix the bug
3. Ensure the test passes
4. Update documentation if needed

#### For New Features:
1. Discuss the feature in an issue first (for major changes)
2. Write tests for the new functionality
3. Implement the feature
4. Update documentation
5. Add examples if applicable

### 3. Code Guidelines

#### Python Code Style
- Follow PEP 8
- Use type hints for all function parameters and return values
- Write docstrings for all public functions and classes
- Keep functions focused and small
- Use descriptive variable and function names

#### Documentation Style
- Use Google-style docstrings
- Include examples in docstrings when helpful
- Keep line length to 88 characters
- Use proper Markdown formatting

## Testing

### Running Tests

```bash
# Run all tests
python -m unittest discover -s tests -v

# Run tests with coverage
python -m pytest tests/ --cov=pyformatter --cov-report=html

# Run specific test file
python -m unittest tests.test_pydocfmt -v
```

### Writing Tests

- Write tests for all new functionality
- Include edge cases and error conditions
- Use descriptive test method names
- Follow the existing test patterns

#### Test File Structure
```python
import unittest
from pyformatter.formatters.your_module import your_function

class TestYourFunction(unittest.TestCase):
    def test_normal_case(self):
        """Test the normal expected behavior."""
        # Arrange
        input_data = "test input"
        expected = "expected output"
        
        # Act
        result = your_function(input_data)
        
        # Assert
        self.assertEqual(result, expected)

    def test_edge_case(self):
        """Test edge cases."""
        pass

if __name__ == "__main__":
    unittest.main()
```

## Code Style

We use several tools to maintain code quality:

### Automated Formatting
- **Black**: Code formatting
- **isort**: Import sorting
- **pydocfmt**: Docstring formatting (our own tool!)
- **pycommentfmt**: Comment formatting (our own tool!)

### Code Quality
- **MyPy**: Type checking (when available)
- **Pre-commit**: Automated checks

### Running Style Checks

```bash
# Format code
black .
isort .
pydocfmt .
pycommentfmt .

# Check formatting without changes
black --check .
isort --check-only .
pydocfmt --check .
pycommentfmt --check .
```

## Submitting Changes

### 1. Before Submitting

- [ ] All tests pass
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive
- [ ] Changes are focused and atomic

### 2. Commit Message Format

Use clear, descriptive commit messages:

```
type: short description (50 chars or less)

Longer description if needed. Explain what and why, not how.
Include any breaking changes or important notes.

Fixes #123
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### 3. Pull Request Process

1. **Push your branch** to your fork
2. **Create a Pull Request** on GitHub
3. **Fill out the PR template** completely
4. **Wait for review** and address feedback
5. **Ensure CI passes** on all checks

#### Pull Request Title Format
```
[Type] Brief description of changes

Examples:
[Feature] Add support for NumPy-style docstrings
[Bugfix] Fix comment wrapping edge case with special characters
[Docs] Update installation instructions
```

#### Pull Request Description Template
```markdown
## Description
Brief description of changes and motivation.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] New tests added for new functionality
- [ ] All existing tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Comments added for complex code
- [ ] No new warnings introduced

## Related Issues
Fixes #(issue number)
```

### 4. Review Process

- **All PRs require review** before merging
- **Address feedback promptly** and professionally
- **Keep discussions focused** on the code
- **Be open to suggestions** and alternative approaches

## Release Process

### Versioning

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Steps (for maintainers)

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create release PR
4. After merge, tag the release
5. Create GitHub release
6. Publish to PyPI

## Project Structure

```
pyformatter/
├── pyformatter/           # Main package
│   ├── cli/              # Command-line interfaces
│   ├── formatters/       # Core formatting logic
│   ├── config.py         # Configuration handling
│   └── utils.py          # Utility functions
├── tests/                # Test suite
├── docs/                 # Documentation (if needed)
├── .github/              # GitHub workflows
├── pyproject.toml        # Project configuration
├── README.md             # Project overview
├── CHANGELOG.md          # Change history
└── CONTRIBUTING.md       # This file
```

## Development Tips

### Debugging
- Use `python -m pdb` for debugging
- Add print statements or logging for complex issues
- Test with various Python files to ensure compatibility

### Performance
- Consider performance impact for large files
- Profile code when making optimization changes
- Keep memory usage reasonable

### Compatibility
- Test with different Python versions (3.11+)
- Ensure cross-platform compatibility (Windows, macOS, Linux)
- Consider edge cases in file handling

## Getting Help

### Communication Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Request Comments**: Code-specific discussions

### Asking Good Questions
1. **Search existing issues** first
2. **Provide minimal reproducible examples**
3. **Include environment details** (Python version, OS, etc.)
4. **Be specific** about expected vs. actual behavior

### Useful Resources
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Google Style Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)

## Recognition

Contributors will be recognized in:
- Release notes
- GitHub contributors list
- Special thanks for significant contributions

Thank you for contributing to pyformatter! 🎉

---

## Quick Reference

### Common Commands
```bash
# Development setup
pip install -e .[dev]
pre-commit install

# Testing
python -m unittest discover -s tests -v

# Formatting
black . && isort . && pydocfmt . && pycommentfmt .

# Check formatting
black --check . && isort --check-only . && pydocfmt --check . && pycommentfmt --check .
```

### Need Help?
- 📖 Read the [README](README.md)
- 🐛 [Report a bug](https://github.com/RikGhosh487/pyformatter/issues/new)
- 💡 [Request a feature](https://github.com/RikGhosh487/pyformatter/issues/new)
- 💬 [Start a discussion](https://github.com/RikGhosh487/pyformatter/discussions)
