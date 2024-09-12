# Analyzing Player Performance Injury and Predicting Tommy John Surgery in Pitchers Using Machine Learning

## Project Overview
Machine learning(ML) is a field of artificial intelligence(AI) where computers use data and algorithms to learn patterns and make predictions or decisions without being explicitly programmed for each task. It enables systems to improve performance over time as they are exposed to more data.

This project analyzes Major League Baseball (MLB) data from 2008 to 2024, focusing on pitcher performance and injury data across the league, with an emphasis on tracking Tommy John surgeries. By exploring trends and patterns in player health and career longevity, the project aims to understand the impact of injuries, particularly Tommy John surgeries, on performance metrics over time.

Tommy John surgery is a procedure used to repair a torn ulnar collateral ligament (UCL) in the elbow, a common injury for baseball pitchers due to the repetitive stress of throwing. The surgery involves replacing the damaged ligament with a tendon from elsewhere in the body. Recovery can take 12 to 18 months, but many players are able to return to their previous performance levels, although the surgery and recovery period can impact career longevity and future injury risks.

The analysis leverages historical player statistics, in-season data, and injury records to develop a machine learning model using the random forest method. This model is designed to predict future performance and injury risks for MLB players, identifying key factors that influence pitcher health and effectiveness.

The random forest technique allows for robust classification of injury risk and prediction of performance trends by capturing complex interactions between various player metrics. This data-driven approach will help teams optimize player usage, minimize injury risks, and make more informed contract and roster decisions.
 
### What is the MLB?

Major League Baseball (MLB) is the professional baseball league in North America, made up of 30 teams divided into two leagues: the American League (AL) and the National League (NL). Each team plays a long season of 162 games from April to September, followed by playoffs in October to determine the champion.

In baseball, two teams take turns playing offense and defense. The offensive team tries to score runs by hitting a ball with a bat and running to a series of four bases, while the defensive team tries to prevent this by getting the offensive players out. The game is played over nine innings, and the team with the most runs at the end wins. Pitchers, who throw the ball to the batter, play a crucial role, as do hitters, who aim to score runs.

MLB is known for its rich history, with famous teams like the New York Yankees and Boston Red Sox, and iconic players such as Babe Ruth and Jackie Robinson. The league is highly competitive, and its players are some of the best in the world.
 Because of the vast number of players and injuries we decided to focus on pitchers and the Tommy John surgery. The goal the 
 surgery is to stabilize the elbow, reduce or eliminate pain
 and restore stability and range of motion. 

## Team Members
- Abigail Parsley
- Jack Yeager
- Jennifer McNew
- Josh Still
- Kayli Smith
- Lisa Ybarra
- Thierno Diallo
- Sylvia Turner

# List of Imported Libraries and Tools

1. **pandas** as pd
2. **sklearn.model_selection** (train_test_split, GridSearchCV, RandomizedSearchCV)
3. **sklearn.linear_model** (LogisticRegression)
4. **sklearn.ensemble** (RandomForestClassifier)
5. **sklearn.metrics** (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report)
6. **matplotlib.pyplot** as plt
7. **unidecode** (unidecode)
8. **splinter** (Browser)
9. **tensorflow** as tf
10. **numpy** as np
11. **sklearn.preprocessing** (OneHotEncoder, StandardScaler, MinMaxScaler, RobustScaler)
12. **sklearn.datasets** (load_iris)
13. **math** (pi)
14. **matplotlib.patches** as patches
15. **matplotlib.cm** (cm)
16. **matplotlib.colors** (Normalize)
17. **hvplot.pandas**
18. **bs4** (BeautifulSoup as soup)
19. **pathlib** (Path)
20. **seaborn** as sns

## Tools Used:
- **Microsoft Excel**
- **VS Code**
- **Jupyter Notebook**


## Project Steps

### 1. Objectives
The objective of this project is twofold:
    - first, to predict the number of days it takes for an MLB player to return to play after undergoing treatment or surgery, using features such as player age, recovery time, and injury type; 
    - second, to model the likelihood of Tommy John surgery occurrence/reoccurrence based on the number of pitches thrown. 

By developing machine learning models, this project aims to provide insights that can improve player recovery management and identify potential risk factors leading to Tommy John surgeries. These models will help teams make data-driven decisions regarding player health, workload, and future performance.

### 2. Data Sources
https://baseballsavant.mlb.com
https://docs.google.com/spreadsheets/d/1gQujXQQGOVNaiuwSN680Hq-FDVsCwvN-3AazykOBON0/edit?gid=0#gid=0
https://www.mlb.com/stats/pitching?sortState=asc
http://seanlahman.com/
https://www.fangraphs.com/roster-resource/injury-report?groupby=all
https://sabr.org/sabermetrics/data
https://www.retrosheet.org/



### 3. Data Transformation
- **Objective**: Clean and prepare the data for eep.
- **Tools**: Pandas for data manipulation and transformation.

#### Sample Transformation Code:
```python
will add


```
### 4. Exporting Clean CSVs
- **Objective:** Export the transformed data to CSV files for database import.
- **Tool:** Pandas.

### 5. Machine Learning
- **Objective:** Python.
- **Tool:** Random Forest.

#### Steps for ML
- will add

```

## Conclusion
This project will apply advanced machine learning techniques to the rich world of baseball statistics, offering new insights into player performance and injury risk. The findings from this project have the potential to significantly impact team management strategies, player development, and the broader field of sports analytics.

## Future Work
While this project laid a strong foundation for data management and analysis, there are several areas for future work:

1. *Explore the impact of external variables (e.g., weather, stadium conditions) on player performance and injury risk.
2. Create a dashboard or visualization tool to present predictions and insights to stakeholders such as coaches, team managers, or fantasy league participants.
3. How can performance and injury risk predictions be used to inform team strategy, roster management, and financial decisions?

By addressing these future work areas, we can further enhance the capabilities of our data infrastructure, enabling more comprehensive and impactful analysis.

## Learning Notes
This project reinforced: 

1. The importance of being proficient in data scraping.
2. The importance of combining data files. We spent most of our time getting the data files ready for use.

