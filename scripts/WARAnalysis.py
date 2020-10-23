from db import OOTPDbAccess, PlayerStats, Player

db_access = OOTPDbAccess()

season = 2055
total_pitching_war = 0
total_batting_war = 0
num_players = 0
num_drafted, drafted_war = (0, 0)
num_discovery, discovery_war = (0, 0)
count_by_round = [0] * 32
war_by_round = [0] * 32
num_fa, fa_war = (0, 0)

drafted_war_list_by_round = {}
for round in range(32):
    drafted_war_list_by_round[round] = []

drafted_war_list_by_year = {}
for year in range(32):
    drafted_war_list_by_year[2056 - year] = []

discovery_war_list = {}
for year in range(32):
    discovery_war_list[2056 - year] = []


for stat_record in db_access.get_stats_by_season(season):
    batting_war = stat_record.battingwar
    pitching_war = stat_record.pitchingwar
    player_record = db_access.get_player_by_id(stat_record.playerid)

    num_players += 1

    if player_record.position in ["SP", "RP"]:
        total_pitching_war += pitching_war
        player_war = pitching_war
    else:
        total_batting_war += batting_war
        player_war = batting_war

    war_string = f"{player_war}-{player_record.position}"

    if player_record.draftyear > 0:
        drafted_war += player_war
        num_drafted += 1
        count_by_round[player_record.draftround - 1] += 1
        war_by_round[player_record.draftround - 1] += player_war
        drafted_war_list_by_round[player_record.draftround - 1].append(war_string)
        drafted_war_list_by_year[player_record.draftyear].append(war_string)
    elif player_record.discoveryyear > 0:
        discovery_war += player_war
        num_discovery += 1
        discovery_war_list[player_record.discoveryyear].append(war_string)
    else:
        fa_war += player_war
        num_fa += 1

print("Summary:")
print("********************")
print(f"total players {num_players}")

print(f"drafted players {num_drafted}     drafted WAR: {int(drafted_war)}")
print(f"discovery players {num_discovery}   discovery WAR: {int(discovery_war)}")
print(f"FA players      {num_fa}   FA WAR: {int(fa_war)}")
print(f"Batting war {total_batting_war}")
print(f"Pitching war {total_pitching_war}")

print("")
print("")

print("War By Round:")
print("********************")
for round in range(32):
    if count_by_round[round] > 0:
        print(
            f"Round {round}   Total Players {count_by_round[round]}  Total War {int(war_by_round[round])}"
        )

print("")
print("")

print("Top By Round:")
print("********************")
for round in range(32):
    if len(drafted_war_list_by_round[round]) > 0:
        drafted_war_list_by_round[round].sort(reverse=True)
        num_to_display = min(10, len(drafted_war_list_by_round[round]))
        print(f"Round {round+1}: {drafted_war_list_by_round[round][0:num_to_display]}")

print("")
print("")
print("Drafted Top By Year:")
print("********************")
for index in range(32):
    year = 2056 - index
    if len(drafted_war_list_by_year[year]) > 0:
        drafted_war_list_by_year[year].sort(reverse=True)
        num_to_display = min(10, len(drafted_war_list_by_year[year]))
        print(f"Year {year}: {drafted_war_list_by_year[year][0:num_to_display]}")

print("")
print("")
print("Discovery Top By Year:")
print("********************")
for index in range(32):
    year = 2056 - index
    if len(discovery_war_list[year]) > 0:
        discovery_war_list[year].sort(reverse=True)
        num_to_display = min(10, len(discovery_war_list[year]))
        print(f"Year {year}: {discovery_war_list[year][0:num_to_display]}")
