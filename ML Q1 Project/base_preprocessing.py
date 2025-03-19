import pandas as pd

df = pd.read_csv('cleaned.csv')

df.drop(columns=['Report Number', 'Local Case Number', "Location"], inplace=True)
total_rows = df.shape[0]
tooManyMissing = []
for column in df.columns:
    missingVals = df[column].isnull().sum()
    percentMissing = (missingVals / total_rows) * 100
    if percentMissing>=75:
        tooManyMissing.append(column)
df.drop(columns=tooManyMissing, inplace=True)

labels_to_remove = ["OTHER", "VEHICLE NOT AT SCENE", "UNKNOWN", "OTHER DISTRACTION"]

for column in df.columns:
    try:
        df[column] = df[column].str.upper()
    except:
        print("failure")
        df[column] = df[column].astype(str)
        
    df = df[~df[column].isin(labels_to_remove)]

    
df.to_csv("preprocessed.csv", index=False)
