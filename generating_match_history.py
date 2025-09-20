import pandas as pd
from data_cleaning import data
import numpy as np

    
    
for i in [0,1]:    
    index = i
    row_list = []

    #guess = np.random.randint(0, 2)
    guess = 1

    if guess == 1:

        initial_date = data.iloc[index, data.columns.get_loc('tourney_date')]
        six_months_before = initial_date - pd.DateOffset(months=6)
        is_in_range = (data['tourney_date'] >= six_months_before) & (data['tourney_date'] < initial_date)

        player1 = data.iloc[index, data.columns.get_loc('w_id')]
        player2 = data.iloc[index, data.columns.get_loc('l_id')]
        

        ranking_diff = (data.iloc[index, data.columns.get_loc('winner_rank_points')]-data.iloc[index, data.columns.get_loc('loser_rank_points')])/np.min([data.iloc[index, data.columns.get_loc('winner_rank_points')], data.iloc[index, data.columns.get_loc('loser_rank_points')]])


        
        
        #filter data to within 6 months
        data = data[is_in_range]
        #data = data.assign(p1_win = 1)


        # column_mapper = {
        #                  'w_win': 'p1_win', 
        #                  'w_id': "p1_id", 
        #                  'w_games_won': 'p1_games_won', 
        #                  "w_aces_per_serve": "p1_aces_per_serve", 
        #                  "w_bp_saved_per_faced":'p1_bp_saved_per_faced',
        #                  "w_serve_winloss": "p1_serve_winloss", 
        #                  "w_nonserve_winloss": 'p1_nonserve_winloss', 
        #                  "w_firstserve_win": "p1_firstserve_win",
        #                  'l_win': 'p2_win', 
        #                  'l_id': "p2_id", 
        #                  'l_games_won': 'p2_games_won', 
        #                  "l_aces_per_serve": "p2_aces_per_serve", 
        #                  "l_bp_saved_per_faced": 'p2_bp_saved_per_faced', 
        #                  "l_serve_winloss": "p2_serve_winloss", 
        #                  "l_nonserve_winloss": 'p2_nonserve_winloss', 
        #                  "l_firstserve_win": "p2_firstserve_win"
        #                  }
        
        # data.rename(columns=column_mapper, inplace=True)

        
        player1_w_filter = (data["w_id"] == player1)
        player1_l_filter = (data["l_id"] == player1)

        player1_w = data[player1_w_filter]
        player1_l = data[player1_l_filter]

        player1_match_winloss = len(player1_w)/(len(player1_w) + len(player1_l))

        player1_total_game_wins = player1_w["w_games_won"].sum() + player1_l["l_games_won"].sum()
        player1_total_game_losses = player1_w["l_games_won"].sum() + player1_l["w_games_won"].sum()

        player1_game_winloss = player1_total_game_wins / player1_total_game_losses

        print(data.head(20))
        print(data["winner_rank_points"].head())
        ranking_diff = (data.iloc[index, data.columns.get_loc('winner_rank_points')]-data.iloc[index, data.columns.get_loc('loser_rank_points')])/np.min([data.iloc[index, data.columns.get_loc('winner_rank_points')],data.iloc[index, data.columns.get_loc('loser_rank_points')]])

        player1_aces_per_serve_count = player1_w["w_aces_per_serve"].sum() + player1_l["l_aces_per_serve"].sum()
        total_matches = len(player1_w) + len(player1_l)

        player1_aces_per_serve = player1_aces_per_serve_count/total_matches

        player1_bp_saved_per_faced_count = player1_w["w_bp_saved_per_faced"].sum() + player1_l["l_bp_saved_per_faced"].sum()

        player1_bp_saved_per_faced = player1_bp_saved_per_faced_count/total_matches
        
        player1_bp_won_per_faced_count = player1_w["w_bp_won_per_faced"].sum() + player1_l["l_bp_won_per_faced"].sum()

        player1_bp_won_per_faced = player1_bp_won_per_faced_count/total_matches

        player1_serve_winloss_count = player1_w["w_serve_winloss"].sum() + player1_l["l_serve_winloss"].sum()

        player1_serve_winloss = player1_serve_winloss_count/total_matches
        
        player1_nonserve_winloss_count = player1_w["w_nonserve_winloss"].sum() + player1_l["l_nonserve_winloss"].sum()

        player1_nonserve_winloss = player1_nonserve_winloss_count/total_matches

        player1_firstserve_win_count = player1_w["w_firstserve_win"].sum() + player1_l["w_firstserve_win"].sum()

        player1_firstserve_win = player1_firstserve_win_count/total_matches


        
        player2_w_filter = (data["w_id"] == player2)
        player2_l_filter = (data["l_id"] == player2)

        player2_w = data[player2_w_filter]
        player2_l = data[player2_l_filter]

        player2_match_winloss = len(player2_w)/(len(player2_w) + len(player2_l))

        player2_total_game_wins = player2_w["w_games_won"].sum() + player2_l["l_games_won"].sum()
        player2_total_game_losses = player2_w["l_games_won"].sum() + player2_l["w_games_won"].sum()

        player2_game_winloss = player2_total_game_wins / player2_total_game_losses

        player2_aces_per_serve_count = player2_w["w_aces_per_serve"].sum() + player2_l["l_aces_per_serve"].sum()
        total_matches = len(player2_w) + len(player2_l)

        player2_aces_per_serve = player2_aces_per_serve_count/total_matches

        player2_bp_saved_per_faced_count = player2_w["w_bp_saved_per_faced"].sum() + player2_l["l_bp_saved_per_faced"].sum()

        player2_bp_saved_per_faced = player2_bp_saved_per_faced_count/total_matches

        player2_bp_won_per_faced_count = player2_w["w_bp_won_per_faced"].sum() + player2_l["l_bp_won_per_faced"].sum()

        player2_bp_won_per_faced = player2_bp_won_per_faced_count/total_matches

        player2_serve_winloss_count = player2_w["w_serve_winloss"].sum() + player2_l["l_serve_winloss"].sum()

        player2_serve_winloss = player2_serve_winloss_count/total_matches
        
        player2_nonserve_winloss_count = player2_w["w_nonserve_winloss"].sum() + player2_l["l_nonserve_winloss"].sum()

        player2_nonserve_winloss = player2_nonserve_winloss_count/total_matches

        player2_firstserve_win_count = player2_w["w_firstserve_win"].sum() + player2_l["w_firstserve_win"].sum()

        player2_firstserve_win = player2_firstserve_win_count/total_matches

        
        match_winloss_diff = (player1_match_winloss-player2_match_winloss)/np.min([player1_match_winloss, player2_match_winloss])
        game_winloss_diff = (player1_game_winloss-player2_game_winloss)/np.min([player1_match_winloss, player2_match_winloss])
        aces_per_serve_diff = (player1_aces_per_serve-player2_aces_per_serve)/np.min([player1_match_winloss, player2_match_winloss])
        bp_saved_per_faced_diff = (player1_bp_saved_per_faced-player2_bp_saved_per_faced)/np.min([player1_match_winloss, player2_match_winloss])
        bp_won_per_faced_diff = (player1_bp_won_per_faced-player2_bp_won_per_faced)/np.min([player1_match_winloss, player2_match_winloss])
        serve_winloss_diff = (player1_serve_winloss-player2_serve_winloss)/np.min([player1_match_winloss, player2_match_winloss])
        nonserve_winloss_diff = (player1_nonserve_winloss-player2_nonserve_winloss)/np.min([player1_match_winloss, player2_match_winloss])
        firstserve_win_diff = (player1_firstserve_win-player2_firstserve_win)/np.min([player1_match_winloss, player2_match_winloss])

        row_list.append({
            "player1_win": 1,
            "ranking_diff": ranking_diff,
            "match_winloss_diff": match_winloss_diff,
            "game_winloss_diff": game_winloss_diff,
            "aces_per_serve_diff": aces_per_serve_diff,
            "bp_saved_per_faced_diff": bp_saved_per_faced_diff,
            "bp_won_per_faced_diff": bp_won_per_faced_diff,
            "serve_winloss_diff": serve_winloss_diff,
            "nonserve_winloss_diff": nonserve_winloss_diff,
            "firstserve_win_diff": firstserve_win_diff})



ML_ready_data = pd.DataFrame(row_list)
print(ML_ready_data.head())







