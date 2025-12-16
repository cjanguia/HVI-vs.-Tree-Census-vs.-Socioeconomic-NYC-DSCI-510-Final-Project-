import requests
from pathlib import Path
import pandas as pd
from io import StringIO
import csv
import time
from pathlib import Path
import random
import json

# -----------------------
# Initialize file paths
# -----------------------

try:
    SCRIPT_DIR = Path(__file__).resolve().parent
except NameError:
    # In case of running in notebook / interactive session
    SCRIPT_DIR = Path.cwd()
OUTPUT_DIR = SCRIPT_DIR.parent / "data" / "raw"


# -----------------------
# Heat Index
# -----------------------

# load data from heat API
heat_raw_data = requests.get("https://data.cityofnewyork.us/resource/4mhf-duep.csv")

# save full data to csv file

# define path to raw heat data csv
raw_heat_data = OUTPUT_DIR / "raw_heat_data.csv"

# convert raw text data to dataframe and save to csv
heat_df = pd.read_csv(StringIO(heat_raw_data.text))
heat_df.to_csv(raw_heat_data, index=False)

print ("Heat data CSV information written to file successfully.")


# -----------------------
# Tree Data
# -----------------------

tree_api_url = "https://data.cityofnewyork.us/resource/uvpi-gqnh.json"

LIMIT = 100_000  # safe batch size
offset = 0

COLUMNS = ["tree_id", "zipcode", "boroname"] # relevant columns to keep to avoid overwhelming memory/storage with unnecessary data

# Output file
tree_data_full = OUTPUT_DIR / "tree_data_full.csv"

with open(tree_data_full, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()

    while True:
        url = (
            f"{tree_api_url}"
            f"?$select={','.join(COLUMNS)}"
            f"&$limit={LIMIT}"
            f"&$offset={offset}"
        )

        response = requests.get(url, timeout=300)
        response.raise_for_status()
        data = response.json()

        if not data:
            print("Finished downloading tree data.")
            break

        for row in data:
            writer.writerow({col: row.get(col, "") for col in COLUMNS})

        offset += LIMIT
        print(f"Downloaded {offset:,} rows...")
        time.sleep(0.1)  # polite pause

print("Tree data CSV information written to file successfully.")

# -----------------------
# Socioeconomic Data
# -----------------------

# CONFIGURATION
API_URL = "https://data.cityofnewyork.us/resource/yjxr-fw8i.json"
LIMIT = 100_000           # rows per request
TOTAL_SAMPLE = 500_000    # reservoir size
KEY_COLUMNS = ["fullval", "zip"] # relevant columns to keep to avoid overwhelming memory/storage with unnecessary data

FINAL_FILE = OUTPUT_DIR / "property_value_sampled.csv"

save_every = 4_000_000    # write reservoir periodically
max_retries = 5 # max retries for API requests in case of errors

# INITIALIZE RESERVOIR
reservoir = []
seen = 0
offset = 0

where_clause = "fullval > 0 AND zip IS NOT NULL" # filter to only valid entries that will contribute to the data set

# STREAMING RESERVOIR SAMPLING TO AVOID MEMORY OVERLOAD
while True:
    url = f"{API_URL}?$limit={LIMIT}&$offset={offset}&$where={where_clause}"

    # Safe JSON fetch with retries
    for attempt in range(max_retries):
        try:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()
            break
        except (requests.RequestException, json.JSONDecodeError) as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                print("Max retries reached, skipping this batch.")
                data = []

    if not data:
        print("No more data returned from API.")
        break

    for row in data:
        seen += 1
        filtered_row = {k: row.get(k, "") for k in KEY_COLUMNS}

        # Reservoir sampling
        if len(reservoir) < TOTAL_SAMPLE:
            reservoir.append(filtered_row)
        else:
            j = random.randint(0, seen - 1)
            if j < TOTAL_SAMPLE:
                reservoir[j] = filtered_row

        # Progress print
        if seen % 100_000 == 0:
            print(f"Processed {seen:,} rows | Reservoir size: {len(reservoir):,}")

        # Periodic failsafe write
        if seen % save_every == 0:
            print(f"Writing temporary reservoir to CSV after {seen:,} rows...")
            with open(FINAL_FILE, "w", newline="", encoding="utf-8") as f_temp:
                writer_temp = csv.DictWriter(f_temp, fieldnames=KEY_COLUMNS)
                writer_temp.writeheader()
                writer_temp.writerows(reservoir)

    offset += LIMIT
    time.sleep(0.1)  # polite pause to avoid overwhelming the server

# WRITE FINAL CSV
with open(FINAL_FILE, "w", newline="", encoding="utf-8") as f_final:
    writer_final = csv.DictWriter(f_final, fieldnames=KEY_COLUMNS)
    writer_final.writeheader()
    writer_final.writerows(reservoir)

print(f"Property data samples written to file successfully.")