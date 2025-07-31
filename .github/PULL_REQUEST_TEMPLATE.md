## Description

Brief description of the changes and the motivation behind them.

Fixes #(issue)

## Type of Change

Please delete options that are not relevant.

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring (no functional changes)
- [ ] Test coverage improvement
- [ ] Dependency update

## Changes Made

Please provide a clear list of changes made:

- 
- 
- 

## Testing

### Test Coverage
- [ ] New tests added for new functionality
- [ ] All existing tests pass
- [ ] Test coverage maintained or improved

### Manual Testing
- [ ] Tested locally with various Python files
- [ ] Tested edge cases and error conditions
- [ ] Verified CLI functionality works as expected

### Test Commands Run
```bash
# Add the commands you used to test your changes
python -m unittest discover -s tests -v
# python -m pytest tests/ --cov=pyformatter
# pydocfmt --check .
# pycommentfmt --check .
```

## Formatting and Style

- [ ] Code follows the project's style guidelines
- [ ] `black` formatting applied
- [ ] `isort` import sorting applied
- [ ] `pydocfmt` docstring formatting applied
- [ ] `pycommentfmt` comment formatting applied
- [ ] Pre-commit hooks pass

## Documentation

- [ ] Docstrings added/updated for new functions and classes
- [ ] README.md updated if needed
- [ ] CHANGELOG.md updated (for significant changes)
- [ ] Comments added for complex logic
- [ ] Type hints added for new functions

## Performance and Compatibility

- [ ] Changes don't negatively impact performance
- [ ] Compatible with Python 3.11+
- [ ] Cross-platform compatibility maintained (Windows, macOS, Linux)
- [ ] Memory usage is reasonable for large files

## Security Considerations

- [ ] No new security vulnerabilities introduced
- [ ] Input validation added where appropriate
- [ ] File path handling is secure
- [ ] No sensitive information exposed in logs or output

## Screenshots (if applicable)

For CLI changes or output formatting changes, please add before/after examples:

**Before:**
```
# Example of current behavior
```

**After:**
```
# Example of new behavior
```

## Related Issues and PRs

- Related Issue: #
- Depends on: #
- Blocks: #

## Breaking Changes

If this is a breaking change, please describe:

1. What functionality is being changed or removed
2. Why the change is necessary
3. How users should update their code
4. Migration guide (if complex)

## Additional Notes

Any additional information, considerations, or context that reviewers should know:

- 
- 
- 

## Reviewer Checklist

*For the reviewer - please check these items during review:*

### Code Quality
- [ ] Code is readable and well-structured
- [ ] Appropriate error handling is in place
- [ ] No code duplication
- [ ] Functions are focused and have single responsibilities
- [ ] Variable and function names are descriptive

### Testing
- [ ] Tests cover the new functionality
- [ ] Tests include edge cases
- [ ] All tests pass locally and in CI
- [ ] Test names are descriptive

### Documentation
- [ ] Code is self-documenting or well-commented
- [ ] Public APIs are documented
- [ ] Examples are provided where helpful

### Performance
- [ ] No obvious performance regressions
- [ ] Efficient algorithms used
- [ ] Memory usage is reasonable

### Security
- [ ] Input validation is appropriate
- [ ] No security vulnerabilities introduced
- [ ] File operations are safe

## Post-Merge Checklist

*To be completed after merging:*

- [ ] Delete feature branch
- [ ] Update local main branch
- [ ] Monitor for any issues in production use
- [ ] Update project board/issues if applicable

---

**Note to Contributors:**
- Please ensure all checkboxes are completed before requesting review
- Feel free to delete sections that don't apply to your PR
- If you need help with any of these requirements, please ask in the PR comments

**Note to Reviewers:**
- Please provide constructive feedback
- Check that the PR follows our [Contributing Guidelines](../CONTRIBUTING.md)
- Consider the impact on existing users
- Test the changes locally if possible
