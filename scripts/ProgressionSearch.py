from db import OOTPDbAccess, PlayerReports
from ratings import PlayerRatings

import sys
import datetime


ratings_calc = PlayerRatings()


def _get_all_players(import_date):
    return db_access.get_all_players_by_date(import_date)


def _add_pitcher_change(increase, pitcher):
    if increase in changed_pitchers:
        changed_pitchers[increase].append(pitcher)
    else:
        changed_pitchers[increase] = []
        changed_pitchers[increase].append(pitcher)


def _add_batter_change(increase, batter):
    if increase in changed_batters:
        changed_batters[increase].append(batter)
    else:
        changed_batters[increase] = []
        changed_batters[increase].append(batter)


def _get_pitcher_diff_actual(id, report_time, reference_time, scale_factor):
    report_record = db_access.get_pitching_record(id, report_time)
    reference_record = db_access.get_pitching_record(id, reference_time)

    if reference_record is None:
        return 0

    total_change = (
        (report_record.stuffpotential - reference_record.stuffpotential)
        + (report_record.controlpotential - reference_record.controlpotential)
        + (report_record.movementpotential - reference_record.movementpotential)
    )

    return total_change


def _get_pitcher_diff_potential(id, report_time, reference_time, scale_factor):
    report_record = db_access.get_pitching_record(id, report_time)
    reference_record = db_access.get_pitching_record(id, reference_time)

    if reference_record is None:
        return 0

    total_change = (
        (report_record.stuffrating - reference_record.stuffrating)
        + (report_record.controlrating - reference_record.controlrating)
        + (report_record.movementrating - reference_record.movementrating)
    )

    return total_change


def _get_batter_diff_actual(id, report_time, reference_time, scale_factor):
    report_record = db_access.get_batting_record(id, report_time)
    reference_record = db_access.get_batting_record(id, reference_time)

    if reference_record is None:
        return 0

    total_change = (
        (report_record.contactrating - reference_record.contactrating)
        + (report_record.gaprating - reference_record.gaprating)
        + (report_record.powerrating - reference_record.powerrating)
        + (report_record.eyerating - reference_record.eyerating)
        + (report_record.krating - reference_record.krating)
    )

    return total_change


def _get_batter_diff_potential(id, report_time, reference_time, scale_factor):
    report_record = db_access.get_batting_record(id, report_time)
    reference_record = db_access.get_batting_record(id, reference_time)

    if reference_record is None:
        return 0

    total_change = (
        (report_record.contactpotential - reference_record.contactpotential)
        + (report_record.gappotential - reference_record.gappotential)
        + (report_record.powerpotential - reference_record.powerpotential)
        + (report_record.eyeprotential - reference_record.eyeprotential)
        + (report_record.kprotential - reference_record.kprotential)
    )

    return total_change


def _init_player_report(playerid, timestamp):
    player_report = PlayerReports()
    player_report.playerid = playerid
    player_report.timestamp = timestamp

    player_report.position = ""
    player_report.team = ""
    player_report.current = 0
    player_report.potential = 0
    player_report.pitcherratingsdiffcurrent = 0
    player_report.pitcherratingsdiffpotential = 0
    player_report.batterratingsdiffcurrent = 0
    player_report.batterratingsdiffpotential = 0
    player_report.starteroverallpotential = 0
    player_report.starterbasepotential = 0
    player_report.starterindivpotential = 0
    player_report.starteroverallcurrent = 0
    player_report.starterbasecurent = 0
    player_report.starterindivrcurrent = 0
    player_report.reliefoverallpotential = 0
    player_report.reliefbasepotential = 0
    player_report.reliefindivpotential = 0
    player_report.reliefoverallcurrent = 0
    player_report.reliefbasecurrent = 0
    player_report.reliefindivcurrent = 0
    player_report.batteroverallpotential = 0
    player_report.batteroverallbattingpotential = 0
    player_report.batteroverallfieldingpotential = 0
    player_report.batteroverallcurrent = 0
    player_report.batteroverallbattingcurrent = 0
    player_report.batteroverallfieldingcurrent = 0

    return player_report
save = sys.argv[3]
import_string = sys.argv[1]
reference_string = sys.argv[2]
scale = sys.argv[4]
db_access = OOTPDbAccess(save)

if scale is None:
    scale_factor = 1.0
else:
    scale_factor = float(scale)

import_date = datetime.datetime.strptime(import_string, "%m/%d/%Y")
reference_date = datetime.datetime.strptime(reference_string, "%m/%d/%Y")
players = _get_all_players(import_date)

changed_batters = {}
changed_pitchers = {}

minval = 99

print(
    "ID,NAME,POS,TEAM,ORG,LEAGUE,LEVEL,AGE,CURRENT,POTENTIAL,"
    + "PITCH DIFF CURRENT,PITCH DIFF POT,BAT DIFF CURRENT,BAT DIF POT,"
    + "START OVR CUR,START OVR POT,RELIEF OVR CUR,RELIEF OVR POT,BAT OVR CUR,BAT OVR POT,"
    + "START BASE CUR,START INDIV CUR,START BASE POT, START INDIV POT,"
    + "RELIEF BASE CUR,RELIEF INDIV CUR,RELIEF BASE POT,RELIEF INDIV POT,"
    + "BAT HIT CUR,BAT FIELD CUR,BAT HIT POT,BAT FIELD POT"
)

for player in players:
    print (f'evaluating {player.name}  {player.id}')
    player_report = _init_player_report(player.id, import_date)
    player_report.position = player.position
    player_report.team = player.team

    player_report.current = player.overall
    player_report.potential = player.potential

    if player.position in ["SP", "RP", "CL"]:
        pitcher_ratings = db_access.get_pitching_record(player.id, import_date)
        player_report.pitcherratingsdiffcurrent = _get_pitcher_diff_actual(
            player.id, import_date, reference_date, scale_factor
        )
        player_report.pitcherratingsdiffpotential = _get_pitcher_diff_potential(
            player.id, import_date, reference_date, scale_factor
        )
        (
            player_report.starteroverallpotential,
            player_report.starterbasepotential,
            player_report.starterindivpotential,
        ) = ratings_calc.calculate_starter_pitcher_rating(
            pitcher_ratings, player.position, True, scale_factor
        )
        (
            player_report.starteroverallcurrent,
            player_report.starterbasecurrent,
            player_report.starterindivcurrent,
        ) = ratings_calc.calculate_starter_pitcher_rating(
            pitcher_ratings, player.position, False, scale_factor
        )
        (
            player_report.reliefoverallpotential,
            player_report.reliefbasepotential,
            player_report.reliefindivpotential,
        ) = ratings_calc.calculate_relief_pitcher_rating(
            pitcher_ratings, player.position, True, scale_factor
        )
        (
            player_report.reliefoverallcurrent,
            player_report.reliefbasecurrent,
            player_report.reliefindivcurrent,
        ) = ratings_calc.calculate_relief_pitcher_rating(
            pitcher_ratings, player.position, False, scale_factor
        )
    else:
        batter_ratings = db_access.get_batting_record(player.id, import_date)
        fielding_ratings = db_access.get_fielding_record(player.id, import_date)
        player_report.batterratingsdiffcurrent = _get_batter_diff_actual(
            player.id, import_date, reference_date,  scale_factor
        )
        player_report.batterratingsdiffpotential = _get_batter_diff_potential(
            player.id, import_date, reference_date,  scale_factor
        )
        (
            player_report.batteroverallpotential,
            player_report.batteroverallbattingpotential,
            player_report.batteroverallfieldingpotential,
        ) = ratings_calc.calculate_overall_batter_rating(
            fielding_ratings, batter_ratings, player.position, True, scale_factor
        )
        (
            player_report.batteroverallcurrent,
            player_report.batteroverallbattingcurrent,
            player_report.batteroverallfieldingcurrent,
        ) = ratings_calc.calculate_overall_batter_rating(
            fielding_ratings, batter_ratings, player.position, False, scale_factor
        )

    db_access.add_player_report_record(player_report)

    # print(
    #     f"{player.id},{player.name},{player.position},{player.team},"
    #     + f"{player.org},{player.league},{player.level},{player.age},"
    #     + f"{player.overall},{player.potential},"
    #     + f"{player_report.pitcherratingsdiffcurrent},{player_report.pitcherratingsdiffpotential},"
    #     + f"{player_report.batterratingsdiffcurrent},{player_report.batterratingsdiffpotential},"
    #     + f"{player_report.starteroverallcurrent},{player_report.starteroverallpotential},"
    #     + f"{player_report.reliefoverallcurrent},{player_report.reliefoverallpotential},"
    #     + f"{player_report.batteroverallcurrent},{player_report.batteroverallpotential},"
    #     + f"{player_report.starterbasecurrent},{player_report.starterindivcurrent},"
    #     + f"{player_report.starterbasepotential},{player_report.starterindivpotential},"
    #     + f"{player_report.reliefbasecurrent},{player_report.reliefindivcurrent},"
    #     + f"{player_report.reliefbasepotential},{player_report.reliefindivpotential},"
    #     + f"{player_report.batteroverallbattingcurrent},{player_report.batteroverallfieldingcurrent},"
    #     + f"{player_report.batteroverallbattingpotential},{player_report.batteroverallfieldingpotential}"
    # )


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
