from db import OOTPDbAccess, Player, PlayerFielding, PlayerBatting
from ratings import PlayerRatings
import datetime
import sys

db_access = OOTPDbAccess()
ratings_calc = PlayerRatings()

player_id = sys.argv[1]
datestamp = sys.argv[2]


import_date = datetime.datetime.strptime(datestamp, "%m/%d/%Y")

player = db_access.get_player_by_date(player_id, import_date)
fielding_record = db_access.get_fielding_record(player_id, import_date)
batting_record = db_access.get_batting_record(player_id, import_date)

print(f'Evaluationg {player.name}')
for target_position in ["C", "1B", "2B", "SS", "3B", "LF", "CF", "RF"]:
    rating, brating, frating = ratings_calc.calculate_overall_batter_rating(
            fielding_record, batting_record, target_position, False
        )

    prating, pbrating, pfrating = ratings_calc.calculate_overall_batter_rating(
            fielding_record, batting_record, target_position, True
        )

    print (f'Position: {target_position}  Current: {rating}  Potential" {prating}')

    