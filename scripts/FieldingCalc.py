from db import OOTPDbAccess, PlayerStats, Player, PlayerFielding, PlayerBatting
from ratings import PlayerRatings
from scipy.stats import spearmanr
import datetime


#PBL
player_sets = [
    {
        "season": 2055,
        "import_date" : "04/01/2056"
    },
    {
        "season": 2056,
        "import_date" : "10/30/2056"
    },
    {
        "season": 2057,
        "import_date" : "11/05/2057"
    },
    {
        "season": 2058,
        "import_date" : "11/29/2058"
    },
    {
        "season": 2059,
        "import_date" : "12/28/2059"
    }
]

#Miami
#player_sets = [
#    {
#        "season": 2034,
#        "import_date" : "11/21/2034"
#    },
#]

#ABL
# player_sets = [
#     {
#         "season": 2047,
#         "import_date" : "11/24/2047"
#     },
#     {
#         "season": 2048,
#         "import_date" : "12/13/2048"
#     },
#     {
#         "season": 2049,
#         "import_date" : "11/22/2049"
#     }, 
# ]


db_access = OOTPDbAccess("ootp")
ratings_calc = PlayerRatings()

scale = 1.0
calc_type = "Overall"
players = {}
for i in range(201):
    players[i] = []


for target_position in ["C", "1B", "2B", "SS", "3B", "LF", "CF", "RF"]:
#for target_position in ['C']:
    ratings = []
    war = []
    wartotal = 0
    ratingstotal = 0

    for player_set in player_sets:
        import_date = datetime.datetime.strptime(player_set["import_date"], "%m/%d/%Y")
        for stat_record in db_access.get_stats_by_season(player_set["season"]):
            player_id = stat_record.playerid
            #print (f'Processsing stat record for id {player_id}')
            player_record = db_access.get_player_by_date(player_id, import_date)

            if player_record is None:
                #print (f'No player record with id:{player_id} for import data {player_set["import_date"]}')
                continue

            if player_record.position != target_position:
                continue
            elif stat_record.plateapp < 75:
                continue

            fielding_record = db_access.get_fielding_record(player_id, import_date)
            batting_record = db_access.get_batting_record(player_id, import_date)

            rating, brating, frating = ratings_calc.calculate_overall_batter_rating(
                fielding_record, batting_record, player_record.position, calc_type, scale 
            )

            #print (f'Got rating {rating} for id {player_id}')
            # brating = ratings_calc.calculate_batting_rating(batting_record)
            war_rate = stat_record.battingwar / stat_record.plateapp
            war.append(war_rate)
            ratings.append(rating)
            players[rating].append(player_record.name)

            if war_rate > 1.5/600 and war_rate < 2.5/600:
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
