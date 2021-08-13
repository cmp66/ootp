from db import OOTPDbAccess, PlayerReports, PlayerStats, PlayerBatting
from parser import OOTPParser
from ratings import PlayerRatings

import sys
import os
import datetime


ratings_calc = PlayerRatings()


def _get_all_players(import_date):
    return db_access.get_all_players_by_date(import_date)

def _init_missing_player_report(player):
    player_report = PlayerReports()
    player_report.playerid = player.id 
    player_report.position = player.position
    player_report.team = player.team
    player_report.current = -100
    player_report.potential = -100

    return player_report

datestamp = sys.argv[1]
season = int(sys.argv[2])
import_date = datetime.datetime.strptime(datestamp, "%m/%d/%Y")
filter_limit = float(sys.argv[3])

save_name = sys.argv[4]
db_access = OOTPDbAccess(save_name)

missing_players = []
if len(sys.argv) < 6:
    players = _get_all_players(import_date)
else:
    player_file = sys.argv[5]
    players = []
    parser = OOTPParser()
    if os.path.isfile(player_file):
        with open(player_file, "r", encoding="utf-8") as handle:
            for export_player in parser.parse_exports_file(handle):
                db_player = (db_access.get_player_by_date(export_player["id"], import_date))

                if db_player is not None:
                    players.append(db_player)
                else:
                    missing_players.append(export_player['name'])




print(
    "NAME,ID,POS,TEAM,ORG,LEAGUE,LEVEL,AGE,CURRENT,POTENTIAL,"
    + "PITCH DIFF CURRENT,PITCH DIFF POT,BAT DIFF CURRENT,BAT DIF POT,"
    + "START OVR CUR,START OVR POT,RELIEF OVR CUR,RELIEF OVR POT,BAT OVR CUR,BAT OVR POT,"
    + "START BASE CUR,START INDIV CUR,START BASE POT, START INDIV POT,"
    + "RELIEF BASE CUR,RELIEF INDIV CUR,RELIEF BASE POT,RELIEF INDIV POT,"
    + "BAT HIT CUR,BAT FIELD CUR,BAT HIT POT,BAT FIELD POT,"
    + "START OVR LEFT,START BASE LEFT,START OVR RIGHT,START BASE RIGHT,"
    + "REL OVR LEFT,REL BASE LEFT,REL OVR RIGHT,REL BASE RIGHT,"
    + "BAT OVR LEFT,BAT BASE LEFT,BAT OVR RIGHT,BAT BASE RIGHT,"
    + "BABIP,BABIP POT,"
    + "C OVR,1B OVR,2B OVR,3B OVR,SS OVR,LF OVR,CF OVR,RF OVR,"
    + "BATTER WAR,PITCHER WAR,MLB YEARS,"
    + "WORK ETHIC,INTELLIGENCE,LEADER,GREED,LOYALTY,PERSONALITY"
)

for player in players:
    player_report = db_access.get_player_report(player.id, import_date)
    player_stats = db_access.get_player_stats(player.id, season)
    player_batting = db_access.get_batting_record(player.id, import_date)

    if player_report is None:
        player_report = _init_missing_player_report(player)

    if player_stats is None:
        battingwar = -100
        pitchingwar = -100
    else:
        battingwar = player_stats.battingwar
        pitchingwar = player_stats.pitchingwar
    


    if player_report.batteroverallpotential < filter_limit and player_report.starteroverallpotential < filter_limit and player_report.reliefoverallpotential < filter_limit:
        continue

    print(
        f"{player.name},{player.id},{player.position},{player.team},"
        + f"{player.org},{player.league},{player.level},{player.age},"
        + f"{player.overall},{player.potential},"
        + f"{player_report.pitcherratingsdiffcurrent},{player_report.pitcherratingsdiffpotential},"
        + f"{player_report.batterratingsdiffcurrent},{player_report.batterratingsdiffpotential},"
        + f"{player_report.starteroverallcurrent},{player_report.starteroverallpotential},"
        + f"{player_report.reliefoverallcurrent},{player_report.reliefoverallpotential},"
        + f"{player_report.batteroverallcurrent},{player_report.batteroverallpotential},"
        + f"{player_report.starterbasecurrent},{player_report.starterindivcurrent},"
        + f"{player_report.starterbasepotential},{player_report.starterindivpotential},"
        + f"{player_report.reliefbasecurrent},{player_report.reliefindivcurrent},"
        + f"{player_report.reliefbasepotential},{player_report.reliefindivpotential},"
        + f"{player_report.batteroverallbattingcurrent},{player_report.batteroverallfieldingcurrent},"
        + f"{player_report.batteroverallbattingpotential},{player_report.batteroverallfieldingpotential},"
        + f"{player_report.starteroverallvLeft},{player_report.starterbasevLeft},"
        + f"{player_report.starteroverallvRight},{player_report.starterbasevRight},"
        + f"{player_report.relieveroverallvLeft},{player_report.relieverbasevLeft},"
        + f"{player_report.relieveroverallvRight},{player_report.relieverbasevRight},"
        + f"{player_report.batteroverallvLeft},{player_report.batterbattingvLeft},"
        + f"{player_report.batteroverallvRight},{player_report.batterbattingvRight},"
        + f"{player_batting.babipoverall},{player_batting.babippotential},"
        + f"{player_report.catcheroverall},{player_report.firstbaseoverall},"
        + f"{player_report.secondbaseoverall},{player_report.thirdbaseoverall},"
        + f"{player_report.shortstopoverall},{player_report.leftfieldoverall},"
        + f"{player_report.centerfieldoverall},{player_report.leftfieldoverall},"
        + f"{battingwar},{pitchingwar},{player.majorleagueyears},"
        + f"{player.workethic},{player.intelligence},{player.leader},{player.greed}, {player.loyalty},{player.personality}"
    )

#print(f'Missing players {missing_players}')

# changed_batters_sorted = list(changed_batters.keys())
# changed_batters_sorted.sort(reverse=True)
# for grouping in changed_batters_sorted:
#     for player in changed_batters[grouping]:
#         print(
#             f'{player["name"]},{player["id"]},{player["position"]},{player["delta"]},{player["team"]}, {player["org"]},{player["level"]}'
#         )

# changed_pitchers_sorted = list(changed_pitchers.keys())
# changed_pitchers_sorted.sort(reverse=True)
# for grouping in changed_pitchers_sorted:
#     for player in changed_pitchers[grouping]:
#         print(
#             f'{player["name"]},{player["id"]},{player["position"]},{player["delta"]},{player["team"]}, {player["org"]},{player["level"]}'
#         )
