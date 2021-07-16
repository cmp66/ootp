from db import OOTPDbAccess, Player, PlayerFielding, PlayerBatting
from ratings import PlayerRatings
import datetime
import sys


player_id = sys.argv[1]

datestamp = sys.argv[2]
reference_date = sys.argv[3]
scale_factor = sys.argv[4]
save = sys.argv[5]
pos = None #sys.argv[6] 

scale = float(scale_factor)


db_access = OOTPDbAccess(save)
ratings_calc = PlayerRatings()

import_date = datetime.datetime.strptime(datestamp, "%m/%d/%Y")
reference_date = datetime.datetime.strptime(reference_date, "%m/%d/%Y")

player = db_access.get_player_by_date(player_id, import_date)
fielding_record = db_access.get_fielding_record(player_id, import_date)
batting_record = db_access.get_batting_record(player_id, import_date)
pitching_record = db_access.get_pitching_record(player_id, import_date)

ref_batting_record = db_access.get_batting_record(player_id, reference_date)
ref_pitching_record = db_access.get_pitching_record(player_id, reference_date)

print (f"{str(batting_record.contactpotential)}")

print(f'Evaluationg {player.name}')
if pos is None:
    for target_position in ["C", "1B", "2B", "SS", "3B", "LF", "CF", "RF"]:
        rating, brating, frating = ratings_calc.calculate_overall_batter_rating(
            fielding_record, batting_record, target_position, False, scale
        )

        prating, pbrating, pfrating = ratings_calc.calculate_overall_batter_rating(
            fielding_record, batting_record, target_position, True, scale
        )

        print (f'Position: {target_position}  Current: {rating}  Potential" {prating}')

        difference_record = ratings_calc.get_batting_difference_record(batting_record, ref_batting_record)
        print(difference_record)
else:
    if pos in ["SP"]:
        rating, brating, indrating = ratings_calc.calculate_starter_pitcher_rating(
            pitching_record, pos, False, scale
        )

        prating, pbrating, pindrating = ratings_calc.calculate_starter_pitcher_rating(
            pitching_record, pos, True, scale
        )

        print (f'Position: {pos}  Current: {rating}  Potential" {prating}')
    elif pos in ["RP", "CL"]:
        rating, brating, indrating = ratings_calc.calculate_relief_pitcher_rating(
            pitching_record, pos, False, scale
        )

        prating, pbrating, pindrating = ratings_calc.calculate_relief_pitcher_rating(
            pitching_record, pos, True, scale
        )

        print (f'Position: {pos}  Current: {rating}  Potential" {prating}')
    else:
        rating, brating, frating = ratings_calc.calculate_overall_batter_rating(
            fielding_record, batting_record, pos, False, scale
        )

        prating, pbrating, pfrating = ratings_calc.calculate_overall_batter_rating(
            fielding_record, batting_record, pos, True, scale
        )

        print (f'Position: {pos}  Current: {rating}  Potential" {prating}')

    difference_record = ratings_calc.get_pitching_difference_record(batting_record, ref_batting_record)
    print(difference_record)
    