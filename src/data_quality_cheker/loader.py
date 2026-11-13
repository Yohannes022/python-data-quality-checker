"""Functions for loading datasets."""

from pathlib import Path
import pandas as pd

def load_data(file_path: str | Path) -> pd.DataFrame:
	"""
	Load a CSV file into. a pandas DataFrame.
	
	Args: 
		file_path: Path to CSV file.

	Returns: 
		Loaded pandas DataFrame.

	Raises:
		FileNotFoundError: If the file dose not exist.
		ValueError: If the fiile is empty or cannot be parsed.
	"""

	file_path = Path(file_path)

	if not file_path.exists():
		raise FileNotFoundError(
			f"File not found: {file_path}"
		)

	if not file_path.is_file():
		raise ValueError(
			f"Path is not a file: {file_path}"
		)

	try:
		df = pd.read_csv(file_path)

	except pd.errors.EmptyDataError as exc:
		raise ValueError(
			f"The CSV file is empty: {file_path}"
		) from exc

	except pd.errors.ParserError as exc:
		raise ValueError(
			f"Unable to parse CSV file: {file_path}"
		) from exc

	except UnicodeDecodeError as exc:
		raise ValueError(
			"Unable to decode the CSV file."
			"Check ts text encoding."
		) from exc

	if len(df.columns) == 0:
		raise ValueError(
			"The CSV file does not contain any columns."
		)

	return df