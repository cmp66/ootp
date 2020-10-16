import os
import datetime
from parser import OOTPParser
from db import OOTPDbAccess


def importBasePlayer(filename, import_date, db_access):
    player_parser = OOTPParser()
   
    players = []
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='windows-1252') as handle:
            players = player_parser.parse_player_file(handle, import_date)
    
    for player in players:
        db_access.add_player_record(player)

def importPlayerBatting(filename, import_date, db_access):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='windows-1252') as handle:
            players = player_parser.parse_batting_file(handle, import_date)

    for player in players:
        db_access.add_player_batting_record(player)

def importPlayerFielding(filename, import_date, db_access):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='windows-1252') as handle:
            players = player_parser.parse_fielding_file(handle, import_date)

    for player in players:
        db_access.add_player_fielding_record(player)

def importPlayerPitching(filename, import_date, db_access):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='windows-1252') as handle:
            players = player_parser.parse_pitching_file(handle, import_date)

    for player in players:
        db_access.add_player_pitching_record(player)

db_access = OOTPDbAccess('mysql', 'localhost', 'ootp', 'ootp--11oo')
import_date = datetime.datetime.strptime('04/01/2056', '%m/%d/%Y')
importBasePlayer('./files/MLB-Player.html', import_date, db_access)
importPlayerBatting("./files/MLB-Batting.html", import_date, db_access)
importPlayerFielding("./files/MLB-Fielding.html", import_date, db_access)
importPlayerPitching("./files/MLB-Pitching.html", import_date, db_access)
importBasePlayer('./files/FS-Player.html', import_date, db_access)
importPlayerBatting("./files/FS-Batting.html", import_date, db_access)
importPlayerFielding("./files/FS-Fielding.html", import_date, db_access)
importPlayerPitching("./files/FS-Pitching.html", import_date, db_access)
importBasePlayer('./files/SS-Player.html', import_date, db_access)
importPlayerBatting("./files/SS-Batting.html", import_date, db_access)
importPlayerFielding("./files/SS-Fielding.html", import_date, db_access)
importPlayerPitching("./files/SS-Pitching.html", import_date, db_access)
importBasePlayer('./files/INT-Player.html', import_date, db_access)
importPlayerBatting("./files/INT-Batting.html", import_date, db_access)
importPlayerFielding("./files/INT-Fielding.html", import_date, db_access)
importPlayerPitching("./files/INT-Pitching.html", import_date, db_access)



