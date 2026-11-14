"""
This is the entry point and connectes all the modules.
Command-line Interface for Data Quality Checker.
"""


"""Command-line interface for Data Quality Checker."""

# import pandas as pd
import argparse
from pathlib import Path

from .loader import load_data
from .profiler import profile_dataset
from .detectors import detect_outliers
from .reporter import generate_report


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Analyze CSV datasets and detect "
            "data quality issues."
        )
    )

    parser.add_argument(
        "file",
        help="Path to the CSV dataset."
    )

    parser.add_argument(
        "--output",
        default="reports/quality_report.json",
        help="Path for the JSON quality report."
    )

    parser.add_argument(
        "--clean-output",
        help="Optional path to save a cleaned CSV."
    )

    parser.add_argument(
        "--drop-duplicates",
        action="store_true",
        help="Remove duplicate rows when exporting cleaned data."
    )

    parser.add_argument(
        "--drop-missing",
        action="store_true",
        help="Remove rows containing missing values when exporting cleaned data."
    )

    args = parser.parse_args()

    try:
        # Load dataset
        df = load_data(args.file)

        print("\nDATASET LOADED SUCCESSFULLY")
        print("-" * 40)

        # Profile dataset
        profile = profile_dataset(df)

        # Detect outliers
        outliers = detect_outliers(df)

        # Generate report
        report_path = generate_report(
            profile,
            outliers,
            args.output
        )

        print("\nDATASET PROFILE")
        print("-" * 40)

        print(f"Rows: {profile['total_rows']}")
        print(f"Columns: {profile['total_columns']}")

        print(
            f"Duplicate rows: "
            f"{profile['duplicate_rows']}"
        )

        print("\nMISSING VALUES")

        for column, details in (
            profile["missing_values"].items()
        ):
            print(
                f"{column}: {details['count']} "
                f"({details['percentage']}%)"
            )

        print("\nOUTLIER DETECTION")

        for column, details in outliers.items():
            print(
                f"{column}: "
                f"{details['outlier_count']} outliers"
            )

        print("\nCONSTANT COLUMNS")
        print(profile["constant_columns"])

        print("\nREPORT GENERATED")
        print(report_path)

        # Optional data cleaning
        if args.clean_output:

            cleaned_df = df.copy()

            if args.drop_duplicates:
                cleaned_df = (
                    cleaned_df.drop_duplicates()
                )

            if args.drop_missing:
                cleaned_df = cleaned_df.dropna()

            # clean_path = args.clean_output

            # cleaned_df.to_csv(
            #     clean_path,
            #     index=False
            # )
            clean_path = Path(args.clean_output)

            clean_path.parent.mkdir(
               parents=True,
               exist_ok=True
            )

            cleaned_df.to_csv(
               clean_path,
               index=False
            )

            print("\nCLEANED DATASET SAVED")
            print(clean_path)

    except (FileNotFoundError, ValueError) as error:
        parser.exit(
            status=1,
            message=f"\nError: {error}\n"
        )


if __name__ == "__main__":
    main()
