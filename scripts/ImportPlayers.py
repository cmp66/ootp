import os
import datetime
from parser import OOTPParser
from db import OOTPDbAccess


def importBasePlayer(filename, import_date, db_access):
    player_parser = OOTPParser()

    players = []
    if os.path.isfile(filename):
        with open(filename, "r", encoding="windows-1252") as handle:
            players = player_parser.parse_player_file(handle, import_date)

    for player in players:
        db_access.add_player_record(player)


def importPlayerBatting(filename, import_date, db_access):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, "r", encoding="windows-1252") as handle:
            players = player_parser.parse_batting_file(handle, import_date)

    for player in players:
        db_access.add_player_batting_record(player)


def importPlayerFielding(filename, import_date, db_access):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, "r", encoding="windows-1252") as handle:
            players = player_parser.parse_fielding_file(handle, import_date)

    for player in players:
        db_access.add_player_fielding_record(player)


def importPlayerPitching(filename, import_date, db_access):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, "r", encoding="windows-1252") as handle:
            players = player_parser.parse_pitching_file(handle, import_date)

    for player in players:
        db_access.add_player_pitching_record(player)


def importPlayerStats(filename, season, db_access):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, "r", encoding="windows-1252") as handle:
            players = player_parser.parse_stats_file(handle, season)

    for player in players:
        db_access.add_player_stats_record(player)


db_access = OOTPDbAccess()
import_date = datetime.datetime.strptime("10/30/2056", "%m/%d/%Y")
import_datestring = "30-Oct-2056"
season = 2056
# importBasePlayer(f'./files/{import_datestring}/MLB-Players.html', import_date, db_access)
# importPlayerBatting(f'./files/{import_datestring}/MLB-Batting.html', import_date, db_access)
# importPlayerFielding(f'./files/{import_datestring}/MLB-Fielding.html', import_date, db_access)
# importPlayerPitching(f'./files/{import_datestring}/MLB-Pitching.html', import_date, db_access)
# importBasePlayer(f'./files/{import_datestring}/FS-Players.html', import_date, db_access)
# importPlayerBatting(f'./files/{import_datestring}/FS-Batting.html', import_date, db_access)
# importPlayerFielding(f'./files/{import_datestring}/FS-Fielding.html', import_date, db_access)
# importPlayerPitching(f'./files/{import_datestring}/FS-Pitching.html', import_date, db_access)
# importBasePlayer(f'./files/{import_datestring}/SS-Players.html', import_date, db_access)
# importPlayerBatting(f'./files/{import_datestring}/SS-Batting.html', import_date, db_access)
# importPlayerFielding(f'./files/{import_datestring}/SS-Fielding.html', import_date, db_access)
# importPlayerPitching(f'./files/{import_datestring}/SS-Pitching.html', import_date, db_access)
# importBasePlayer(f'./files/{import_datestring}/INT-Players.html', import_date, db_access)
# importPlayerBatting(f'./files/{import_datestring}/INT-Batting.html', import_date, db_access)
# importPlayerFielding(f'./files/{import_datestring}/INT-Fielding.html', import_date, db_access)
# importPlayerPitching(f'./files/{import_datestring}/INT-Pitching.html', import_date, db_access)
importPlayerStats(f"./files/{import_datestring}/MLB-Stats.html", season, db_access)
