from pathlib import Path
import pandas as pd

# pull data from merged csv and calculate correlations

# define script directory
try:
    SCRIPT_DIR = Path(__file__).resolve().parent
except NameError:
    # In case of running in notebook / interactive session
    SCRIPT_DIR = Path.cwd()
PROCESSED_DIR = SCRIPT_DIR.parent / "data" / "processed"

# define path for merged data csv
merged_data_file = PROCESSED_DIR / "merged_data_by_zip.csv"

merged_df = pd.read_csv(merged_data_file)

# descriptive statistics
print(merged_df.describe())

# calculate correlations
correlation_matrix = merged_df.corr()