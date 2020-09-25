import os
from parser import OOTPParser


def importBasePlayer(filename):
    player_parser = OOTPParser()
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='windows-1252') as handle:
            player_parser.parse_player_file(handle)
            

#importBasePlayer('./orig-files/MLB-Player.html')
importBasePlayer('./files/MLB-Player.html')
