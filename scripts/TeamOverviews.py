from db import OOTPDbAccess, PlayerReports

import sys
import os
import datetime

db_access = OOTPDbAccess()


datestamp = sys.argv[1]
import_date = datetime.datetime.strptime(datestamp, "%m/%d/%Y")

pbl_teams = [
    "San Francisco",
    "Boston",
    "Texas",
    "Minnesota",
    "Seattle",
    "New York",
    "San Diego",
    "Detroit",
    "Cleveland",
    "Washington",
    "Atlanta",
    "Chicago",
    "Arizona",
    "Miami",
    "Tampa Bay",
    "Los Angeles",
    "Kansas City",
    "Toronto",
    "Philadelphia",
    "Cincinnati",
    "Oakland",
    "Houston",
    "St. Louis",
    "Montreal",
    "Carolina",
    "Colorado",
    "Pittsburgh",
    "Baltimore",
    "Milwaukee",
] 

def create_empty_dict():
    return {
        "pitchers": [],
        "relievers": [],
        "batters": []
    }

team_dict = { key: create_empty_dict() for key in pbl_teams}

mlb_players = db_access.get_all_mlb_players_by_date(import_date)

for player in mlb_players:
    report = db_access.get_player_report(player.id, import_date)
    mlb_team = player.team
    if player.position == "SP":
        team_dict[mlb_team]["pitchers"].append(report.starteroverallcurrent)
    elif player.position in ["1B", "2B", "3B", "SS", "LF", "CF", "RF", "C", "DH"]:
        team_dict[mlb_team]["batters"].append(report.batteroverallcurrent)
    elif player.position in ["RP", "CL"]:
        team_dict[mlb_team]["relievers"].append(report.reliefoverallcurrent)
    else:
        print (f"bad position {player.position}")

print (f'Team,SP,Batting,Relief,Index')
for team in team_dict:
    team_dict[team]["pitchers"].sort(reverse=True)
    team_dict[team]["batters"].sort(reverse=True)
    team_dict[team]["relievers"].sort(reverse=True)
    pitching = sum(team_dict[team]["pitchers"][:5]) / 5 
    batting = sum(team_dict[team]["batters"][:10]) / 10
    relieving = sum(team_dict[team]["relievers"][:4]) / 4

    index = round(0.4*pitching + 0.4*batting + 0.2*relieving)

    print (f'{team},{pitching},{batting},{relieving},{index}')

