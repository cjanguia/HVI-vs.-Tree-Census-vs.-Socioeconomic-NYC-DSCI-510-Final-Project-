# DSCI 510 Final Project

## Shade NYC

### ---

### Project Description

Shade cover from trees has colloquially been said to cool down urban environments. As climate change continues to impact urban environments, keeping cities cool is incredibly important for health and economic purposes (Ettinger, 2024). This is a social justice issue, as people in lower income communities often have less access to green spaces, meaning that they will experience “heat island effect” to a greater extent than those in higher income regions. This project aims to analyze data from New York City Open Data to test if this theory applies to New York. In addition, we will investigate environmental injustices by analyzing socioeconomic status by zip code to determine if wealth disparity affects the tree cover.

This repository was developed as a final project for DSCI 510 and demonstrates applied data science skills including data cleaning, integration, statistical analysis, and visualization.  
---

### Research Questions

* How does Health Vulnerability Index (HVI) vary across NYC neighborhoods?  
* Is there a relationship between tree canopy coverage (from NYC Tree Census data) and HVI?  
* How do socioeconomic variables (e.g., income, wealth proxies) relate to both tree canopy and HVI?  
* Are neighborhoods with higher socioeconomic status associated with lower health vulnerability and greater tree coverage?

---

### Repository Structure

├── README.md  
├── requirements.txt  
├── data/  
│ 	├── processed/  
│ 	└── raw/  
├── project\_proposal.pdf  
├── results/  
│ 	└── final\_report.pdf  
└── src/  
├── clean\_data.py  
├── get\_data.py  
├── run\_analysis.py  
└── visualize\_results.py

### ---

### Folder Descriptions

README.md

Provides an overview of the project, research questions, data sources, methodology, and instructions for setup and execution.

requirements.txt

Lists all Python dependencies required to run the project and reproduce the analysis.

data/

Contains all datasets used in the project.

* raw/: Original datasets exactly as downloaded from public sources. These files are not modified and serve as the data provenance.  
* processed/: Cleaned, transformed, and merged datasets created during preprocessing and used for analysis and visualization.

src/

Holds the core analysis code.

* Jupyter notebooks and/or Python scripts for data cleaning, exploratory data analysis (EDA), statistical analysis, and visualization.  
* Spatial analysis code integrating geographic data (e.g., HVI and neighborhood boundaries).

project\_proposal.pdf

The original project proposal outlining the research questions, data sources, methodology, and expected outcomes for the DSCI 510 final project.

results/

* final\_report.pdf: Contains a final report of the process used in the creation of this project, as well as analysis and visualizations of the data. 

---

### Data Sources

The project relies on publicly available NYC datasets, including:

* Health Vulnerability Index (HVI): Neighborhood-level health vulnerability indicators.  
* NYC Tree Census: Street tree locations, species, and health attributes.  
* Socioeconomic Data: Census-based variables such as income, poverty rates, or other wealth indicators.

All raw datasets are stored in \`data/raw/\`, with cleaned and merged versions saved in   
\`data/processed/\`.  
---

### Methods

* Data cleaning and preprocessing using \*\*pandas\*\* and \*\*geopandas\*\*  
* Spatial joins and aggregation at the neighborhood or borough level  
* Exploratory Data Analysis (EDA)  
* Statistical analysis (correlation between HVI, tree canopy, and socioeconomic variables)  
* Data visualization including:  
* Bar charts  
  * Scatter plots  
  * Geographic maps overlaying HVI and socioeconomic indicators

---

### Key Visualizations

* Comparison of average HVI by neighborhood  
* Tree density or canopy metrics by socioeconomic group  
* Choropleth maps showing spatial overlap between:  
  * HVI  
  * Wealth indicators  
  * Tree canopy distribution

---

### Technologies Used

* Python 3  
* pandas  
* geopandas  
* matplotlib / seaborn  
* Jupyter Notebook

---

### Installation & Setup

1\. Clone the repository:  
git clone https://github.com/cjanguia/HVI-vs.-Tree-Census-vs.-Socioeconomic-NYC-DSCI-510-Final-Project-.git  
2\. Navigate to the project directory:  
	cd HVI-vs.-Tree-Census-vs.-Socioeconomic-NYC-DSCI-510-Final-Project-  
3\. Install required packages:  
pip install \-r requirements.txt  
4\. Launch Jupyter Notebook  
---

### How to Run the Analysis

* Open the main Jupyter notebook located in the src/ directory  
* Run all cells sequentially to reproduce the analysis and visualizations  
* Alternative: Run project directly through .py files in terminal

---

### Limitations

* Tree Census data reflects street trees only, not all canopy coverage  
* Socioeconomic indicators are proxies and may not capture all dimensions of wealth  
* Health Vulnerability Index has multiple factors that could all contribute to final conclusions made