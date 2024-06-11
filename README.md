# TcUnit pre-commit

Pre-commit hooks for [TcUnit](https://tcunit.org/) library.

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
