from db import OOTPDbAccess, PlayerReports, PlayerStats, PlayerBatting
from parser import OOTPParser
from ratings import PlayerRatings
from parser import BABIP

import sys
import os
import datetime


ratings_calc = PlayerRatings()


def _get_all_player_batting_by_date(timestamp):
    return db_access.get_all_batting_records_by_date(timestamp)

def _get_all_timestamps():
    return db_access.get_all_timestamps()

save_name = sys.argv[1]
scale = int(sys.argv[2])
db_access = OOTPDbAccess(save_name)

for timestamp in _get_all_timestamps():
    players = _get_all_player_batting_by_date(timestamp)
    for player in players:

        if player.babipoverall is None or player.babipoverall == 0:
        
            player.babipoverall = (BABIP.calc_babip(player.contactrating*scale, player.powerrating*scale, player.krating*scale))/scale
            player.babippotential = (BABIP.calc_babip(player.contactpotential*scale, player.powerpotential*scale, player.kprotential*scale))/scale

            db_access.update_player_batting_record(player)
    


