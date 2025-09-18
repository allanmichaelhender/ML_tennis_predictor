from h11 import Data
import pandas as pd
import numpy as np

data_2023 = pd.read_csv("./Data/atp_matches_2023.csv")
data_2024 = pd.read_csv("./Data/atp_matches_2024.csv")

data = pd.concat([data_2024,data_2023]).sort_values('tourney_date').reset_index(drop=True)
print(data.tail())