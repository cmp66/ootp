import os
from parser import OOTPParser


def importBasePlayer(filename):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='windows-1252') as handle:
            player_parser.parse_player_file(handle)

def importPlayerBatting(filename):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='windows-1252') as handle:
            player_parser.parse_batting_file(handle)

def importPlayerFielding(filename):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='windows-1252') as handle:
            player_parser.parse_fielding_file(handle)

def importPlayerPitching(filename):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='windows-1252') as handle:
            player_parser.parse_pitching_file(handle)


#importBasePlayer('./files/MLB-Player.html')
#importPlayerBatting("./files/MLB-Batting.html")
#importPlayerFielding("./files/MLB-Fielding.html")
importPlayerPitching("./files/MLB-Pitching.html")
