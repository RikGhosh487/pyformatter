# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project release preparation
- Comprehensive README with usage examples and integration guides

## [0.1.0] - 2025-01-31

### Added
- **pydocfmt**: Command-line tool for formatting Python docstrings
  - Google-style docstring formatting support
  - Intelligent line wrapping for docstring sections (Args, Returns, Raises, Examples, etc.)
  - Preservation of code blocks in Examples sections with automatic fencing
  - Support for parameter descriptions with type annotations
  - Proper handling of multi-paragraph descriptions and lists
  - Configuration via `pyproject.toml` and command-line arguments

- **pycommentfmt**: Command-line tool for formatting Python comments
  - Automatic comment line wrapping based on configurable line length
  - Intelligent handling of inline comments vs. block comments
  - Preservation of special comments (noqa, type: ignore, pylint directives, etc.)
  - Smart spacing correction for inline comments
  - Preservation of code-style comment blocks
  - Long inline comment extraction to separate comment blocks

- **Core Infrastructure**:
  - Configurable line length (default: 88 characters)
  - Include/exclude file patterns with regex support
  - Check mode for CI/CD integration (non-destructive validation)
  - Recursive directory processing
  - TOML configuration support via `pyproject.tool.<formatter>`

- **CLI Features**:
  - `--check` flag for validation without modification
  - `--line-length` for custom line length configuration
  - `--include` and `--exclude` for file filtering
  - Exit code 1 when formatting issues are detected in check mode

- **Google-style Docstring Support**:
  - Args/Arguments section formatting with type annotations
  - Returns/Return section formatting
  - Raises/Raise section formatting with exception backticks
  - Yields/Yield section formatting
  - Examples section with automatic code block fencing
  - Attributes section formatting
  - Intelligent paragraph and list handling in descriptions

- **Comment Formatting Features**:
  - Block comment rewrapping with proper indentation preservation
  - Inline comment spacing standardization
  - Long inline comment extraction and placement above code
  - Special comment preservation (tool directives, pragmas, etc.)
  - Code comment block detection and preservation

- **Testing & Quality Assurance**:
  - Comprehensive test suite with 100% coverage for core functionality
  - Unit tests for both docstring and comment formatting
  - Edge case handling for malformed docstrings and comments
  - Test coverage for check mode and file modification detection

- **Developer Experience**:
  - Pre-commit hook configuration
  - Pre-commit hooks for external repositories (`.pre-commit-hooks.yaml`)
  - GitHub Actions CI/CD workflows
  - Black and isort integration
  - Development environment configuration

- **Documentation**:
  - Comprehensive README with usage examples
  - Configuration documentation
  - Before/after formatting examples
  - Integration guides for popular tools

### Technical Details
- **Supported Python Versions**: 3.11, 3.12, 3.13+
- **Dependencies**: Pure Python implementation with no external dependencies
- **License**: MIT License
- **Architecture**: Modular design with separate formatters for docstrings and comments

### Configuration Options
- `line_length`: Maximum line length (default: 88)
- `exclude`: Regex pattern for files/directories to exclude
- `include`: Regex pattern for files to include (default: `\.py$`)

### Command-Line Interface
```bash
# Format docstrings
pydocfmt [--line-length=88] [--check] [--include=PATTERN] [--exclude=PATTERN] FILES...

# Format comments
pycommentfmt [--line-length=88] [--check] [--include=PATTERN] [--exclude=PATTERN] FILES...
```

---

## Release Notes

### What's New in v0.1.0

This is the initial release of **pyformatter**, introducing two powerful Python code formatting tools designed to complement existing formatters like Black and isort.

#### Key Features:
- **Intelligent Docstring Formatting**: Automatic Google-style docstring formatting with support for all standard sections
- **Smart Comment Management**: Proper comment wrapping and spacing with preservation of special directives
- **Zero Configuration**: Works out of the box with sensible defaults
- **CI/CD Ready**: Check mode for validation in continuous integration workflows
- **Highly Configurable**: Extensive configuration options via `pyproject.toml`

#### Use Cases:
- **Code Quality**: Ensure consistent docstring and comment formatting across teams
- **CI/CD Integration**: Validate formatting in pull requests and builds
- **Legacy Code**: Automatically format existing codebases for better readability
- **Documentation**: Improve code documentation consistency and readability

---

## Future Roadmap

### Planned Features (v0.2.0)
- Support for NumPy-style docstrings
- Integration with popular IDEs and editors
- Performance optimizations for large codebases
- Additional docstring section types (Note, See Also, References)

### Long-term Vision
- Plugin architecture for custom formatting rules
- Integration with documentation generators
- Support for additional comment styles and formats
- Language server protocol (LSP) support

---

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to:
- Report bugs and request features
- Submit pull requests
- Set up the development environment
- Run tests and quality checks

## Support

- **Issues**: [GitHub Issues](https://github.com/RikGhosh487/pyformatter/issues)
- **Discussions**: [GitHub Discussions](https://github.com/RikGhosh487/pyformatter/discussions)
- **Documentation**: [README](README.md)

---

[Unreleased]: https://github.com/RikGhosh487/pyformatter/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/RikGhosh487/pyformatter/releases/tag/v0.1.0
