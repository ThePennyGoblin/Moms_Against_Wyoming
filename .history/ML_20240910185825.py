# Import necessary packages
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import *


df = pd.read_csv("DATA/creditcard.csv")
df = df.drop('Time', axis=1)
print(df.shape)
df.head()

# Dataset sampling for faster computation
pos_idx = list(df[df['Class']==1].index)
neg_idx = list(df[df['Class']==0].sample(5000).index)

df = df.loc[pos_idx+neg_idx]
print(df.shape)
df['Class'].value_counts()