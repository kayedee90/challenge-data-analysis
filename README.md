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
- Emmanuel.ipynb -> tracks and visualises outliers among all features and various feature combinations
- Kenny.ipynb -> Visualises the distribution of properties by area surface, creates and interactive chart to sort this distribution by subtype and plots a heatmap of the correlation of all features to Price

## 📊 Visuals
All charts are generated using a mix of ##seaborn, Plotly and matplotlib.  
Visuals include:
- Maps of most and least expensive areas in Belgium
- Heatmaps of features corrolating to price
- Various visual breakdowns of outliers per feature
- Slides are located in the /presentation folder
  
## 🔍 Data Cleaning
- Starting dataset: 80.199rows, 37 columns
- Data cleaned: 964 duplicates removed, 36.003 rows removed for excessive missing values
- We infered and imputed missing values to be False in the following data: hasgarden, hasswimmingpool, hasterrace, haslift
- Removed datasets due to exessive missing values and low impact: bathroomcount, roomcount, hasattic,hasbasement, hasdressingroom, diningroomsurface, hasdiningroom, floorcount, streetfacadewidth, floodzonetype, heatingtype, hasheatpump, hasvoltaicpanels, hasthermicpanels, kitchensurface, kitchentype,haslivingroom, livingroomsurface, gardenorientation, hasairconditioning, hasarmoreddoor, hasvisiophone, hasoffice, hastoiletcount, hasfireplace, terracesurface, terraceorientation, gardensurface, parkingcountindoor, parkingcountoutdoor
- Remaining dataset: 44.196 rows, 14 columns.
- We decided to add 1 column: Price/m² for a new total of 15 columns

## 🔍 Key Insights
- Based on the parameter -- price per square meter ---
(medium averaged per postal code, without differentiating by property type)
we conclude:

1. Flanders are on average more expensive than Wallonia (and the whole of Belgium).
Between the cheapest properties the difference is about 30%.
Between the most expensive properties (except for Knokke and Leuven)
the difference is however smaller - about 10%.

2. The 10 most expensive municipalities in Flanders are either located at the coast
(Knokke, Ramskapelle, Oostduinkerke, Wilskerke) or associated with big cities:
Ghent (Ghent, Vinderhote), Antwerpen (Antwerpen, Deurne),
or the university town of Leuven (Leuven, Heverlee).

3. The top 10 least expensive municipalities in Flanders are usually associated with
remote rural areas: Nokere, Sint-Denijs, Alveringem, Bossuit, Aspelare,
Boezinge, Watou, Schalkhoeven, Leisele, Vliermaalroot.

4. Top 10 most expensive municipalities in Wallonia are associated mostly
with the area around Waterloo and Louvain-la-Neuve (Waterloo, Lasne-Chapelle-Saint-Lambert,
Ottignies, Mont-Saint-Guibert, Bornival),
city of Liege (Magnée),
Eupen-Aachen border with Germany (Hauset, Raeren),   
province of Luxembourg (Sélange, Habay-la-Vieille),
and some small villages in central Ardennes (Méan, Filot).  

5. In Wallonia top 10 cheapest municipalities are again associated with remote rural areas,
located mostly in the south-west part of Ardennes:
Hives, Forge-Philippe, Momignies, Bourlers, Framont, Lompret,
Wasmes, Corbion, Tourinne, Sohier, Wellin.   

6. The Ixelles and Ukkel communes of Brussels are in the top 10 of most expensive municipalities in Belgium,
but are still cheaper than the most expensive municipalities of Flanders (Knokke, Leuven, Antwerpen)
and Wallonia (Louvain-la-Neuve area).

7. The most expensive properties in Belgium are about 10 times more expensive than the cheapest properties.
  
8. The majority of properties lie around the 100m² to 200m² point, with the peak being at 100m²  

9. The top 5 features most correlated with price are:
   - **habitablesurface**: 0.58  
     Largest driver of price — bigger living spaces consistently lead to higher overall prices.
   - **price_per_m²**: 0.51  
     Strong indicator — though correlated with total price, the relationship is nuanced: high price per m² doesn't always mean the most expensive properties.
   - **bedroomcount**: 0.39  
     More bedrooms tend to push prices upward, especially up to about 5 bedrooms, after which the trend flattens.
   - **hasswimmingpool**: 0.27  
     Properties with pools are generally more expensive, reflecting luxury appeal — though some overlap with non-pool properties exists.
   - **building_condition**: 0.24  
     Better condition is linked to higher pricing, but with notable variability across conditions — not a dominant factor alone.

11. Extreme outliers have been identified using boxplots:   
•    Duplex, penthouse, groundfloor, triplex, kot have more than 5 bedrooms  
•    The surface of ground floor subtype is more than 10 thousand m2  
•    A lot of outliers have apartment values more than 2 million EUR  
•    More than 20 thousand EUR per m2 have been identified in apartments as outliers  
•    Houses have outliers in apartment block reaching 100 rooms  
•    The surface of farmhouses are reaching 50 thousand m2 and house subtype more than 40 thousand m2  
•    A lot of prices of houses are more than 2 million EUR  
•    A lot of houses are reaching more than 10 thousand per m2  


12. KDE plot to see the distribution of various non-numerical versus p/m2  
Plotted using KDE to have a global view on the dependence of p/m2 on the type of the property, location and score:  
•    The higher the EPC Score the higher the p/m2  
•    The Flat studio seems the least expensive per m2, while the penthouse subtype tends to be the most expensive on p/m2 for apartments  
•    Apartment block seems the least expensive, while Villa subtype ten ds to be the most expensive on p/m2 for house  
•    The newer the building conditions, the higher the p/m2  
•    Ranking of the regions based on the mode of the p/m2 distribution: 1. Brussels, 2. Flanders, 3. Wallonia!  
  
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
