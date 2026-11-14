"""
This module detects numerical outliers using Interquartile Range (IQR) method.
Functions for detecting data quality issues.
"""

import pandas as pd

def detect_outliers(
		df: pd.DataFrame,
		multiplier: float = 1.5
) -> dict:
	
	"""
	Detect numerical outliers using IQR method.

	Lower bound = Q1 - multiplier * IQR
	Upper bound = Q3 + multiplier * IQR

	Returns:
		Dictionary containing outlier statistics.
	"""

	if multiplier <=0:
		raise ValueError(
			"Multiplier must be greater than zero."
		)

	numeric_df = df.select_dtypes(
		include="number"
	)

	results = {}

	for column in numeric_df.columns:
		series = numeric_df[column].dropna()

		if series.empty:
			continue

		q1 = series.quantile(0.25)
		q3 = series.quantile(0.75)

		iqr = q3 - q1

		lower_bound = q1 - multiplier * iqr
		upper_bound = q3 + multiplier * iqr

		outliers = series[
			(series < lower_bound) | 
			(series > upper_bound)
		]

		results[column] = {
			"outlier_count": int(len(outliers)),
			"outlier_percentage": round(
				float(len(outliers) / len(series) * 100),
				2
			),
			"lower_bound": float(lower_bound),
			"upper_bound": float(upper_bound),
			"outlier_values": [
				float(value)
				for value in outliers.tolist()
			],
		}

	return results