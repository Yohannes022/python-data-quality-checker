
import pandas as pd
import pytest

from data_quality_checker.loader import load_csv


def test_load_csv(tmp_path):

    file_path = tmp_path / "sample.csv"

    file_path.write_text(
        "name,age\nAbebe,25\nMarta,30\n",
        encoding="utf-8"
    )

    df = load_csv(file_path)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["name", "age"]


def test_file_not_found():

    with pytest.raises(FileNotFoundError):
        load_csv("nonexistent.csv")


def test_empty_csv(tmp_path):

    file_path = tmp_path / "empty.csv"
    file_path.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        load_csv(file_path)
