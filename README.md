# Moms_Against_Wyoming
#Project Title: Baseball Pitching Data and Tommy John Surgery Analysis

##Project Overview

This project analyzes Major League Baseball (MLB) pitching data from 2008 and tracks Tommy John surgeries among players. The goal of the project is to understand trends and patterns related to pitcher performance and health, with a focus on surgeries affecting career longevity.

##Key Objectives:

Merging pitching data with Tommy John surgery records.
Cleaning and processing raw datasets to extract meaningful insights.
Conducting data analysis to explore relationships between player performance metrics and surgeries.
Dataset Descriptions

1. Tommy John Surgery List
File: Tommy John Surgery List.csv
Description: A list of players who underwent Tommy John surgery, including player name, surgery date, team, position, and additional performance statistics.
Key Columns:
Player: Name of the player who underwent surgery.
Surgery Date: Date when the surgery was performed.
Team: The team the player was on when the surgery occurred.
Position: The player's position at the time of surgery.
Throws: Indicates which hand the player throws with.
2. Filtered Pitching Data (2008)
File: Pitch Data - 2008.csv
Description: A dataset containing detailed pitching metrics from the 2008 MLB season, covering various performance metrics for each pitcher.
Key Columns:
Player: Pitcher name.
Innings Pitched (IP): Number of innings the pitcher played.
Strikeouts (SO): Number of strikeouts by the pitcher.
Earned Run Average (ERA): The average number of earned runs allowed by the pitcher.

/project-root
│
├── data/                                # Folder containing all dataset files
│   ├── Tommy John Surgery List.csv       # Tommy John Surgery data
│   ├── Pitch Data - 2008.csv             # Pitching data for 2008
│
├── notebooks/                           # Jupyter notebooks for analysis
│   ├── data_cleaning_and_merging.ipynb   # Notebook for cleaning and merging data
│   ├── analysis.ipynb                    # Exploratory data analysis and visualizations
│
├── scripts/                             # Python scripts for data processing
│   ├── clean_and_merge.py                # Script for cleaning and merging datasets
│
├── README.md                            # Project documentation (this file)
├── requirements.txt                     # Required libraries and versions
└── LICENSE                              # License file for the project

/project-root
│
├── data/                                # Folder containing all dataset files
│   ├── Tommy John Surgery List.csv       # Tommy John Surgery data
│   ├── Pitch Data - 2008.csv             # Pitching data for 2008
│
├── notebooks/                           # Jupyter notebooks for analysis
│   ├── data_cleaning_and_merging.ipynb   # Notebook for cleaning and merging data
│   ├── analysis.ipynb                    # Exploratory data analysis and visualizations
│
├── scripts/                             # Python scripts for data processing
│   ├── clean_and_merge.py                # Script for cleaning and merging datasets
│
├── README.md                            # Project documentation (this file)
├── requirements.txt                     # Required libraries and versions
└── LICENSE                              # License file for the project

Setup and Installation

Prerequisites
Ensure that you have the following installed:

Python 3.x
pip (Python package installer)
Required Libraries
Install the required Python libraries by running:

Running the Project
Data Cleaning and Merging:
Use the script scripts/clean_and_merge.py to clean and merge the datasets. This script will:
Remove punctuation from player names.
Merge the Tommy John surgery data with the pitching data.
Run the script as follows:

Data Analysis:
After cleaning and merging the data, you can run the analysis in the Jupyter notebook located at notebooks/analysis.ipynb.
Open the notebook and run all cells to generate insights and visualizations from the merged data.

Project Workflow

Data Cleaning
Remove punctuation from player names to ensure consistency.
Standardize date formats and team abbreviations across datasets.
Handle missing or null values in key fields.
Data Merging
Merge the Tommy John Surgery List with the Pitch Data - 2008 based on player names.
Add a flag to indicate if the player has undergone surgery, allowing further analysis of their pre- and post-surgery performance.
Data Analysis
Explore trends in performance before and after Tommy John surgery.
Analyze common factors leading to surgery among pitchers (e.g., innings pitched, strikeouts).
Visualize data trends through graphs and charts.
File Descriptions

clean_and_merge.py: Python script to clean and merge the Tommy John surgery and pitching datasets.
analysis.ipynb: Jupyter notebook containing the analysis and visualizations.
requirements.txt: File containing the required Python libraries (e.g., pandas, numpy, matplotlib, seaborn).
LICENSE: License information for the project.
Results and Insights

Summarize the key findings from your data analysis here. For example:

Insight 1: A significant increase in ERA is observed in pitchers who underwent Tommy John surgery.
Insight 2: Pitchers who threw more than 100 innings in a season were more likely to require surgery within the next three years.
Future Work

Extend the analysis to include more recent years of pitching data.
Incorporate more advanced machine learning models to predict injury risk based on pitching performance.
License

This project is licensed under the MIT License. See the LICENSE file for details.