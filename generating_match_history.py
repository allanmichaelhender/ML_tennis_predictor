import pandas as pd
from data_cleaning import data
import numpy as np


row_list = []

guess = np.random.randint(0, 2)
guess = 1

if guess == 1:

    initial_date = data["tourney_date"][0]
    six_months_before = initial_date - pd.DateOffset(months=6)
    is_in_range = (data['tourney_date'] >= six_months_before) & (data['tourney_date'] <= initial_date)

    #filter data to within 6 months
    data = data[is_in_range]


    column_mapper = {
                     'w_win': 'p1_win', 
                     'w_id': "p1_id", 
                     'w_games_won': 'p1_games_won', 
                     "w_aces_per_serve": "p1_aces_per_serve", 
                     "w_bp_saved_per_faced":'p1_bp_saved_per_faced',
                     "w_serve_winloss": "p1_serve_winloss", 
                     "w_nonserve_winloss": 'p1_nonserve_winloss', 
                     "w_firstserve_win": "p1_firstserve_win",
                     'l_win': 'p2_win', 
                     'l_id': "p2_id", 
                     'l_games_won': 'p2_games_won', 
                     "l_aces_per_serve": "p2_aces_per_serve", 
                     "l_bp_saved_per_faced": 'p2_bp_saved_per_faced', 
                     "l_serve_winloss": "p2_serve_winloss", 
                     "l_nonserve_winloss": 'p2_nonserve_winloss', 
                     "l_firstserve_win": "p2_firstserve_win"
                     }
    
    data = data.assign(p1_win = 1)
    data.rename(columns=column_mapper, inplace=True)

    
    




print(data.head())