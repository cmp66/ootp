from db import OOTPDbAccess
import sys
import datetime

db_access = OOTPDbAccess()


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


def _get_pitcher_diff_actual(id, report_time, reference_time):
    report_record = db_access.get_pitching_record(id, report_time)
    reference_record = db_access.get_pitching_record(id, reference_time)

    total_change = (
        (report_record.stuffpotential - reference_record.stuffpotential)
        + (report_record.controlpotential - reference_record.controlpotential)
        + (report_record.movementpotential - reference_record.movementpotential)
    )

    return total_change


def _get_pitcher_diff_potential(id, report_time, reference_time):
    report_record = db_access.get_pitching_record(id, report_time)
    reference_record = db_access.get_pitching_record(id, reference_time)

    total_change = (
        (report_record.stuffrating - reference_record.stuffrating)
        + (report_record.controlrating - reference_record.controlrating)
        + (report_record.movementrating - reference_record.movementrating)
    )

    return total_change


def _get_batter_diff_actual(id, report_time, reference_time):
    report_record = db_access.get_batting_record(id, report_time)
    reference_record = db_access.get_batting_record(id, reference_time)

    total_change = (
        (report_record.contactrating - reference_record.contactrating)
        + (report_record.gaprating - reference_record.gaprating)
        + (report_record.powerrating - reference_record.powerrating)
        + (report_record.eyerating - reference_record.eyerating)
        + (report_record.krating - reference_record.krating)
    )

    return total_change


def _get_batter_diff_potential(id, report_time, reference_time):
    report_record = db_access.get_batting_record(id, report_time)
    reference_record = db_access.get_batting_record(id, reference_time)

    total_change = (
        (report_record.contactpotential - reference_record.contactpotential)
        + (report_record.gappotential - reference_record.gappotential)
        + (report_record.powerpotential - reference_record.powerpotential)
        + (report_record.eyeprotential - reference_record.eyeprotential)
        + (report_record.kprotential - reference_record.kprotential)
    )

    return total_change


import_date = datetime.datetime.strptime("08/07/2056", "%m/%d/%Y")
reference_date = datetime.datetime.strptime("04/01/2056", "%m/%d/%Y")
progression_type = sys.argv[1]
players = _get_all_players(import_date)

changed_batters = {}
changed_pitchers = {}

for player in players:
    if db_access.get_player_by_date(player.id, reference_date) is not None:
        if player.position in ["SP", "RP", "CL"]:
            pitcher_diff = (
                _get_pitcher_diff_actual(player.id, import_date, reference_date)
                if progression_type == "Actual"
                else _get_pitcher_diff_potential(player.id, import_date, reference_date)
            )

            if pitcher_diff > 0:
                pitcher_change = {
                    "id": player.id,
                    "position": player.position,
                    "name": player.name,
                    "delta": pitcher_diff,
                    "team": player.team,
                    "org": player.org,
                    "level": player.level,
                }
                _add_pitcher_change(pitcher_diff, pitcher_change)
        else:
            batter_diff = (
                _get_batter_diff_actual(player.id, import_date, reference_date)
                if progression_type == "Actual"
                else _get_batter_diff_potential(player.id, import_date, reference_date)
            )

            if batter_diff > 0:
                batter_change = {
                    "id": player.id,
                    "position": player.position,
                    "name": player.name,
                    "delta": batter_diff,
                    "team": player.team,
                    "org": player.org,
                    "level": player.level,
                }
                _add_batter_change(batter_diff, batter_change)

changed_batters_sorted = list(changed_batters.keys())
changed_batters_sorted.sort(reverse=True)
for grouping in changed_batters_sorted:
    for player in changed_batters[grouping]:
        print(
            f'{player["name"]},{player["id"]},{player["position"]},{player["delta"]},{player["team"]}, {player["org"]},{player["level"]}'
        )

changed_pitchers_sorted = list(changed_pitchers.keys())
changed_pitchers_sorted.sort(reverse=True)
for grouping in changed_pitchers_sorted:
    for player in changed_pitchers[grouping]:
        print(
            f'{player["name"]},{player["id"]},{player["position"]},{player["delta"]},{player["team"]}, {player["org"]},{player["level"]}'
        )
