# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

The pyformatter team takes security bugs seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

To report a security issue, please use the GitHub Security Advisory ["Report a Vulnerability"](https://github.com/RikGhosh487/pyformatter/security/advisories/new) tab.

The pyformatter team will send a response indicating the next steps in handling your report. After the initial reply to your report, the security team will keep you informed of the progress towards a fix and full announcement, and may ask for additional information or guidance.

### When Should I Report a Vulnerability?

You should report a vulnerability if you have discovered:

- **Code injection vulnerabilities** that could allow arbitrary code execution
- **Path traversal vulnerabilities** that could allow access to files outside the intended scope
- **Denial of service vulnerabilities** that could be exploited to make the tool unusable
- **Information disclosure vulnerabilities** that could expose sensitive data
- **Any other security issue** that could compromise user systems or data

### What Information Should I Include?

When reporting a vulnerability, please include:

- **Type of issue** (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
- **Full paths of source file(s)** related to the manifestation of the issue
- **The location of the affected source code** (tag/branch/commit or direct URL)
- **Any special configuration required** to reproduce the issue
- **Step-by-step instructions to reproduce the issue**
- **Proof-of-concept or exploit code** (if possible)
- **Impact of the issue**, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

## Security Considerations for pyformatter

### Input Validation

pyformatter processes Python source code files, which presents certain security considerations:

- **Malicious Python files**: While pyformatter parses Python AST, it does not execute the code. However, the AST parsing itself could potentially be exploited.
- **Path traversal**: Care is taken to ensure that file operations remain within intended directories.
- **Resource exhaustion**: Large files or deeply nested structures could potentially cause resource exhaustion.

### Safe Usage Guidelines

To use pyformatter safely:

1. **Run in isolated environments** when processing untrusted code
2. **Validate file paths** before processing
3. **Monitor resource usage** when processing large codebases
4. **Keep pyformatter updated** to the latest version
5. **Review changes** made by pyformatter before committing

### Dependencies

pyformatter has minimal dependencies to reduce the attack surface:

- **Zero runtime dependencies**: The core package has no external dependencies
- **Development dependencies**: Only well-maintained, security-conscious packages are used for development

## Security Update Process

When a security vulnerability is reported:

1. **Acknowledgment**: We'll acknowledge receipt within 24 hours
2. **Investigation**: We'll investigate and assess the severity within 72 hours
3. **Fix development**: We'll develop and test a fix
4. **Disclosure coordination**: We'll coordinate disclosure with the reporter
5. **Release**: We'll release a security update and publish an advisory
6. **Communication**: We'll notify users through multiple channels

### Security Releases

Security releases will be:

- **Prioritized**: Released as soon as possible after a fix is available
- **Clearly marked**: Version numbers and release notes will indicate security fixes
- **Documented**: Security advisories will detail the vulnerability and mitigation steps
- **Backward compatible**: When possible, security fixes will be backward compatible

## Security Best Practices

### For Users

- **Keep updated**: Always use the latest version of pyformatter
- **Review output**: Always review changes made by pyformatter before committing
- **Isolate processing**: When processing untrusted code, use containers or virtual environments
- **Monitor logs**: Watch for any unusual behavior or errors

### For Contributors

- **Security mindset**: Consider security implications of all changes
- **Input validation**: Validate all user inputs and file paths
- **Error handling**: Implement proper error handling to prevent information leakage
- **Testing**: Include security-focused test cases
- **Dependencies**: Carefully evaluate any new dependencies

## Scope

This security policy applies to:

- **pyformatter core package**: All code in the main pyformatter package
- **CLI tools**: pydocfmt and pycommentfmt command-line interfaces
- **Configuration handling**: pyproject.toml and other configuration processing
- **File operations**: All file reading, writing, and path handling

This policy does not cover:

- **Third-party dependencies**: Issues in dependencies should be reported to their respective maintainers
- **User environments**: Security issues in user environments or configurations
- **Integration tools**: Issues in editors, CI/CD systems, or other integration points

## Recognition

We appreciate the security research community and will recognize researchers who help improve pyformatter's security:

- **Public acknowledgment**: With your permission, we'll acknowledge your contribution in our security advisories
- **Hall of fame**: We maintain a list of security researchers who have helped improve pyformatter
- **Communication**: We'll keep you informed throughout the process and coordinate on disclosure timing

## Contact

For security-related questions or concerns that don't constitute a vulnerability report:

- **General security questions**: Open a discussion in [GitHub Discussions](https://github.com/RikGhosh487/pyformatter/discussions)
- **Security policy questions**: Contact the maintainers through GitHub Issues (for non-sensitive matters)

## Resources

- [GitHub Security Advisories](https://github.com/RikGhosh487/pyformatter/security/advisories)
- [Python Security](https://python.org/news/security/)
- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [Common Vulnerability Scoring System (CVSS)](https://www.first.org/cvss/)

---

**Note**: This security policy may be updated from time to time. Please check back regularly for the most current version.

Last updated: January 31, 2025
