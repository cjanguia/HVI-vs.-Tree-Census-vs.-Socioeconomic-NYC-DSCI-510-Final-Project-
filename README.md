# DSCI 510 Final Project

## Shade NYC

### ---

### Project Description

Shade cover from trees has colloquially been said to cool down urban environments. As climate change continues to impact urban environments, keeping cities cool is incredibly important for health and economic purposes (Ettinger, 2024). This is a social justice issue, as people in lower-income communities often have less access to green spaces, meaning that they will experience “heat island effect” to a greater extent than those in higher-income regions. This project aims to analyze data from New York City Open Data to test if this theory applies to New York. In addition, we will investigate environmental injustices by analyzing socioeconomic status by zip code to determine if wealth disparity affects the tree cover.

This repository was developed as a final project for DSCI 510 and demonstrates applied data science skills, including data cleaning, integration, statistical analysis, and visualization.  
---

### Research Questions

* How does Heat Vulnerability Index (HVI) vary across NYC neighborhoods?  
* Is there a relationship between tree canopy coverage (from NYC Tree Census data) and HVI?  
* How do socioeconomic variables (e.g., wealth proxies) relate to both tree canopy and HVI?  
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

* Python files for data collecting, cleaning, analysis, statistical analysis, and visualizations.

project\_proposal.pdf

The original project proposal outlining the research questions, data sources, methodology, and expected outcomes for the DSCI 510 final project.

results/

* final\_report.pdf: Contains a final report of the process used in the creation of this project, as well as analysis and visualizations of the data. 

---

### Data Sources

The project relies on publicly available NYC datasets, including:

* Heat Vulnerability Index (HVI): Neighborhood-level heat vulnerability indicators.  
* NYC Tree Census: Street tree locations, ID number, tree circumference, etc..  
* Socioeconomic Data: Property value as a proxy for socioeconomic values

All raw datasets are stored in \`data/raw/\`, and cleaned and merged versions are saved in   
\`data/processed/\`.  
---

### Methods

* Data cleaning and preprocessing using \*\*pandas\*\*  
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

* requests  
* pandas  
* io  
* random  
* time  
* json  
* csv  
* pathlib  
* matplotlib.pyplot  
* seaborn

---

### Installation & Setup

1\. Clone the repository:  
git clone https://github.com/cjanguia/HVI-vs.-Tree-Census-vs.-Socioeconomic-NYC-DSCI-510-Final-Project-.git  
2\. Navigate to the project directory:  
	cd HVI-vs.-Tree-Census-vs.-Socioeconomic-NYC-DSCI-510-Final-Project-  
3\. Install required packages:  
pip install \-r requirements.txt  
---

### How to Run the Analysis

* Open the files located in the src/ directory in preferred python software  
* Run all cells sequentially to reproduce the analysis and visualizations

---

### Limitations

* The Heat Vulnerability Index has multiple factors that could all contribute to final conclusions made  
* The data collection method, including a randomizer, provides a new dataset every time the code is run, leading to results that cannot be replicated  
* The tree data count most likely underestimates the actual number of trees in New York City, which could make the data and final conclusions inaccurate