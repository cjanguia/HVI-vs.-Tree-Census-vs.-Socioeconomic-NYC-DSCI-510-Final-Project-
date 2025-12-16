from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# define script directory
try:
    SCRIPT_DIR = Path(__file__).resolve().parent
except NameError:
    # In case of running in notebook / interactive session
    SCRIPT_DIR = Path.cwd()
PROCESSED_DIR = SCRIPT_DIR.parent / "data" / "processed"

# define path for merged data csv
merged_data_file = PROCESSED_DIR / "merged_data_by_zip.csv"

# reopen merged data dataframe
merged_df = pd.read_csv(merged_data_file)


# -----------------------
# Distribution of Average Property Value (Histogram)
# -----------------------
mean = merged_df['Average Property Value'].mean()
std = merged_df['Average Property Value'].std()

# Keep only points within 3 std devs
filtered_data = merged_df[(merged_df['Average Property Value'] > mean - 3*std) & (merged_df['Average Property Value'] < mean + 3*std)]

plt.figure()
plt.hist(filtered_data['Average Property Value'], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribution of Average Property Value')
plt.xlabel('Average Property Value (in millions)')
plt.ylabel('Number of Zip Codes')
plt.show(block=False)

# -----------------------
# Tree Count vs. Average Property Value (Scatter Plot)
# -----------------------
# focus data down to get a clearer scatter plot

filtered_data_2 = merged_df[(merged_df['Average Property Value'] > mean - 2*std) & (merged_df['Average Property Value'] < mean + 2*std)]

plt.figure()
plt.scatter(filtered_data_2['Average Property Value'], filtered_data_2['Tree Count'], color='green')
plt.title('Tree Count vs Average Property Value')
plt.ylabel('Tree Count')
plt.xlabel('Average Property Value')
plt.show(block=False)


# -----------------------
# Tree Count vs. Property Value (colored by Heat Index) (Multivariable Scatter Plot)
# -----------------------

# focus data down to get a clearer scatter plot
filtered_data = merged_df[(merged_df['Average Property Value'] > mean - 0.5*std) & (merged_df['Average Property Value'] < mean + 0.5*std)]

heat_colors = {1: 'blue', 2: 'green', 3: 'orange', 4: 'red', 5: 'purple'}

plt.figure(figsize=(8,6))

# Plot each Heat Index value separately to create discrete legend
for heat_index, color in heat_colors.items():
    subset = filtered_data[filtered_data['Heat Index'] == heat_index]
    plt.scatter(
        subset['Tree Count'],
        subset['Average Property Value'],
        color=color,
        label=f'{heat_index}',
        s=100,
        edgecolor='k'
    )

# Labels, title, legend
plt.xlabel('Tree Count')
plt.ylabel('Average Property Value ($)')
plt.title('Tree Count vs Property Value by Heat Index')
plt.legend(title='Heat Index')
plt.show(block=False)

# -----------------------
# Heatmap of Average Values by Borough (Heatmap via Seaborn)
# -----------------------

import seaborn as sns

borough_means = merged_df.groupby('Borough')[['Heat Index','Tree Count','Average Property Value']].mean()

# Create heatmap
plt.figure(figsize=(6,4))
sns.heatmap(borough_means, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Average Values by Borough')
plt.show(block=False)

# -----------------------
# Heat Index by Borough
# -----------------------
plt.figure(figsize=(8,6))
sns.boxplot(x='Borough', y='Heat Index', data=merged_df, palette='Set2')
plt.title('Distribution of Heat Index by Borough')
plt.ylabel('Heat Index')
plt.xlabel('Borough')
plt.show()