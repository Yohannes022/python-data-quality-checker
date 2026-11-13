
# Python Data Quality Checker

A lightweight Python command-line application for profiling
CSV datasets and identifying common data quality issues.

## Features

- Dataset profiling
- Missing value detection
- Duplicate row detection
- Data type inspection
- Unique value analysis
- Constant column detection
- Numerical outlier detection using IQR
- JSON report generation
- Optional removal of duplicate and missing rows
- Automated testing with pytest

## Technologies

- Python
- Pandas
- NumPy
- Pytest

## Project Structure

```text
src/
  data_quality_checker/
    loader.py
    profiler.py
    detectors.py
    reporter.py
    cli.py

tests/
data/
reports/
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd python-data-quality-checker
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project:

```bash
pip install -e ".[dev]"
```

## Usage

Analyze a CSV dataset:

```bash
data-quality data/sample.csv
```

Alternatively:

```bash
python -m data_quality_checker.cli data/sample.csv
```

Specify a custom report destination:

```bash
data-quality data/sample.csv \
  --output reports/my_report.json
```

## Data Cleaning

Remove duplicate rows:

```bash
data-quality data/sample.csv \
  --clean-output data/cleaned.csv \
  --drop-duplicates
```

Remove rows containing missing values:

```bash
data-quality data/sample.csv \
  --clean-output data/cleaned.csv \
  --drop-missing
```

Apply both operations:

```bash
data-quality data/sample.csv \
  --clean-output data/cleaned.csv \
  --drop-duplicates \
  --drop-missing
```

Cleaning always exports a separate file.

The original dataset remains unchanged.

## Testing

Run automated tests:

```bash
pytest -v
```

## Outlier Detection

The application uses the Interquartile Range (IQR)
method to identify potential numerical outliers.

IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 * IQR

Upper Bound = Q3 + 1.5 * IQR

## Output

The application generates a JSON report containing:

- Dataset statistics
- Missing value summaries
- Duplicate records
- Data types
- Unique values
- Constant columns
- Outlier analysis

## Limitations

- CSV input is supported in the initial release.
- Outlier detection focuses on numerical columns.
- Outliers are statistical indicators, not necessarily errors.
- Cleaning rules are intentionally limited to duplicate
  and missing-row removal.

## License

MIT License.
