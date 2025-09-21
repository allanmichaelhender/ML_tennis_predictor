import pandas as pd

dataframe = pd.read_csv("ML_ready_data.csv", index_col=0)
print(dataframe.head())