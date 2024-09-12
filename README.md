# Leveraging Machine Learning to Analyze Player Injury Return Dates and Predict Tommy John Surgery in Pitchers

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
- https://baseballsavant.mlb.com
- https://docs.google.com/spreadsheets/d/1gQujXQQGOVNaiuwSN680Hq-FDVsCwvN-3AazykOBON0/edit?gid=0#gid=0
- https://www.mlb.com/stats/pitching?sortState=asc
- http://seanlahman.com/
- https://www.fangraphs.com/roster-resource/injury-report?groupby=all
- https://sabr.org/sabermetrics/data
- https://www.retrosheet.org/



### 3. Data Transformation and Cleaning Process
- **Objective**: Clean and prepare the data for analysis, focusing on evaluating various injury risks (including Tommy John surgery) and examining recovery times across different types of injuries.
- **Tools Used**: 
  - **Pandas**: For data manipulation, merging, and transformation.
  - **NumPy**: For numerical operations and handling missing data.
  - **Scikit-learn**: For applying machine learning models.
  - **Matplotlib** & **Seaborn**: For visualizing trends and patterns in injury recovery and performance.

#### Steps Involved:
1. **Data Merging**: 
   - Multiple datasets were merged, including pitching statistics, player performance data, and injury logs.
   - The goal was to create a comprehensive dataset that included both performance metrics and injury occurrences across different types of injuries.

2. **Data Cleaning**:
   - Irrelevant columns were dropped to simplify the analysis.
   - Missing values were handled through mean imputation for numerical fields and careful adjustments for categorical data.
   - Player names were standardized by removing punctuation and ensuring consistency across datasets.

3. **Tommy John Surgery Prediction**:
   - The analysis focused on understanding the influence of pitch counts on the probability of Tommy John surgeries.
   - Historical data on surgeries and related performance statistics were explored to identify trends in injury risk linked to high pitch counts.

4. **Comprehensive Injury Analysis**:
   - Beyond pitching data, various statistical injury datasets were cleaned and analyzed to understand injury return and recovery times for different types of injuries (e.g., shoulder injuries, oblique strains, etc.).
   - Factors affecting recovery time and return to performance were investigated, incorporating a wide range of player metrics.

5. **Injury Return Time Analysis**:
   - Injury recovery time was analyzed using cleaned datasets, focusing on factors that could influence the length of recovery.
   - The analysis provided insights into how different injuries impact players’ ability to return to pre-injury performance levels.

### Outcome:
- **Tommy John Surgery Analysis**: The project identified clear patterns between high pitch counts and increased risk of Tommy John surgery. This analysis helped shed light on how workload management could play a role in injury prevention for pitchers.
  
- **Injury Recovery Insights**: By analyzing various types of injuries across multiple datasets, the project uncovered factors that influence injury recovery time. This included insights into player performance post-recovery and how certain injuries take longer for athletes to regain their previous level of play.

- **Predictive Insights**: The analysis aimed to predict injury probabilities and recovery times, helping teams make informed decisions about player management and medical intervention strategies.

- **Visualization**: Several visualizations were created to highlight trends in injury recovery, performance degradation, and the probability of surgeries like Tommy John.


## Synopsis of Cleaned CSVs

1. **Pitching Data**: This CSV contains cleaned pitching performance data for players across multiple seasons. The data has been preprocessed to remove missing values and ensure consistency in player names and team information.

2. **Tommy John Surgery List**: This CSV provides a comprehensive list of players who have undergone Tommy John surgery, along with details such as surgery date, team, level of play, and position. The data has been cleaned to standardize player names, remove unnecessary columns, and prepare it for further analysis of pitch count and injury risk.

3. **Merged Injury and Performance Data**: This CSV combines various injury datasets with player performance statistics to allow for the analysis of injury recovery times and the impact of injuries on player performance. It includes fields for injury type, recovery time, and other relevant performance metrics.

These cleaned CSVs serve as the foundation for the analysis of player injuries, recovery times, and predictions of injury probabilities.


## 5. Machine Learning
- **Objective**: Predicting Tommy John surgeries based on pitch count data.
- **Tool**: Python, Random Forest Classifier, GridSearchCV.

### Steps for ML

#### Modeling TJ Surgeries Based on Pitch Count:
- **Dataset**: Used historical data on player pitches and Tommy John (TJ) surgeries.
- **Target Variable**: Tommy John Surgery (Yes/No)
- **Model**: A Random Forest Classifier was employed to predict the probability of Tommy John surgery based on pitch count data.
- **Performance**: Initial model achieved an accuracy of 60.06% on the test set.

#### Model Optimization:
- **Fine-Tuning**: To improve model performance, hyperparameter tuning was performed using GridSearchCV. Specifically, we adjusted parameters such as the number of estimators (`n_estimators`).
- **GridSearchCV Details**: Explored 108 different hyperparameter combinations with a 5-fold cross-validation, leading to 540 fits in total.
- **Outcome**: After optimization, the model’s accuracy increased significantly to 70% on the test set.

This improvement demonstrates the effectiveness of optimizing hyperparameters for better predictive performance in determining injury probabilities.


## Conclusion

This project leveraged advanced machine learning techniques and in-depth data analysis to explore player performance and injury risk within MLB. By combining detailed statistical datasets, we were able to make meaningful insights into injury patterns, recovery times, and potential performance after injury.

Key findings from the project include the influence of pitch count on Tommy John surgery probability and the analysis of multiple statistical injury datasets, shedding light on factors affecting recovery and return times for injured players.

The machine learning model, enhanced through optimization and fine-tuning, improved its predictive power for Tommy John surgery cases, offering insights that could be crucial for team management and player development strategies. These findings have broad implications for how data-driven decisions can shape not only individual player careers but also organizational strategies in professional sports.

Overall, this project demonstrates the power of data analytics and machine learning in the field of sports, providing actionable insights that can potentially improve both performance outcomes and long-term player health.

## Future Work

This project has established a solid foundation for analyzing MLB player performance and injury risk using machine learning and statistical techniques. However, several areas for future exploration could further enhance the project's scope and impact:

1. **Incorporate External Factors**: Future work could involve integrating external variables such as weather conditions, stadium environments, and even travel schedules to understand their impact on player performance and injury risks. These factors may provide additional predictive power for models assessing injury probabilities.

2. **Advanced Visualization Tools**: Developing a real-time dashboard or visualization tool would allow stakeholders, including coaches, team managers, and even fantasy league participants, to interact with the predictions and insights generated by the models. This would facilitate decision-making by presenting key metrics and injury risk assessments in a user-friendly format.

3. **Strategy and Financial Decisions**: Extending the project to include more advanced decision-making models that focus on team strategy, roster management, and financial implications of player injuries could add substantial value. Predictive analytics could help guide roster changes, injury management strategies, and long-term investment decisions for teams.

By addressing these areas in future work, we can further elevate the project’s analytical depth and utility, ultimately providing a more comprehensive view of player health and performance management in professional sports.


## Learning Notes

Throughout the course of this project, we encountered several key lessons that reinforced important concepts in data science and machine learning:

1. **Data Preprocessing is Critical**: We learned firsthand that a significant portion of time in any data project is spent on cleaning and preparing data. The process of combining and harmonizing multiple data sources was a major part of the work, emphasizing the importance of thorough and organized preprocessing.

2. **Proficiency in Data Scraping**: The project reinforced the importance of being proficient in data scraping and collection. Accessing reliable and well-structured data is often a challenge, and understanding how to retrieve and structure raw data is a fundamental skill for any data science project.

3. **Data Integration Across Sources**: Merging datasets from various sources—each with their own structures and formats—was a key challenge. We learned that ensuring consistency in naming conventions, units, and data types is crucial for merging datasets without introducing errors.

4. **Iterative Model Improvement**: The machine learning aspect of this project taught us the importance of iterative model improvement. Fine-tuning models through hyperparameter optimization and feature selection proved critical for enhancing predictive performance and achieving more accurate results.

5. **Value of Cross-Disciplinary Insights**: Lastly, we recognized the value of blending domain knowledge—in this case, sports analytics and player health—with machine learning techniques. Understanding the context and implications of the data made it easier to interpret results and make actionable recommendations.


