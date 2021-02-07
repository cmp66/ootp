from db import OOTPDbAccess, PlayerStats, Player, PlayerFielding, PlayerBatting
from ratings import PlayerRatings
from scipy.stats import spearmanr
import datetime

db_access = OOTPDbAccess("ootp")

#season = 2055
#import_date = datetime.datetime.strptime("04/01/2056", "%m/%d/%Y")

ratings_calc = PlayerRatings()

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

players = {}
for i in range(201):
    players[i] = []


for target_position in ["C", "1B", "2B", "SS", "3B", "LF", "CF", "RF"]:
#for target_position in ['CF']:
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
            elif stat_record.plateapp < 125:
                continue

            fielding_record = db_access.get_fielding_record(player_id, import_date, 1.0)
            batting_record = db_access.get_batting_record(player_id, import_date, 1.0)

            rating, brating, frating = ratings_calc.calculate_overall_batter_rating(
                fielding_record, batting_record, player_record.position, False
            )
            # brating = ratings_calc.calculate_batting_rating(batting_record)
            war_rate = stat_record.battingwar / stat_record.plateapp
            war.append(war_rate)
            ratings.append(rating)
            players[rating].append(player_record.name)

            if war_rate > -0.5/600 and war_rate < 0.5/600:
            #if stat_record.battingwar > 1.5 and stat_record.battingwar < 2.5:
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

# for key in sorted(players):
#     if len(players[key]) == 0:
#         continue
#     print(f"{key} : {players[key]}")
