# TcUnit pre-commit

Pre-commit hooks for [TcUnit](https://tcunit.org/) library.

This pre-commit checks if your `METHOD` name is the same as name passed to `TEST('...')`. This is also how the [TcUnit examples](https://tcunit.org/#/introduction-user-guide?id=create-test-suites-and-run-them) are set up.

Your project looks as follows:

```
MyFunction.TcPOU
MyFunction_Tests.TcPOU
└─ TestSomething()
└─ TestSomethingElse()
```

Where `TestSomething()` looks as follows:

```
METHOD TestSomething

TEST('TestSomething')
...
```
## Usage

Add the following to your existing `.pre-commit-config.yml` file or create one.



```yaml
  - repo: https://github.com/InspireHornets/tcunit-precommit
    rev: v0.1.0
    hooks:
      - id: unittest-name-fixer
        # --fix: fixes non-matching method - test names
        args: [--fix]
        # Only check files that end in _Tests.TcPOU, because that is how I name my tests
        files: '.*_Tests\.TcPOU$'
```

## Developers

```bash
# Create conda environment with necessary dependencies
conda env create -f conda.yml
# activate environment
conda activate tcunit-pc312
# Install development dependencies
pip install .[dev]
# Install/activate pre-commits of this repo. Assumes you have pre-commit installed globally
pre-commit install
```
