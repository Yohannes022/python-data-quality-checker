
import pandas as pd
import pytest

from data_quality_checker.detectors import detect_outliers


def test_detect_outliers():

    df = pd.DataFrame({
        "salary": [
            5000, 5200, 5100, 5300,
            5400, 5500, 5600, 200000
        ]
    })

    result = detect_outliers(df)

    assert result["salary"]["outlier_count"] == 1

    assert result["salary"]["outlier_values"] == [
        200000.0
    ]


def test_ignore_missing_values():

    df = pd.DataFrame({
        "salary": [5000, 5100, None, 5200, 5300]
    })

    result = detect_outliers(df)

    assert result["salary"]["outlier_count"] == 0


def test_invalid_multiplier():

    df = pd.DataFrame({
        "salary": [100, 200, 300]
    })

    with pytest.raises(ValueError):
        detect_outliers(df, multiplier=0)
