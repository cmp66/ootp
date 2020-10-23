from db import OOTPDbAccess, PlayerStats, Player

db_access = OOTPDbAccess('mysql', 'localhost', 'ootp', 'ootp--11oo')

season = 2055
total_pitching_war = 0
total_batting_war = 0
num_players = 0
num_drafted, drafted_war = (0, 0)
num_discovery, discovery_war = (0, 0)
count_by_round = [0] * 32
war_by_round = [0] * 32
num_fa, fa_war = (0, 0)

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

    if player_record.draftyear > 0:
        drafted_war += player_war
        num_drafted += 1
        count_by_round[player_record.draftround-1] += 1
        war_by_round[player_record.draftround-1] += player_war
    elif player_record.discoveryyear > 0:
        discovery_war += player_war
        num_discovery += 1
    else:
        fa_war += player_war
        num_fa += 1 

print (f'total players {num_players}')

print (f'drafted players {num_drafted}     drafted WAR: {int(drafted_war)}')
print (f'discovery players {num_discovery}   discovery WAR: {int(discovery_war)}')
print (f'FA players      {num_fa}   FA WAR: {int(fa_war)}')

for round in range(16):
    print(f'Round {round}   Total Players {count_by_round[round]}  Total War {int(war_by_round[round])}')
    
print (f'Batting war {total_batting_war}')
print (f'Pitching war {total_pitching_war}')
