#!/usr/bin/env python3
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("pandas is not installed. Please install pandas (pip install pandas pyreadstat) and retry.")
    sys.exit(1)

sas_path = Path(__file__).parent.parent / 'data' / 'STU_QQQ_SAS' / 'CY08MSP_STU_QQQ.SAS7BDAT'
if not sas_path.exists():
    print(f"SAS file not found at {sas_path}. Please check the path.")
    sys.exit(1)

# Read the SAS file
try:
    stu = pd.read_sas(str(sas_path), format='sas7bdat', encoding='latin1')
except Exception as e:
    print(f"Error reading SAS file: {e}")
    sys.exit(1)

country_id_var = 'CNT'
pv_var = 'PV1MATH'
weight_var = 'W_FSTUWT'

# Convert to numeric and drop NA similar to notebook
stu[pv_var] = pd.to_numeric(stu[pv_var], errors='coerce')
stu[weight_var] = pd.to_numeric(stu[weight_var], errors='coerce')

df_mean = stu[[country_id_var, pv_var, weight_var]].dropna()

weighted_sum = df_mean.groupby(country_id_var).apply(lambda x: (x[pv_var] * x[weight_var]).sum())
total_weight = df_mean.groupby(country_id_var)[weight_var].sum()
mean_math_scores = (weighted_sum / total_weight).rename('Mean_Math_Score')

# Prepare output files
out_dir = Path(__file__).parent.parent / 'temp'
out_dir.mkdir(parents=True, exist_ok=True)
csv_path = out_dir / 'mean_math_countries.csv'
json_path = out_dir / 'mean_math_countries.json'

# Save country codes (index) as CSV (one column) and JSON (list)
mean_math_scores.index.to_series().to_csv(csv_path, index=False, header=['CountryCode'])
mean_math_scores.index.to_list()
import json
with open(json_path, 'w') as f:
    json.dump(mean_math_scores.index.to_list(), f, indent=2)

print(f"Wrote {len(mean_math_scores)} country codes to:")
print(f"  {csv_path}")
print(f"  {json_path}")
