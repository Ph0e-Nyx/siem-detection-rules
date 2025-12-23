# Contributing to SIEM Detection Rules

First off, thanks for taking the time to contribute! 🎉

The following is a set of guidelines for contributing to the SIEM Detection Rules repository. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

- **Use a clear and descriptive title** for the issue to identify the problem.
- **Describe the exact steps which reproduce the problem** in as much detail as possible.
- **Provide specific examples** to demonstrate the steps.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new rules and minor improvements to existing functionality.

- **Use a clear and descriptive title** for the issue to identify the suggestion.
- **Provide a step-by-step description of the suggested enhancement** in as much detail as possible.
- **Explain why this enhancement would be useful** to most users.

### Pull Requests

- Fill in the required template
- Do not include issue numbers in the PR title
- Include screenshots and animated GIFs in your pull request whenever possible.
- Follow the [Sigma Rule Standard](https://github.com/SigmaHQ/sigma/wiki/Specification) for new rules.

## Styleguides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Rule Metadata

All rules must include:
- `title`: Brief, descriptive title
- `id`: Unique UUID
- `status`: experimental, test, or stable
- `description`: Detailed description of the detection
- `author`: Your name/handle
- `date`: Creation date
- `tags`: MITRE ATT&CK tags (e.g., `attack.initial_access`, `attack.t1566`)
- `logsource`: Category, product, and service
- `detection`: The logic itself
- `falsepositives`: Known benign activities that might trigger the rule
- `level`: critical, high, medium, or low

## Attribution

This guide is based on the **contributing-gen**. [Make your own](https://github.com/bttger/contributing-gen)!
