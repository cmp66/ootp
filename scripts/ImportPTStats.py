import os
import sys
from datetime import datetime, timezone
from dateutil import parser
import pylightxl as xl
from parser import OOTPParser

datetimestamp = sys.argv[1]

import_datetime = parser.parse(datetimestamp)

def importPTFiles(dirname):
    player_parser = OOTPParser()
    pt_players={}
    pt_players["batting"] = []
    pt_players["pitching"] = []

    for (dirpath, dirnames, filenames) in os.walk(dirname):
        for dirname in dirnames:
            if ".pt" in dirname:
                fulldirpath = os.path.join(dirpath, dirname)
                modified_time = datetime.fromtimestamp(os.stat(fulldirpath).st_mtime, tz=timezone.utc)
                if modified_time > import_datetime:
                    pt_id = modified_time.strftime("%Y%m%d%H%M") #dirname[:-3]
                    statfile_dir = os.path.join(fulldirpath, "news/html/temp")
                    print (f'{pt_id} -> {str(modified_time)}')
                    for (_, _, statfilenames) in os.walk(statfile_dir):
                        full_statfile_names = [os.path.join(statfile_dir, fname) for fname in statfilenames]
                        for stat_file in full_statfile_names:
                            with open(stat_file, "r", encoding="utf-8") as handle:
                                player_records = player_parser.parse_tourney_records(handle, pt_id)
                                pt_players['batting'] = pt_players['batting'] + player_records['batting']
                                pt_players['pitching'] = pt_players['pitching'] + player_records['pitching']
                                print (f'parsing {stat_file}')

    return pt_players

def write_batting_rows(bsheet, players):
    row_index = 3
    for player in players:
        bsheet.update_index(row=row_index, col=1, val=player["pt_id"])
        bsheet.update_index(row=row_index, col=2, val=player["ID"]) 
        bsheet.update_index(row=row_index, col=3, val=player["POS"]) 
        bsheet.update_index(row=row_index, col=4, val=player["Name"]) 
        bsheet.update_index(row=row_index, col=5, val=player["TM"]) 
        bsheet.update_index(row=row_index, col=6, val=player["TM2"]) 
        bsheet.update_index(row=row_index, col=7, val=player["B"]) 
        bsheet.update_index(row=row_index, col=8, val=player["T"]) 
        bsheet.update_index(row=row_index, col=9, val=player["CON"]) 
        bsheet.update_index(row=row_index, col=10, val=player["GAP"]) 
        bsheet.update_index(row=row_index, col=11, val=player["POW"]) 
        bsheet.update_index(row=row_index, col=12, val=player["EYE"]) 
        bsheet.update_index(row=row_index, col=13, val=player["AVK"]) 
        bsheet.update_index(row=row_index, col=14, val=player["CON vL"]) 
        bsheet.update_index(row=row_index, col=15, val=player["GAP vL"]) 
        bsheet.update_index(row=row_index, col=16, val=player["POW vL"]) 
        bsheet.update_index(row=row_index, col=17, val=player["EYE vL"]) 
        bsheet.update_index(row=row_index, col=18, val=player["AVK vL"]) 
        bsheet.update_index(row=row_index, col=19, val=player["CON vR"]) 
        bsheet.update_index(row=row_index, col=20, val=player["GAP vR"]) 
        bsheet.update_index(row=row_index, col=21, val=player["POW vR"]) 
        bsheet.update_index(row=row_index, col=22, val=player["EYE vR"]) 
        bsheet.update_index(row=row_index, col=23, val=player["AVK vR"]) 
        bsheet.update_index(row=row_index, col=24, val=player["BUN"]) 
        bsheet.update_index(row=row_index, col=25, val=player["BFH"]) 
        bsheet.update_index(row=row_index, col=26, val=player["BBT"]) 
        bsheet.update_index(row=row_index, col=27, val=player["GBT"]) 
        bsheet.update_index(row=row_index, col=28, val=player["FBT"]) 
        bsheet.update_index(row=row_index, col=29, val=player["C ABI"]) 
        bsheet.update_index(row=row_index, col=30, val=player["C ARM"]) 
        bsheet.update_index(row=row_index, col=31, val=player["IF RNG"]) 
        bsheet.update_index(row=row_index, col=32, val=player["IF ERR"]) 
        bsheet.update_index(row=row_index, col=33, val=player["IF ARM"]) 
        bsheet.update_index(row=row_index, col=34, val=player["TDP"]) 
        bsheet.update_index(row=row_index, col=35, val=player["OF RNG"]) 
        bsheet.update_index(row=row_index, col=36, val=player["OF ERR"]) 
        bsheet.update_index(row=row_index, col=37, val=player["OF ARM"]) 
        bsheet.update_index(row=row_index, col=38, val=player["P"]) 
        bsheet.update_index(row=row_index, col=39, val=player["C"]) 
        bsheet.update_index(row=row_index, col=40, val=player["1B"]) 
        bsheet.update_index(row=row_index, col=41, val=player["2B"]) 
        bsheet.update_index(row=row_index, col=42, val=player["3B"]) 
        bsheet.update_index(row=row_index, col=43, val=player["SS"]) 
        bsheet.update_index(row=row_index, col=44, val=player["LF"]) 
        bsheet.update_index(row=row_index, col=45, val=player["CF"]) 
        bsheet.update_index(row=row_index, col=46, val=player["RF"]) 
        bsheet.update_index(row=row_index, col=47, val=player["SPE"]) 
        bsheet.update_index(row=row_index, col=48, val=player["STE"]) 
        bsheet.update_index(row=row_index, col=49, val=player["RUN"]) 
        bsheet.update_index(row=row_index, col=50, val=player["G"]) 
        bsheet.update_index(row=row_index, col=51, val=player["GS"]) 
        bsheet.update_index(row=row_index, col=52, val=player["PA"]) 
        bsheet.update_index(row=row_index, col=53, val=player["AB"]) 
        bsheet.update_index(row=row_index, col=54, val=player["H"]) 
        bsheet.update_index(row=row_index, col=55, val=player["1B"]) 
        bsheet.update_index(row=row_index, col=56, val=player["2B"]) 
        bsheet.update_index(row=row_index, col=57, val=player["3B"]) 
        bsheet.update_index(row=row_index, col=58, val=player["HR"]) 
        bsheet.update_index(row=row_index, col=59, val=player["RBI"]) 
        bsheet.update_index(row=row_index, col=60, val=player["R"]) 
        bsheet.update_index(row=row_index, col=61, val=player["BB"]) 
        bsheet.update_index(row=row_index, col=62, val=player["IBB"]) 
        bsheet.update_index(row=row_index, col=63, val=player["HP"]) 
        bsheet.update_index(row=row_index, col=64, val=player["SH"]) 
        bsheet.update_index(row=row_index, col=65, val=player["SF"]) 
        bsheet.update_index(row=row_index, col=66, val=player["CI"]) 
        bsheet.update_index(row=row_index, col=67, val=player["SO"]) 
        bsheet.update_index(row=row_index, col=68, val=player["GIDP"]) 
        bsheet.update_index(row=row_index, col=69, val=player["WAR"]) 
        bsheet.update_index(row=row_index, col=70, val=player["SB"]) 
        bsheet.update_index(row=row_index, col=71, val=player["CS"]) 
        bsheet.update_index(row=row_index, col=72, val=player["BatR"]) 
        bsheet.update_index(row=row_index, col=73, val=player["wSB"]) 
        bsheet.update_index(row=row_index, col=74, val=player["UBR"]) 
        bsheet.update_index(row=row_index, col=75, val=player["BsR"]) 
        bsheet.update_index(row=row_index, col=76, val=player["TC"]) 
        bsheet.update_index(row=row_index, col=77, val=player["A"]) 
        bsheet.update_index(row=row_index, col=78, val=player["PO"]) 
        bsheet.update_index(row=row_index, col=79, val=player["E"]) 
        bsheet.update_index(row=row_index, col=80, val=player["DP"])
        bsheet.update_index(row=row_index, col=81, val=player["TP"]) 
        bsheet.update_index(row=row_index, col=82, val=player["ZR"]) 
        bsheet.update_index(row=row_index, col=83, val=player["SBA"]) 
        bsheet.update_index(row=row_index, col=84, val=player["RTO"]) 
        bsheet.update_index(row=row_index, col=85, val=player["PB"]) 
        bsheet.update_index(row=row_index, col=86, val=player["BIZ-R"]) 
        bsheet.update_index(row=row_index, col=87, val=player["BIZ-Rm"]) 
        bsheet.update_index(row=row_index, col=88, val=player["BIZ-L"]) 
        bsheet.update_index(row=row_index, col=89, val=player["BIZ-Lm"]) 
        bsheet.update_index(row=row_index, col=90, val=player["BIZ-E"]) 
        bsheet.update_index(row=row_index, col=91, val=player["BIZ-Em"]) 
        bsheet.update_index(row=row_index, col=92, val=player["BIZ-U"]) 
        bsheet.update_index(row=row_index, col=93, val=player["BIZ-Um"]) 
        bsheet.update_index(row=row_index, col=94, val=player["BIZ-Z"]) 
        bsheet.update_index(row=row_index, col=95, val=player["BIZ-Zm"]) 
        bsheet.update_index(row=row_index, col=96, val=player["BIZ-I"]) 

        row_index = row_index + 1

def write_pitching_rows(psheet, players):
    row_index = 3
    for player in players:
        psheet.update_index(row=row_index, col=1, val=player["pt_id"])
        psheet.update_index(row=row_index, col=2, val=player["ID"]) 
        psheet.update_index(row=row_index, col=3, val=player["POS"])
        psheet.update_index(row=row_index, col=4, val=player["RL"]) 
        psheet.update_index(row=row_index, col=5, val=player["Name"]) 
        psheet.update_index(row=row_index, col=6, val=player["TM"]) 
        psheet.update_index(row=row_index, col=7, val=player["B"]) 
        psheet.update_index(row=row_index, col=8, val=player["T"]) 
        psheet.update_index(row=row_index, col=9, val=player["OVR"]) 
        psheet.update_index(row=row_index, col=10, val=player["STU"]) 
        psheet.update_index(row=row_index, col=11, val=player["MOV"]) 
        psheet.update_index(row=row_index, col=12, val=player["CON"]) 
        psheet.update_index(row=row_index, col=13, val=player["STU vL"]) 
        psheet.update_index(row=row_index, col=14, val=player["MOV vL"]) 
        psheet.update_index(row=row_index, col=15, val=player["CON vL"]) 
        psheet.update_index(row=row_index, col=16, val=player["STU vR"]) 
        psheet.update_index(row=row_index, col=17, val=player["MOV vR"]) 
        psheet.update_index(row=row_index, col=18, val=player["CON vR"]) 
        psheet.update_index(row=row_index, col=19, val=player["FB"]) 
        psheet.update_index(row=row_index, col=20, val=player["CH"]) 
        psheet.update_index(row=row_index, col=21, val=player["CB"]) 
        psheet.update_index(row=row_index, col=22, val=player["SL"]) 
        psheet.update_index(row=row_index, col=23, val=player["SI"]) 
        psheet.update_index(row=row_index, col=24, val=player["SP"]) 
        psheet.update_index(row=row_index, col=25, val=player["CT"]) 
        psheet.update_index(row=row_index, col=26, val=player["FO"]) 
        psheet.update_index(row=row_index, col=27, val=player["CC"]) 
        psheet.update_index(row=row_index, col=28, val=player["SC"]) 
        psheet.update_index(row=row_index, col=29, val=player["KC"]) 
        psheet.update_index(row=row_index, col=30, val=player["KN"]) 
        psheet.update_index(row=row_index, col=31, val=player["PIT"]) 
        psheet.update_index(row=row_index, col=32, val=player["G/F"]) 
        psheet.update_index(row=row_index, col=33, val=player["VELO"]) 
        psheet.update_index(row=row_index, col=34, val=player["Slot"]) 
        psheet.update_index(row=row_index, col=35, val=player["PT"]) 
        psheet.update_index(row=row_index, col=36, val=player["STM"]) 
        psheet.update_index(row=row_index, col=37, val=player["HLD"]) 
        psheet.update_index(row=row_index, col=38, val=player["G"]) 
        psheet.update_index(row=row_index, col=39, val=player["GS"]) 
        psheet.update_index(row=row_index, col=40, val=player["W"]) 
        psheet.update_index(row=row_index, col=41, val=player["L"]) 
        psheet.update_index(row=row_index, col=42, val=player["SVO"]) 
        psheet.update_index(row=row_index, col=43, val=player["SV"]) 
        psheet.update_index(row=row_index, col=44, val=player["BS"]) 
        psheet.update_index(row=row_index, col=45, val=player["HLD"]) 
        psheet.update_index(row=row_index, col=46, val=player["SD"]) 
        psheet.update_index(row=row_index, col=47, val=player["MD"]) 
        psheet.update_index(row=row_index, col=48, val=player["IP"]) 
        psheet.update_index(row=row_index, col=49, val=player["BF"]) 
        psheet.update_index(row=row_index, col=50, val=player["AB"]) 
        psheet.update_index(row=row_index, col=51, val=player["HA"]) 
        psheet.update_index(row=row_index, col=52, val=player["1B"]) 
        psheet.update_index(row=row_index, col=53, val=player["2B"]) 
        psheet.update_index(row=row_index, col=54, val=player["HR"]) 
        psheet.update_index(row=row_index, col=55, val=player["TB"]) 
        psheet.update_index(row=row_index, col=56, val=player["R"]) 
        psheet.update_index(row=row_index, col=57, val=player["ER"]) 
        psheet.update_index(row=row_index, col=58, val=player["BB"]) 
        psheet.update_index(row=row_index, col=59, val=player["IBB"]) 
        psheet.update_index(row=row_index, col=60, val=player["K"]) 
        psheet.update_index(row=row_index, col=61, val=player["HP"]) 
        psheet.update_index(row=row_index, col=62, val=player["BABIP"]) 
        psheet.update_index(row=row_index, col=63, val=player["K/BB"]) 
        psheet.update_index(row=row_index, col=64, val=player["WP"]) 
        psheet.update_index(row=row_index, col=65, val=player["BK"]) 
        psheet.update_index(row=row_index, col=66, val=player["DP"]) 
        psheet.update_index(row=row_index, col=67, val=player["RA"]) 
        psheet.update_index(row=row_index, col=68, val=player["GF"]) 
        psheet.update_index(row=row_index, col=69, val=player["IR"]) 
        psheet.update_index(row=row_index, col=70, val=player["IRS"]) 
        psheet.update_index(row=row_index, col=71, val=player["QS"]) 
        psheet.update_index(row=row_index, col=72, val=player["CG"]) 
        psheet.update_index(row=row_index, col=73, val=player["RS"]) 
        psheet.update_index(row=row_index, col=74, val=player["PI"]) 
        psheet.update_index(row=row_index, col=75, val=player["GB"]) 
        psheet.update_index(row=row_index, col=76, val=player["FB"]) 
        psheet.update_index(row=row_index, col=77, val=player["SB"]) 
        psheet.update_index(row=row_index, col=78, val=player["CS"]) 
        psheet.update_index(row=row_index, col=79, val=player["WAR"]) 

        row_index = row_index + 1


def update_stats_sheet(players, stat_file):
    db = xl.readxl(stat_file)

    batting_sheet = db.ws('Raw')
    write_batting_rows(batting_sheet, players['batting'])
    
    pitching_sheet = db.ws('Raw Pitch')
    write_pitching_rows(pitching_sheet, players['pitching'])

    xl.writexl(db=db, fn='./sheets/Iron-Copy.xlsx')


    




players = importPTFiles(f'/home/wahoo/linkdirs/ootp22/saved_games')
update_stats_sheet(players, '/home/wahoo/projects/ootp/sheets/Iron-Tourneys-Transfer.xlsx')
