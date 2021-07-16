import os
import sys
import datetime
from parser import OOTPParser
from db import OOTPDbAccess

def importOOTPFiles(dirname, import_date, db_access):
    player_parser = OOTPParser()
    for (dirpath, dirnames, filenames) in os.walk(dirname):
        fullnames = [os.path.join(dirpath, fname) for fname in filenames]
        for filename in fullnames:
            print (f'importing {filename}')
            if os.path.isfile(filename):
                with open(filename, "r", encoding="utf-8") as handle:
                    players = player_parser.parse_ootp_file(handle, import_date)

                    for player in players["player"]:
                        db_access.add_player_record(player)
                    for player in players["batting"]:
                        db_access.add_player_batting_record(player)
                    for player in players["fielding"]:
                        db_access.add_player_fielding_record(player)
                    for player in players["pitching"]:
                        db_access.add_player_pitching_record(player)


def importBasePlayer(dirname, import_date, db_access):
    player_parser = OOTPParser()

    for (dirpath, dirnames, filenames) in os.walk(dirname):
        fullnames = [os.path.join(dirpath, fname) for fname in filenames]
        for filename in fullnames:
            print (f'importing {filename}')
            if os.path.isfile(filename):
                with open(filename, "r", encoding="windows-1252") as handle:
                    players = player_parser.parse_player_file(handle, import_date)

                    for player in players:
                        db_access.add_player_record(player)


def importPlayerBatting(dirname, import_date, db_access):
    player_parser = OOTPParser()

    for (dirpath, _, filenames) in os.walk(dirname):
        fullnames = [os.path.join(dirpath, fname) for fname in filenames]
        for filename in fullnames:
            print (f'importing {filename}')
            if os.path.isfile(filename):
                with open(filename, "r", encoding="windows-1252") as handle:
                    players = player_parser.parse_batting_file(handle, import_date)

                    for player in players:
                        db_access.add_player_batting_record(player)


def importPlayerFielding(dirname, import_date, db_access):
    player_parser = OOTPParser()
    for (dirpath, _, filenames) in os.walk(dirname):
        fullnames = [os.path.join(dirpath, fname) for fname in filenames]
        for filename in fullnames:
            print (f'importing {filename}')
            if os.path.isfile(filename):
                with open(filename, "r", encoding="windows-1252") as handle:
                    players = player_parser.parse_fielding_file(handle, import_date)

                    for player in players:
                        db_access.add_player_fielding_record(player)


def importPlayerPitching(dirname, import_date, db_access):
    player_parser = OOTPParser()
    for (dirpath, _, filenames) in os.walk(dirname):
        fullnames = [os.path.join(dirpath, fname) for fname in filenames]
        for filename in fullnames:
            print (f'importing {filename}')
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


datestamp = sys.argv[1]
season = int(sys.argv[2])
save = sys.argv[3]
import_date = datetime.datetime.strptime(datestamp, "%m/%d/%Y")
import_datestring = date_time = import_date.strftime("%d-%b-%Y")

db_access = OOTPDbAccess(save)

importOOTPFiles(f'./files/{save}/{import_datestring}', import_date, db_access)

# importBasePlayer(f'./files/{import_datestring}/MLB/Players', import_date, db_access)
# importPlayerBatting(f'./files/{import_datestring}/MLB/Batting', import_date, db_access)
# importPlayerFielding(f'./files/{import_datestring}/MLB/Fielding', import_date, db_access)
# importPlayerPitching(f'./files/{import_datestring}/MLB/Pitching', import_date, db_access)
# importBasePlayer(f'./files/{import_datestring}/FS/Players', import_date, db_access)
# importPlayerBatting(f'./files/{import_datestring}/FS/Batting', import_date, db_access)
# importPlayerFielding(f'./files/{import_datestring}/FS/Fielding', import_date, db_access)
# importPlayerPitching(f'./files/{import_datestring}/FS/Pitching', import_date, db_access)
# importBasePlayer(f'./files/{import_datestring}/SS/Players', import_date, db_access)
# importPlayerBatting(f'./files/{import_datestring}/SS/Batting', import_date, db_access)
# importPlayerFielding(f'./files/{import_datestring}/SS/Fielding', import_date, db_access)
# importPlayerPitching(f'./files/{import_datestring}/SS/Pitching', import_date, db_access)
# importBasePlayer(f'./files/{import_datestring}/INT/Players', import_date, db_access)
# importPlayerBatting(f'./files/{import_datestring}/INT/Batting', import_date, db_access)
# importPlayerFielding(f'./files/{import_datestring}/INT/Fielding', import_date, db_access)
# importPlayerPitching(f'./files/{import_datestring}/INT/Pitching', import_date, db_access)
# importBasePlayer(f'./files/{import_datestring}/FA/Players', import_date, db_access)
# importPlayerBatting(f'./files/{import_datestring}/FA/Batting', import_date, db_access)
# importPlayerFielding(f'./files/{import_datestring}/FA/Fielding', import_date, db_access)
# importPlayerPitching(f'./files/{import_datestring}/FA/Pitching', import_date, db_access)
# importBasePlayer(f'./files/{import_datestring}/Draft/Players', import_date, db_access)
# importPlayerBatting(f'./files/{import_datestring}/Draft/Batting', import_date, db_access)
# importPlayerFielding(f'./files/{import_datestring}/Draft/Fielding', import_date, db_access)
# importPlayerPitching(f'./files/{import_datestring}/Draft/Pitching', import_date, db_access)

#importPlayerStats(f"./files/ABL-Stats-2048.html", season, db_access)
