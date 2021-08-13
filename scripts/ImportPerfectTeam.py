import os
import sys
import datetime
import json
from parser import OOTPParser
from db import OOTPDbAccess

def import_perfect_team(filename, import_date, db_access):
    player_parser = OOTPParser()
    with open(filename, "r") as handle:
        pt_data = json.load(handle)

        for player in pt_data:
            player_record = player_parser.create_pt_player_record(player, import_date) 
            batting_record = player_parser.create_pt_batting_record(player, import_date)
            fielding_record = player_parser.create_pt_fielding_record(player, import_date)
            pitching_record = player_parser.create_pt_pitching_record(player, import_date)
            db_access.add_player_record(player_record)
            db_access.add_player_batting_record(batting_record)
            db_access.add_player_fielding_record(fielding_record)
            db_access.add_player_pitching_record(pitching_record)
         



datestamp = sys.argv[1]
save = "pt"
import_date = datetime.datetime.strptime(datestamp, "%m/%d/%Y")
import_datestring = date_time = import_date.strftime("%d-%b-%Y")

db_access = OOTPDbAccess(save)

import_perfect_team(f'./files/pt/{import_datestring}.json', import_date, db_access)