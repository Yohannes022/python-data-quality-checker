
"""
This module handles general dataset profiling.
It inspects and summarizes the structure and quality of a dataset.
"""

import pandas as pd


def profile_dataset(df: pd.DataFrame) -> dict:
    """
    Generate a general profile of a DataFrame.

    Returns:
        Dictionary containing dataset statistics.
    """

    # Calculate missing values
    missing_values = df.isnull().sum()

    # Calculate missing-value percentages
    missing_percentage = (
        (missing_values / len(df)) * 100
        if len(df) > 0
        else missing_values.astype(float)
    )

    # Count duplicate rows
    duplicate_rows = int(df.duplicated().sum())

    # Identify column data types
    column_types = {
        column: str(dtype)
        for column, dtype in df.dtypes.items()
    }

    # Count unique values in each column
    unique_values = {
        column: int(df[column].nunique())
        for column in df.columns
    }

    # Identify constant columns
    constant_columns = [
        column
        for column in df.columns
        if len(df) > 0
        and df[column].nunique(dropna=False) <= 1
    ]

    # Create missing-value summary
    missing_summary = {}

    for column in df.columns:
        missing_summary[column] = {
            "count": int(missing_values[column]),
            "percentage": round(
                float(missing_percentage[column]), 2
            ),
        }

    return {
        "total_rows": int(df.shape[0]),
        "total_columns": int(df.shape[1]),
        "memory_usage_bytes": int(
            df.memory_usage(deep=True).sum()
        ),
        "duplicate_rows": duplicate_rows,
        "column_types": column_types,
        "unique_values": unique_values,
        "missing_values": missing_summary,
        "constant_columns": constant_columns,
    }
