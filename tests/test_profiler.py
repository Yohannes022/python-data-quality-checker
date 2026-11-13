
import pandas as pd

from data_quality_checker.profiler import profile_dataset


def test_profile_dataset():

    df = pd.DataFrame({
        "name": ["Abebe", "Marta", "Abebe"],
        "age": [25, None, 25],
        "country": ["Ethiopia", "Ethiopia", "Ethiopia"]
    })

    result = profile_dataset(df)

    assert result["total_rows"] == 3
    assert result["total_columns"] == 3

    assert result["duplicate_rows"] == 1

    assert result["missing_values"]["age"]["count"] == 1

    assert result["constant_columns"] == ["country"]
