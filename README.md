# practical-python-projects

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/K-Saikrishnan/practical-python-projects/main.svg)](https://results.pre-commit.ci/latest/github/K-Saikrishnan/practical-python-projects/main)
[![CI](https://github.com/K-Saikrishnan/practical-python-projects/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/K-Saikrishnan/practical-python-projects/actions/workflows/ci.yaml)
[![CodeQL](https://github.com/K-Saikrishnan/practical-python-projects/actions/workflows/github-code-scanning/codeql/badge.svg?branch=main)](https://github.com/K-Saikrishnan/practical-python-projects/actions/workflows/github-code-scanning/codeql)
[![pages-build-deployment](https://github.com/K-Saikrishnan/practical-python-projects/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/K-Saikrishnan/practical-python-projects/actions/workflows/pages/pages-build-deployment)

Implementations of projects in <https://github.com/karan/Projects>

## Local Development

- Create a virtual environment: `python -m venv .venv`

- Activate the virtual environment:
  - Linux/MacOS: `source .venv/bin/activate`
  - Windows: `.venv\Scripts\activate`
  - Git Bash: `source .venv/Scripts/activate`

- Install packages: `pip install -r requirements.txt`

- Install pre-commit hooks: `pre-commit install`

- Run pre-commit: `pre-commit run --all-files`

- Run tests: `python -m pytest`
