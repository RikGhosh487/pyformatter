## 🐛 Bug Fixes - Multi-line Summary Support

This patch release improves the handling of multi-line summaries in Google-style docstring formatting.

### Fixed
- Multi-line summaries are now properly treated as a single summary block instead of splitting into summary + description
- Proper blank line spacing between summary and sections when no description is present  
- Improved formatting consistency for various docstring structures
- Enhanced multi-line summary support in Google-style docstring formatting

### Before vs After
**Before (v0.1.0):**
```python
def func():
    """This is a summary line that is long and goes past the allowed line
    
    width but is still part of the summary.
    
    This is the description
    """
```

**After (v0.1.1):**
```python  
def func():
    """This is a summary line that is long and goes past the allowed line
    width but is still part of the summary.
    
    This is the description
    """
```

### Installation
```bash
pip install python-doc-formatter==0.1.1
```

### What's Next
See our [roadmap](https://github.com/RikGhosh487/pyformatter/blob/main/CHANGELOG.md#future-roadmap) for upcoming features including NumPy-style docstring support.

---

**Full Changelog**: https://github.com/RikGhosh487/pyformatter/compare/v0.1.0...v0.1.1
