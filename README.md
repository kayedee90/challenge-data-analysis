# 🏡 Challenge: Data Analysis

## 📖 Description  
Preliminary data analysis for ImmoEliza, a real estate company aiming to dominate the Belgian housing market. Our mission is to clean, analyze, and extract insights from a large dataset of property listings,laying the foundation for a price prediction model.

## 🛠 Requirements
Python 3.13.2

## 🚀 Installation
To run the code locally:  
git clone git@github.com:kayedee90/challenge-data-analysis.git
cd challenge-data-analysis


Dependencies include:
- pandas
- numpy
- matplotlib
- matplotlib.pyplot
- seaborn
- Plotly.io
- Plotly.express
- ipython.display

## 🛠️ Usage
Run the script:
- python cleaning.py -> Cleans the dataset stored in /data/Raw_data.csv -> stores the cleaned data in /data/Cleaned_data.csv
- Nadiya.py Shows a visual representation of the most and least expensive areas in belgium
- Notebook_EDA_Emmanuel.ipynb -> tracks and visualises outliers among all features and various feature combinations
- Kenny_jupiter.ipynb -> Visualises the distribution of properties by area surface, creates and interactive chart to sort this distribution by subtype and plots a heatmap of the corrolation of all features to Price

## 📊 Visuals
All charts are generated using a mix of ##seaborn, Plotly and matplotlib.  
Visuals include:
- Maps of most and least expensive areas in Belgium
- Heatmaps of features corrolating to price
- Various visual breakdowns of outliers per feature
  
## 🔍 Data Cleaning
- Starting dataset: 80.199rows, 37 columns
- Data cleaned: 964 duplicates removed, 36.003 rows removed for excessive missing values
- We infered and imputed missing values to be False in the following data: hasgarden, hasswimmingpool, hasterrace, haslift
- Removed datasets due to exessive missing values and low impact: bathroomcount, roomcount, hasattic,hasbasement, hasdressingroom, diningroomsurface, hasdiningroom, floorcount, streetfacadewidth, floodzonetype, heatingtype, hasheatpump, hasvoltaicpanels, hasthermicpanels, kitchensurface, kitchentype,haslivingroom, livingroomsurface, gardenorientation, hasairconditioning, hasarmoreddoor, hasvisiophone, hasoffice, hastoiletcount, hasfireplace, terracesurface, terraceorientation, gardensurface, parkingcountindoor, parkingcountoutdoor
- Remaining dataset: 44.196 rows, 14 columns.
- We decided to add 1 column: Price/m² for a new total of 15 columns

## 🔍 Key Insights
- 
-
- 
- 
- 
  
## 👥 Contributors
- [Kenny](https://github.com/kayedee90)
- [Emmanuel](https://github.com/Manu1175)
- [Nadiya](https://github.com/nadiya0509)

  
## 🕓 Timeline
- 20/06/2025 – Kickoff - Initial cleaning
- 23/06/2025 – Final cleaning
- 24/06/2025 – Analizing the cleaned dataset and initial visualisation
- 25/06/2025 - Finished visualising data and final polishing
- 26/06/2025 – Presentation day


## 📋 Technical Steps
- [x] Dataset loaded and cleaned (script: cleaning.py - Cleaned data: /data/cleaned_data.csv)
- [x] Exploratory Data Analysis (EDA) in notebook
- [x] Visual questions answered
- [x] README structured and polished
- [ ] Bonus insights added
