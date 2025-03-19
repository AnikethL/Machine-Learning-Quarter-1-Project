import pandas as pd
import arff

input_file = 'Crash_Reporting_-_Drivers_Data.csv'
output_file = 'cleaned.csv'

df = pd.read_csv(input_file)

df = df.replace({'\n': '', '\r': '', "['\"]":''}, regex=True)

df.to_csv(output_file, index=False)