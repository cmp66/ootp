from db import OOTPDbAccess, PlayerStats, Player, PlayerPitching
from ratings import PlayerRatings
from scipy.stats import spearmanr
import datetime

db_access = OOTPDbAccess('ootp')

player_sets = [
    {
        "season": 2055,
        "import_date" : "04/01/2056"
    },
    {
        "season": 2056,
        "import_date" : "10/30/2056"
    }

]

ratings_calc = PlayerRatings()

players = {}
for i in range(201):
    players[i] = []

for target_position in ["SP", "RP", "CL"]:
    # for target_position in ['C', '1B', '2B', 'SS', '3B', 'LF', 'CF', 'RF']:
    ratings = []
    war = []
    wartotal = 0
    ratingstotal = 0

    for player_set in player_sets:
        import_date = datetime.datetime.strptime(player_set["import_date"], "%m/%d/%Y")        

        for stat_record in db_access.get_stats_by_season(player_set["season"]):
            player_id = stat_record.playerid
            player_record = db_access.get_player_by_date(player_id, import_date)

            if player_record.position != target_position:
                continue
            elif stat_record.battersfaced < 100:
                continue

            pitching_record = db_access.get_pitching_record(player_id, import_date, 1.0)

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

            if target_position == "SP" and war_rate > 1.5/774 and war_rate < 2.5/774:
                wartotal += 1
                ratingstotal += rating
            elif  target_position == "RP" and war_rate > -0.5/258 and war_rate < 0.5/258:
                wartotal += 1
                ratingstotal += rating
            elif  target_position == "CL" and  war_rate > -0.5/258 and war_rate < 0.5/258:
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
