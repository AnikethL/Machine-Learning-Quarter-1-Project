import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

input_file = 'preprocessed.csv'
output_file = 'encoded.csv'

df = pd.read_csv(input_file)

encoder = OrdinalEncoder()


for column in df.columns:
    if df[column].dtype == 'object' or column=="Latitude" or column=="Longitude":  # Categorical (qualitative) data
        # fill missing values with the mode
        mode = df[column].mode()[0]
        df[column].fillna(mode, inplace=True)
        
    elif pd.api.types.is_numeric_dtype(df[column]):  #  numerical check
        if column=="Speed Limit":
            # calc the mean, ignoring 0s
            meanVal = df[column][df[column] != 0].mean()

            # replace 0s with the calculated mean
            df[column].replace(0, meanVal, inplace=True)
            df[column].fillna(meanVal, inplace=True)
        else:
            # fill missing values with the mean
            meanVal = df[column].mean()
            df[column].fillna(meanVal, inplace=True)
        
for column in df.columns:
    if column != "Vehicle Damage Extent" and not(pd.api.types.is_numeric_dtype(df[column])):
        print(df[column])
        df[column] = encoder.fit_transform(df[[column]])
        
# save df to csv
df.to_csv(output_file, index=False)