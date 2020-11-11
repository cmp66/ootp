from db import OOTPDbAccess, PlayerStats, Player, PlayerFielding, PlayerBatting
from ratings import PlayerRatings
from scipy.stats import spearmanr
import datetime

db_access = OOTPDbAccess()

season = 2056
import_date = datetime.datetime.strptime("10/30/2056", "%m/%d/%Y")

ratings_calc = PlayerRatings()

players = {}
for i in range(201):
    players[i] = []


for target_position in ["C", "1B", "2B", "SS", "3B", "LF", "CF", "RF"]:
    # for target_position in ['C']:
    ratings = []
    war = []
    wartotal = 0
    ratingstotal = 0

    for stat_record in db_access.get_stats_by_season(season):
        player_id = stat_record.playerid
        player_record = db_access.get_player_by_date(player_id, import_date)

        if player_record.position != target_position:
            continue
        elif stat_record.plateapp < 30:
            continue

        fielding_record = db_access.get_fielding_record(player_id, import_date)
        batting_record = db_access.get_batting_record(player_id, import_date)

        rating = ratings_calc.calculate_overall_batter_rating(
            fielding_record, batting_record, player_record.position, True
        )
        # brating = ratings_calc.calculate_batting_rating(batting_record)
        war_rate = stat_record.battingwar / stat_record.plateapp
        war.append(war_rate)
        ratings.append(rating)
        players[rating].append(player_record.name)

        if stat_record.battingwar > -0.2 and stat_record.battingwar < 0.2:
            wartotal += 1
            ratingstotal += rating

        # if rating > 0:
        #    print(f'Player: {player_record.name}  Position: {player_record.position}  Rating: {rating}')

    # corr, _ = pearsonr(war,ratings)
    # print(f'Position: {target_position} Pearsons correlation: {corr}')
    corr, _ = spearmanr(war, ratings)
    zero_war_rating = int((round(ratingstotal / wartotal)))
    print(
        f"Position: {target_position} Spearmans correlation: {corr}  Zero WAR Rating {zero_war_rating}"
    )

for key in sorted(players):
    if len(players[key]) == 0:
        continue
    print(f"{key} : {players[key]}")
