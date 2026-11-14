"""
This module generates a JSON report.
Functions for generating data quality reports. 
"""

import json
from pathlib import Path

def generate_report(
		profile: dict,
		outlier: dict,
		output_path: str | Path
) -> Path:
	
	"""
	Generate and save a JSON data quality report.

	Args:
		profile: Dataset profiling results.
		outlier: Outlier detection result.
		output_path: Destination for JSON report.

	Returns:
		path to the generated report. 
	"""

	output_path = Path(output_path)

	report = {
		"dataset_profile": profile,
		"outlier_analysis": outlier
	}

	output_path.parent.mkdir(
		parents=True,
		exist_ok=True
	)

	with output_path.open(
		"w",
		encoding="utf-8"
	) as file:
		json.dump(
			report,
			file,
			indent=4,
			ensure_ascii=False
		)
	return output_path