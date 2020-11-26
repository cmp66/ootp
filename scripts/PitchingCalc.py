from db import OOTPDbAccess, PlayerStats, Player, PlayerPitching
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


# for target_position in ['C', '1B', '2B', 'SS', '3B', 'LF', 'CF', 'RF']:
for target_position in ["SP", "RP", "CL"]:

    ratings = []
    war = []
    wartotal = 0
    ratingstotal = 0

    for stat_record in db_access.get_stats_by_season(season):
        player_id = stat_record.playerid
        player_record = db_access.get_player_by_date(player_id, import_date)

        if player_record.position != target_position:
            continue
        elif stat_record.battersfaced < 100:
            continue

        pitching_record = db_access.get_pitching_record(player_id, import_date)

        if pitching_record.numpitches < 3 and target_position == "SP":
            continue

        if target_position == "SP":
            rating, base, indiv = ratings_calc.calculate_starter_pitcher_rating(
                pitching_record, player_record.position, False
            )
        else:
            rating, base, indiv = ratings_calc.calculate_relief_pitcher_rating(
                pitching_record, player_record.position, False
            )

        war_rate = stat_record.pitchingwar / stat_record.battersfaced
        war.append(war_rate)
        ratings.append(rating)
        players[rating].append(player_record.name)

        if stat_record.pitchingwar > -0.5 and stat_record.pitchingwar < 0.5:
            wartotal += 1
            ratingstotal += rating

    corr, _ = spearmanr(war, ratings)
    if wartotal == 0:
        wartotal = 1
    zero_war_rating = int((round(ratingstotal / wartotal)))
    print(
        f"Position: {target_position} Spearmans correlation: {corr}  Zero WAR Rating {zero_war_rating}"
    )

# for key in sorted(players):
#     if len(players[key]) == 0:
#         continue
#     print(f"{key} : {players[key]}")
