import pandas as pd
import numpy as np
from data_functions import calculate_games_add_tiebreak

data_2023 = pd.read_csv("./Data/atp_matches_2023.csv")
data_2024 = pd.read_csv("./Data/atp_matches_2024.csv")

data = pd.concat([data_2024,data_2023]).sort_values('tourney_date').reset_index(drop=True)
data.drop(columns=["winner_seed", "winner_entry","loser_seed", "loser_entry", "minutes"], inplace=True)
data.dropna(inplace=True)
data.reset_index(drop=True)
data['tourney_date'] = pd.to_datetime(data['tourney_date'], format='%Y%m%d')
data[['w_games_won', 'l_games_won']] = data['score'].apply(lambda x: pd.Series(calculate_games_add_tiebreak(x)))

data["w_aces_per_serve"] = np.where(
    data["w_svpt"] == 0,  # Condition: if w_svpt is zero
    np.nan,                  # Value if True: set to 1
    data["w_ace"] / data["w_svpt"] # Value if False: perform the normal division
    )
data["l_aces_per_serve"] = np.where(
    data["l_svpt"] == 0,  # Condition: if l_svpt is zero
    np.nan,                  # Value if True: set to 1
    data["l_ace"] / data["l_svpt"] # Value if False: perform the normal division
    )

data["w_bp_saved_per_faced"] = np.where(
    data["w_bpFaced"] == 0,  # Condition: if w_svpt is zero
    np.nan,                  # Value if True: set to 1
    data["w_bpSaved"] / data["w_bpFaced"] # Value if False: perform the normal division
    )
data["l_bp_saved_per_faced"] = np.where(
    data["l_bpFaced"] == 0,  # Condition: if l_svpt is zero
    np.nan,                  # Value if True: set to 1
    data["l_bpSaved"] / data["l_bpFaced"] # Value if False: perform the normal division
    )

data["w_serve_winloss"] = ( data['w_1stWon'] + data['w_2ndWon'] ) / data['w_svpt']
data["l_serve_winloss"] = ( data['l_1stWon'] + data['l_2ndWon'] ) / data['l_svpt']

data["w_nonserve_winloss"] = 1 - data["l_serve_winloss"]
data["l_nonserve_winloss"] = 1 - data["w_serve_winloss"]

data["w_firstserve_win"] = data['w_1stWon']/data['w_svpt']
data["l_firstserve_win"] = data['l_1stWon']/data['w_svpt']

column_mapping = {"winner_id": "w_id", "loser_id": "l_id"}
data.rename(columns=column_mapping, inplace=True)

data = data[['tourney_date', 'w_id', 'w_games_won', "w_aces_per_serve", "w_bp_saved_per_faced", "w_serve_winloss", "w_nonserve_winloss", "w_firstserve_win",
             'l_id', 'l_games_won', "l_aces_per_serve", "l_bp_saved_per_faced", "l_serve_winloss", "l_nonserve_winloss", "l_firstserve_win"]]


print(data.head())
