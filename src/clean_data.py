from pathlib import Path
import pandas as pd

try:
    SCRIPT_DIR = Path(__file__).resolve().parent
except NameError:
    # In case of running in notebook / interactive session
    SCRIPT_DIR = Path.cwd()
RAW_DIR = SCRIPT_DIR.parent / "data" / "raw"
PROCESSED_DIR = SCRIPT_DIR.parent / "data" / "processed"


# -----------------------
# Heat Index
# -----------------------

# clean and sort data by zipcode and save to cleaned csv file

# define path to cleaned heat by zip file
raw_heat_data = RAW_DIR / "raw_heat_data.csv"
heat_by_zip = PROCESSED_DIR / "heat_by_zip.csv"

# open raw heat data
heat_df = pd.read_csv(raw_heat_data)

# clean data frame
sorted_heat_df = heat_df.sort_values(by='zcta20')

sorted_heat_df = sorted_heat_df.rename(columns={'zcta20': 'zip_code', 'hvi': 'Heat Index'})

# save cleaned data to csv
sorted_heat_df.to_csv(heat_by_zip, index=False)

print("Finished saving heat index by zip to CSV.")


# -----------------------
# Tree Data
# -----------------------

# define file paths to full tree data csv and cleaned tree count by zip csv
tree_data_full = RAW_DIR / "data/tree_data_full.csv"
tree_data_by_zip = PROCESSED_DIR / "data/tree_count_by_zip.csv"

# Load full tree data
tree_df = pd.read_csv(tree_data_full)

# Remove irregular entries
tree_df = tree_df[tree_df['zipcode'].between(int(10001), int(11697))]

# Aggregate tree count by zip
tree_count_by_zip = tree_df.groupby('zipcode', as_index=False).agg(
    tree_count=('zipcode', 'count'),
    boro=('boroname', 'first')  # keep the boro for this zip
)

# Sort by zip_code
tree_count_by_zip = tree_count_by_zip.sort_values('zipcode')

# Rename columns for CSV
tree_count_by_zip = tree_count_by_zip.rename(columns={'zipcode': 'zip_code'})

# Save cleaned CSV
tree_count_by_zip.to_csv(tree_data_by_zip, index=False)

print("Finished saving tree count by zip to CSV.")


# -----------------------
# Socioeconomic Data
# -----------------------

# Paths to CSV files
property_file = RAW_DIR / "property_value_sampled.csv"
socio_file = PROCESSED_DIR / "property_data_by_zip.csv"

# Read CSV into DataFrames
property_df = pd.read_csv(property_file)

# process property value data
property_data_by_zip = (
    property_df
    .groupby('zip', as_index=False)['fullval']
    .mean()
    .rename(columns={'zip': 'zip_code', 'fullval': 'Average Property Value'})
    .sort_values('zip_code')
)

# Save to CSV
property_data_by_zip.to_csv(socio_file, index=False)

print("Cleaned CSV saved with property data by zip.")


# -----------------------
# Merge Data
# -----------------------

# define paths to CSV files if processing needs to be restarted
heat_file = PROCESSED_DIR / "heat_by_zip.csv"
tree_file = PROCESSED_DIR / "tree_count_by_zip.csv"
property_file = PROCESSED_DIR / "data/property_data_by_zip.csv"

# define path for merged data csv
merged_data_file = PROCESSED_DIR / "merged_data_by_zip.csv"

# reload data frames if they were closed
sorted_heat_df = pd.read_csv(heat_file)
tree_count_by_zip = pd.read_csv(tree_file)
property_data_by_zip = pd.read_csv(property_file)

# Ensure zip codes are strings with leading zeros if necessary
sorted_heat_df['zip_code'] = sorted_heat_df['zip_code'].astype(str).str.zfill(5)
tree_count_by_zip['zip_code'] = tree_count_by_zip['zip_code'].astype(str).str.zfill(5)
property_data_by_zip['zip_code'] = property_data_by_zip['zip_code'].astype(str).str.zfill(5)

# Merge dataframes on zip_code
merged_df = (
    sorted_heat_df
    .merge(tree_count_by_zip, on='zip_code', how='left')
    .merge(property_data_by_zip, on='zip_code', how='left')
)

# clean up column names
merged_df = merged_df.rename(columns={'zip_code': 'Zip Code','Heat Index':'Heat Index', 'tree_count': 'Tree Count', 'boro': 'Borough', 'Average Property Value': 'Average Property Value'})

merged_df = merged_df.dropna(subset=['Heat Index', 'Tree Count', 'Average Property Value'])

merged_df['Average Property Value'] = merged_df['Average Property Value'].round(2)

# Save merged dataframe to CSV
merged_df.to_csv(merged_data_file, index=False)

print ("Finished saving merged data by zip CSV.")