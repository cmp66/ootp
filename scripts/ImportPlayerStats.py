import os
import sys
import datetime
from parser import OOTPParser
from db import OOTPDbAccess


def importPlayerStats(filename, season, db_access):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf-8") as handle:
            players = player_parser.parse_stats_file(handle, season)

            for player in players:
                db_access.add_player_stats_record(player)


season = int(sys.argv[1])
save = sys.argv[2]
file = sys.argv[3]

db_access = OOTPDbAccess(save)

importPlayerStats(file, season, db_access)
