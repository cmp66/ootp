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
import_date = datetime.datetime.strptime("08/07/2056", "%m/%d/%Y")
season = 2056
importBasePlayer("./files/07-Aug-2056/MLB-Player.html", import_date, db_access)
importPlayerBatting("./files/07-Aug-2056/MLB-Batting.html", import_date, db_access)
importPlayerFielding("./files/07-Aug-2056/MLB-Fielding.html", import_date, db_access)
importPlayerPitching("./files/07-Aug-2056/MLB-Pitching.html", import_date, db_access)
importBasePlayer("./files/07-Aug-2056/FS-Player.html", import_date, db_access)
importPlayerBatting("./files/07-Aug-2056/FS-Batting.html", import_date, db_access)
importPlayerFielding("./files/07-Aug-2056/FS-Fielding.html", import_date, db_access)
importPlayerPitching("./files/07-Aug-2056/FS-Pitching.html", import_date, db_access)
importBasePlayer("./files/07-Aug-2056/SS-Player.html", import_date, db_access)
importPlayerBatting("./files/07-Aug-2056/SS-Batting.html", import_date, db_access)
importPlayerFielding("./files/07-Aug-2056/SS-Fielding.html", import_date, db_access)
importPlayerPitching("./files/07-Aug-2056/SS-Pitching.html", import_date, db_access)
importBasePlayer("./files/07-Aug-2056/INT-Player.html", import_date, db_access)
importPlayerBatting("./files/07-Aug-2056/INT-Batting.html", import_date, db_access)
importPlayerFielding("./files/07-Aug-2056/INT-Fielding.html", import_date, db_access)
importPlayerPitching("./files/07-Aug-2056/INT-Pitching.html", import_date, db_access)
importPlayerStats("./files/07-Aug-2056/MLB-Stats-07-Aug-2056.html", season, db_access)
