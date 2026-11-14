
import pandas as pd
import pytest

from data_quality_checker.loader import load_data


def test_load_data(tmp_path):

    file_path = tmp_path / "sample.csv"

    file_path.write_text(
        "name,age\nAbebe,25\nMarta,30\n",
        encoding="utf-8"
    )

    df = load_data(file_path)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["name", "age"]


def test_file_not_found():

    with pytest.raises(FileNotFoundError):
        load_data("nonexistent.csv")


def test_empty_csv(tmp_path):

    file_path = tmp_path / "empty.csv"
    file_path.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        load_data(file_path)
