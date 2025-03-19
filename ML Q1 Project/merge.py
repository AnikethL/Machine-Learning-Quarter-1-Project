import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

folders = ["correlation", "GainRatio", "InfoGain", "nonweka", "CFS"]
files = ["train_ND", "validation_ND"]

# Models: RandomForest, Decision Trees, KNN, NaiveBayes
for folder in folders:
    print(folder)
    df1 = pd.read_csv(f"{folder}/{files[0]}.csv")
    df2 = pd.read_csv(f"{folder}/{files[1]}.csv")

    # print(df1.head())
    dfTrain = pd.concat([df1, df2])
    dfTrain.to_csv(folder+"/trainMerged_ND.csv", index=False)