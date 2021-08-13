from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from db import Player, PlayerBatting, PlayerFielding, PlayerPitching, PlayerStats
import datetime
from parser import BABIP

bat_throw_lookup = {
     1 : "Right",
     2 : "Left",
     3 : "Switch"
}

position_lookup = {
    0: "DH",
    1 : "P",
    2 : "C",
    3 : "1B",
    4 : "2B",
    5 : "3B",
    6 : "SS",
    7 : "LF",
    8 : "CF",
    9 : "RF",
    10 : "DH"
}

pitcher_lookup = {
    11 : "SP",
    12 : "RP",
    13 : "CL"
}

default_date = datetime.datetime.strptime("01/01/1900", "%m/%d/%Y")


class OOTPParser:

    def parse_tourney_records(self, playerfile, pt_id):
        parser = BeautifulSoup(playerfile, "lxml")
        parsed_players = {}
        parsed_players["batting"] = []
        parsed_players["pitching"] = []

        player_table = parser.body.table.table
        indicator_column = player_table.tr.find_all("th")[8]

        playerfile.seek(0)

        if indicator_column.string == "CON":
            print ("This is a batting tourney file")
            parsed_players["batting"].extend(self.parse_pt_tourney_batting_file(playerfile, pt_id))
        elif indicator_column.string == "OVR":
            print("This is a pitching tourney file")
            parsed_players["pitching"].extend(self.parse_pt_tourney_pitching_file(playerfile, pt_id))
        else:
            print ("NO CLUE what this file is")

        return parsed_players

    def parse_pt_tourney_batting_file(self, playerfile, pt_id):
        parser = BeautifulSoup(playerfile, "lxml")
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all("tr")[1:]
        for player in players:
            parsed_players.append(self.create_pt_tourney_batting_record(player, pt_id))

        return parsed_players

    def parse_pt_tourney_pitching_file(self, playerfile, pt_id):
        parser = BeautifulSoup(playerfile, "lxml")
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all("tr")[1:]
        for player in players:
            parsed_players.append(self.create_pt_tourney_pitching_record(player, pt_id))

        return parsed_players

    
    def parse_ootp_file(self, playerfile, import_date):
        parser = BeautifulSoup(playerfile, "lxml")
        parsed_players = {}
        parsed_players["player"] = []
        parsed_players["batting"] = []
        parsed_players["fielding"] = []
        parsed_players["pitching"] = []

        player_table = parser.body.table.table
        indicator_column = player_table.tr.find_all("th")[3]
        playerfile.seek(0)
        if indicator_column.string == "GAP":
            parsed_players["batting"].extend(self.parse_batting_file(playerfile, import_date))
        elif indicator_column.string == "IF RNG":
            parsed_players["fielding"].extend(self.parse_fielding_file(playerfile, import_date))
        elif indicator_column.string == "STU":
             parsed_players["pitching"].extend(self.parse_pitching_file(playerfile, import_date))
        elif indicator_column.string == "TM":
             parsed_players["player"].extend(self.parse_player_file(playerfile, import_date))
        else:
            print ("NO CLUE what this file is")
        
        return parsed_players
        
    def parse_player_file(self, playerfile, import_date):
        parser = BeautifulSoup(playerfile, "lxml")
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all("tr")[1:]
        for player in players:
            parsed_players.append(self.create_player_record(player, import_date))

        return parsed_players

    def parse_batting_file(self, playerfile, import_date):
        parser = BeautifulSoup(playerfile, "lxml")
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all("tr")[1:]
        for player in players:
            parsed_players.append(self.create_batting_record(player, import_date))

        return parsed_players

    def parse_fielding_file(self, playerfile, import_date):
        parser = BeautifulSoup(playerfile, "lxml")
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all("tr")[1:]
        for player in players:
            parsed_players.append(self.create_fielding_record(player, import_date))

        return parsed_players

    def parse_pitching_file(self, playerfile, import_date):
        parser = BeautifulSoup(playerfile, "lxml")
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all("tr")[1:]
        for player in players:
            parsed_players.append(self.create_pitching_record(player, import_date))

        return parsed_players

    def parse_stats_file(self, playerfile, season):
        parser = BeautifulSoup(playerfile, "lxml")
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all("tr")[1:]
        for player in players:
            parsed_players.append(self.create_stats_record(player, season))

        return parsed_players

    def parse_exports_file(self, exportsfile):
        parser = BeautifulSoup(exportsfile, "lxml")
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all("tr")[1:]
        for player in players:
            parsed_players.append(self.create_export_record(player))

        return parsed_players

    def create_pt_tourney_batting_record(self, player_parser, pt_id):
        attributes = player_parser.find_all("td")
        player = {}
        player["pt_id"] = pt_id
        player["ID"] = attributes[1].string
        player["POS"] = attributes[2].string
        player["Name"] = attributes[3].string
        player["TM"] = attributes[4].string
        player["TM2"] = attributes[5].string
        player["B"] = attributes[6].string
        player["T"] = attributes[7].string
        player["CON"] = attributes[8].string
        player["GAP"] = attributes[9].string
        player["POW"] = attributes[10].string
        player["EYE"] = attributes[11].string
        player["AVK"] = attributes[12].string
        player["CON vL"] = attributes[13].string
        player["GAP vL"] = attributes[14].string
        player["POW vL"] = attributes[15].string
        player["EYE vL"] = attributes[16].string
        player["AVK vL"] = attributes[17].string
        player["CON vR"] = attributes[18].string
        player["GAP vR"] = attributes[19].string
        player["POW vR"] = attributes[20].string
        player["EYE vR"] = attributes[21].string
        player["AVK vR"] = attributes[22].string
        player["BUN"] = attributes[23].string
        player["BFH"] = attributes[24].string
        player["BBT"] = attributes[25].string
        player["GBT"] = attributes[26].string
        player["FBT"] = attributes[27].string
        player["C ABI"] = attributes[28].string
        player["C ARM"] = attributes[29].string
        player["IF RNG"] = attributes[30].string
        player["IF ERR"] = attributes[31].string
        player["IF ARM"] = attributes[32].string
        player["TDP"] = attributes[33].string
        player["OF RNG"] = attributes[34].string
        player["OF ERR"] = attributes[35].string
        player["OF ARM"] = attributes[36].string
        player["P"] = attributes[37].string
        player["C"] = attributes[38].string
        player["1B"] = attributes[39].string
        player["2B"] = attributes[40].string
        player["3B"] = attributes[41].string
        player["SS"] = attributes[42].string
        player["LF"] = attributes[43].string
        player["CF"] = attributes[44].string
        player["RF"] = attributes[45].string
        player["SPE"] = attributes[46].string
        player["STE"] = attributes[47].string
        player["RUN"] = attributes[48].string
        player["G"] = attributes[49].string
        player["GS"] = attributes[50].string
        player["PA"] = attributes[51].string
        player["AB"] = attributes[52].string
        player["H"] = attributes[53].string
        player["1B"] = attributes[54].string
        player["2B"] = attributes[55].string
        player["3B"] = attributes[56].string
        player["HR"] = attributes[57].string
        player["RBI"] = attributes[58].string
        player["R"] = attributes[59].string
        player["BB"] = attributes[60].string
        player["IBB"] = attributes[61].string
        player["HP"] = attributes[62].string
        player["SH"] = attributes[63].string
        player["SF"] = attributes[64].string
        player["CI"] = attributes[65].string
        player["SO"] = attributes[66].string
        player["GIDP"] = attributes[67].string
        player["WAR"] = attributes[68].string
        player["SB"] = attributes[69].string
        player["CS"] = attributes[70].string
        player["BatR"] = attributes[71].string
        player["wSB"] = attributes[72].string
        player["UBR"] = attributes[73].string
        player["BsR"] = attributes[74].string
        player["TC"] = attributes[75].string
        player["A"] = attributes[76].string
        player["PO"] = attributes[77].string
        player["E"] = attributes[78].string
        player["DP"] = attributes[79].string
        player["TP"] = attributes[80].string
        player["ZR"] = attributes[81].string
        player["SBA"] = attributes[82].string
        player["RTO"] = attributes[83].string
        player["PB"] = attributes[84].string
        player["BIZ-R"] = attributes[85].string
        player["BIZ-Rm"] = attributes[86].string
        player["BIZ-L"] = attributes[87].string
        player["BIZ-Lm"] = attributes[88].string
        player["BIZ-E"] = attributes[89].string
        player["BIZ-Em"] = attributes[90].string
        player["BIZ-U"] = attributes[91].string
        player["BIZ-Um"] = attributes[92].string
        player["BIZ-Z"] = attributes[93].string
        player["BIZ-Zm"] = attributes[94].string
        player["BIZ-I"] = attributes[95].string

        return player

    def create_pt_tourney_pitching_record(self, player_parser, pt_id):
        attributes = player_parser.find_all("td")
        player = {}
        player["pt_id"] = pt_id
        player["ID"] = attributes[1].string
        player["POS"] = attributes[2].string
        player["RL"] = attributes[3].string
        player["Name"] = attributes[4].string
        player["TM"] = attributes[5].string
        player["B"] = attributes[6].string
        player["T"] = attributes[7].string
        player["OVR"] = attributes[8].string
        player["STU"] = attributes[9].string
        player["MOV"] = attributes[10].string
        player["CON"] = attributes[11].string
        player["STU vL"] = attributes[12].string
        player["MOV vL"] = attributes[13].string
        player["CON vL"] = attributes[14].string
        player["STU vR"] = attributes[15].string
        player["MOV vR"] = attributes[16].string
        player["CON vR"] = attributes[17].string
        player["FB"] = attributes[18].string
        player["CH"] = attributes[19].string
        player["CB"] = attributes[20].string
        player["SL"] = attributes[21].string
        player["SI"] = attributes[22].string
        player["SP"] = attributes[23].string
        player["CT"] = attributes[24].string
        player["FO"] = attributes[25].string
        player["CC"] = attributes[26].string
        player["SC"] = attributes[27].string
        player["KC"] = attributes[28].string
        player["KN"] = attributes[29].string
        player["PIT"] = attributes[30].string
        player["G/F"] = attributes[31].string
        player["VELO"] = attributes[32].string
        player["Slot"] = attributes[33].string
        player["PT"] = attributes[34].string
        player["STM"] = attributes[35].string
        player["HLD"] = attributes[36].string
        player["G"] = attributes[37].string
        player["GS"] = attributes[38].string
        player["W"] = attributes[39].string
        player["L"] = attributes[40].string
        player["SVO"] = attributes[41].string
        player["SV"] = attributes[42].string
        player["BS"] = attributes[43].string
        player["HLD"] = attributes[44].string
        player["SD"] = attributes[45].string
        player["MD"] = attributes[46].string
        player["IP"] = attributes[47].string
        player["BF"] = attributes[48].string
        player["AB"] = attributes[49].string
        player["HA"] = attributes[50].string
        player["1B"] = attributes[51].string
        player["2B"] = attributes[52].string
        player["HR"] = attributes[53].string
        player["TB"] = attributes[54].string
        player["R"] = attributes[55].string
        player["ER"] = attributes[56].string
        player["BB"] = attributes[57].string
        player["IBB"] = attributes[58].string
        player["K"] = attributes[59].string
        player["HP"] = attributes[60].string
        player["BABIP"] = attributes[61].string
        player["K/BB"] = attributes[62].string
        player["WP"] = attributes[63].string
        player["BK"] = attributes[64].string
        player["DP"] = attributes[65].string
        player["RA"] = attributes[66].string
        player["GF"] = attributes[67].string
        player["IR"] = attributes[68].string
        player["IRS"] = attributes[69].string
        player["QS"] = attributes[70].string
        player["CG"] = attributes[71].string
        player["RS"] = attributes[72].string
        player["PI"] = attributes[73].string
        player["GB"] = attributes[74].string
        player["FB"] = attributes[75].string
        player["SB"] = attributes[76].string
        player["CS"] = attributes[77].string
        player["WAR"] = attributes[78].string

        return player



    def create_player_record(self, player_parser, import_date):
        attributes = player_parser.find_all("td")
        player = Player()
        player.id = int(attributes[0].string)
        player.timestamp = import_date
        player.position = attributes[1].string
        player.name = attributes[2].string
        player.team = attributes[3].string
        player.org = attributes[4].string
        player.league = attributes[5].string
        player.level = attributes[6].string
        player.dob = datetime.datetime.strptime(attributes[7].string, "%m/%d/%Y")
        player.age = attributes[8].string
        player.height = self._convert_height(attributes[9].string)
        player.weight = int(attributes[10].string.split(" ")[0])
        player.bats = attributes[11].string
        player.throws = attributes[12].string
        player.overall = float(attributes[13].string.split(" ")[0])
        player.potential = float(attributes[14].string.split(" ")[0])
        player.leader = attributes[15].string
        player.loyalty = attributes[16].string
        player.adaptability = attributes[17].string
        player.greed = attributes[18].string
        player.workethic = attributes[19].string
        player.intelligence = attributes[20].string
        player.personality = attributes[21].string
        player.injury = attributes[22].string
        player.competition = attributes[23].string
        player.hscol = attributes[24].string
        player.salary = int(self._convert_unknown(attributes[25].string))
        player.yearsleft = int(self._convert_unknown(attributes[26].string))
        player.contractvalue = int(self._convert_unknown(attributes[27].string))
        player.totalyears = int(self._convert_unknown(attributes[28].string))
        player.majorleagueyears = int(attributes[29].string)
        player.majorleaguedays = int(attributes[30].string)
        player.proyears = int(attributes[31].string)
        player.draftleague = attributes[32].string
        player.draftteam = attributes[33].string
        player.draftyear = int(attributes[34].string)

        if "S" in attributes[35].string:
            player.draftround = int(attributes[35].string.replace("S", ""))
            player.draftsupplimental = 1
        else:
            player.draftround = int(attributes[35].string)
            player.draftsupplimental = 0

        player.draftpick = int(attributes[36].string)
        player.overallpick = int(attributes[37].string)
        player.discoveryyear = int(attributes[38].string)
        player.discoveryteam = attributes[39].string

        return player

    def create_pt_player_record(self, player_data, import_date):
        player = Player()
        player.id = player_data[74]
        player.timestamp = import_date
        player.position = position_lookup[player_data[7]]
        if player.position == "P":
            player.position = pitcher_lookup[player_data[8]]

        player.name = player_data[0]
        player.team = player_data[75]
        player.org =  " ".join([player_data[4], player_data[3]])
        player.league = "PT"
        player.level = "MLB"
        #player.dob = default_date
        #player.age = 0
        #player.height = int(player_data[73])
        #player.weight = 0
        player.bats = bat_throw_lookup[player_data[5]]
        player.throws = bat_throw_lookup[player_data[6]]
        player.overall = float(player_data[1])
        player.potential = float(player_data[1])
        #player.leader = attributes[15].string
        #player.loyalty = attributes[16].string
        #player.adaptability = attributes[17].string
        #player.greed = attributes[18].string
        #player.workethic = attributes[19].string
        #player.intelligence = attributes[20].string
        #player.personality = attributes[21].string
        #player.injury = attributes[22].string
        #player.competition = attributes[23].string
        #player.hscol = attributes[24].string
        #player.salary = int(self._convert_unknown(attributes[25].string))
        #player.yearsleft = int(self._convert_unknown(attributes[26].string))
        #player.contractvalue = int(self._convert_unknown(attributes[27].string))
        #player.totalyears = int(self._convert_unknown(attributes[28].string))
        #player.majorleagueyears = int(attributes[29].string)
        #player.majorleaguedays = int(attributes[30].string)
        #player.proyears = int(attributes[31].string)
        #player.draftleague = attributes[32].string
        #player.draftteam = attributes[33].string
        #player.draftyear = int(attributes[34].string)

        #if "S" in attributes[35].string:
        #    player.draftround = int(attributes[35].string.replace("S", ""))
        #    player.draftsupplimental = 1
        #else:
        #    player.draftround = int(attributes[35].string)
        #    player.draftsupplimental = 0

        #player.draftpick = int(attributes[36].string)
        #player.overallpick = int(attributes[37].string)
        #player.discoveryyear = int(attributes[38].string)
        #player.discoveryteam = attributes[39].string

        return player

    def create_batting_record(self, player_parser, import_date):
        attributes = player_parser.find_all("td")
        player = PlayerBatting()

        player.playerid = int(attributes[0].string)
        player.timestamp = import_date
        player.name = attributes[1].string
        player.contactrating = int(self._convert_unknown(attributes[2].string))
        player.gaprating = int(self._convert_unknown(attributes[3].string))
        player.powerrating = int(self._convert_unknown(attributes[4].string))
        player.eyerating = int(self._convert_unknown(attributes[5].string))
        player.krating = int(self._convert_unknown(attributes[6].string))
        player.contactvleft = int(self._convert_unknown(attributes[7].string))
        player.gapvleft = int(self._convert_unknown(attributes[8].string))
        player.powervleft = int(self._convert_unknown(attributes[9].string))
        player.eyevleft = int(self._convert_unknown(attributes[10].string))
        player.kvleft = int(self._convert_unknown(attributes[11].string))
        player.contactvright = int(self._convert_unknown(attributes[12].string))
        player.gapvright = int(self._convert_unknown(attributes[13].string))
        player.powervright = int(self._convert_unknown(attributes[14].string))
        player.eyevright = int(self._convert_unknown(attributes[15].string))
        player.kvright = int(self._convert_unknown(attributes[16].string))
        player.contactpotential = int(self._convert_unknown(attributes[17].string))
        player.gappotential = int(self._convert_unknown(attributes[18].string))
        player.powerpotential = int(self._convert_unknown(attributes[19].string))
        player.eyeprotential = int(self._convert_unknown(attributes[20].string))
        player.kprotential = int(self._convert_unknown(attributes[21].string))
        player.buntrating = int(self._convert_unknown(attributes[22].string))
        player.buntforhitrating = int(self._convert_unknown(attributes[23].string))
        player.battedballtype = attributes[24].string
        player.groundballtype = attributes[25].string
        player.flyballtype = attributes[26].string
        player.speedrating = int(self._convert_unknown(attributes[27].string))
        player.stealrating = int(self._convert_unknown(attributes[28].string))
        player.baserunningrating = int(self._convert_unknown(attributes[29].string))
        player.babipoverall = BABIP.calc_babip(player.contactrating, player.powerrating, player.krating)
        player.babippotential = BABIP.calc_babip(player.contactpotential, player.powerpotential, player.kprotential)

        return player

    def create_pt_batting_record(self, player_data, import_date):
        player = PlayerBatting()

        player.playerid = int(player_data[74])
        player.timestamp = import_date
        player.name = player_data[0]
        player.contactrating = player_data[9]
        player.gaprating = player_data[10]
        player.powerrating = player_data[11]
        player.eyerating = player_data[12]
        player.krating = player_data[13]
        player.contactvleft = player_data[14]
        player.gapvleft = player_data[15]
        player.powervleft = player_data[16]
        player.eyevleft = player_data[17]
        player.kvleft = player_data[18]
        player.contactvright = player_data[19]
        player.gapvright = player_data[20]
        player.powervright = player_data[21]
        player.eyevright = player_data[22]
        player.kvright = player_data[23]
        player.contactpotential = player_data[9]
        player.gappotential = player_data[10]
        player.powerpotential = player_data[11]
        player.eyeprotential = player_data[12]
        player.kprotential = player_data[13]
        player.buntrating = player_data[27]
        player.buntforhitrating = player_data[28]
        player.battedballtype = "Normal"
        player.groundballtype = "Spray Hitter"
        player.flyballtype = "Spray Hitter"
        player.speedrating = player_data[24]
        player.stealrating = player_data[25]
        player.baserunningrating = player_data[26]
        player.babipoverall = BABIP.calc_babip(player.contactrating, player.powerrating, player.krating)
        player.babippotential = BABIP.calc_babip(player.contactpotential, player.powerpotential, player.kprotential)

        return player

    def create_fielding_record(self, player_parser, import_date):
        attributes = player_parser.find_all("td")
        player = PlayerFielding()

        player.playerid = int(attributes[0].string)
        player.timestamp = import_date
        player.name = attributes[1].string
        player.infieldrange = int(self._convert_unknown(attributes[3].string))
        player.infieldarm = int(self._convert_unknown(attributes[4].string))
        player.turndoubleplay = int(self._convert_unknown(attributes[5].string))
        player.infielderror = int(self._convert_unknown(attributes[6].string))
        player.outfieldrange = int(self._convert_unknown(attributes[7].string))
        player.outfieldarm = int(self._convert_unknown(attributes[8].string))
        player.outfielderror = int(self._convert_unknown(attributes[9].string))
        player.catcherarm = int(self._convert_unknown(attributes[10].string))
        player.catcherability = int(self._convert_unknown(attributes[11].string))
        player.priamrydefensiverating = int(
            self._convert_unknown(attributes[12].string)
        )
        player.pitcherrating = int(self._convert_unknown(attributes[13].string))
        player.catcherrating = int(self._convert_unknown(attributes[14].string))
        player.firstbaserating = int(self._convert_unknown(attributes[15].string))
        player.secondbaserating = int(self._convert_unknown(attributes[16].string))
        player.thirdbaserating = int(self._convert_unknown(attributes[17].string))
        player.shortstoprating = int(self._convert_unknown(attributes[18].string))
        player.leftfieldrating = int(self._convert_unknown(attributes[19].string))
        player.centerfieldrating = int(self._convert_unknown(attributes[20].string))
        player.rightfieldrating = int(self._convert_unknown(attributes[21].string))

        return player

    def create_pt_fielding_record(self, player_data, import_date):
        player = PlayerFielding()

        player.playerid = int(player_data[74])
        player.timestamp = import_date
        player.name = player_data[0]
        player.infieldrange = player_data[55]
        player.infieldarm = player_data[57]
        player.turndoubleplay = player_data[58]
        player.infielderror = player_data[56]
        player.outfieldrange = player_data[61]
        player.outfieldarm = player_data[63]
        player.outfielderror = player_data[62]
        player.catcherarm = player_data[60]
        player.catcherability = player_data[62]
        player.priamrydefensiverating = 0
        player.pitcherrating = player_data[64]
        player.catcherrating = player_data[65]
        player.firstbaserating = player_data[66]
        player.secondbaserating = player_data[67]
        player.thirdbaserating = player_data[68]
        player.shortstoprating = player_data[69]
        player.leftfieldrating = player_data[70]
        player.centerfieldrating = player_data[71]
        player.rightfieldrating = player_data[72]

        return player


    def create_pitching_record(self, player_parser, import_date):
        attributes = player_parser.find_all("td")
        player = PlayerPitching()

        player.playerid = int(attributes[0].string)
        player.timestamp = import_date
        player.name = attributes[1].string

        player.stuffrating = int(self._convert_unknown(attributes[3].string))
        player.movementrating = int(self._convert_unknown(attributes[4].string))
        player.controlrating = int(self._convert_unknown(attributes[5].string))
        player.stuffvleft = int(self._convert_unknown(attributes[6].string))
        player.movementvleft = int(self._convert_unknown(attributes[7].string))
        player.controlvleft = int(self._convert_unknown(attributes[8].string))
        player.stuffvright = int(self._convert_unknown(attributes[9].string))
        player.movementvright = int(self._convert_unknown(attributes[10].string))
        player.controlvright = int(self._convert_unknown(attributes[11].string))
        player.stuffpotential = int(self._convert_unknown(attributes[12].string))
        player.movementpotential = int(self._convert_unknown(attributes[13].string))
        player.controlpotential = int(self._convert_unknown(attributes[14].string))
        player.fastballrating = int(self._convert_unknown(attributes[15].string))
        player.fastballpotential = int(self._convert_unknown(attributes[16].string))
        player.changeuprating = int(self._convert_unknown(attributes[17].string))
        player.changeuppotential = int(self._convert_unknown(attributes[18].string))
        player.curveballrating = int(self._convert_unknown(attributes[19].string))
        player.curveballpotential = int(self._convert_unknown(attributes[20].string))
        player.sliderrating = int(self._convert_unknown(attributes[21].string))
        player.sliderpotential = int(self._convert_unknown(attributes[22].string))
        player.splitterrating = int(self._convert_unknown(attributes[23].string))
        player.splitterpotential = int(self._convert_unknown(attributes[24].string))
        player.sinkerrating = int(self._convert_unknown(attributes[25].string))
        player.sinkerpotential = int(self._convert_unknown(attributes[26].string))
        player.cutterrating = int(self._convert_unknown(attributes[27].string))
        player.cutterpotential = int(self._convert_unknown(attributes[28].string))
        player.forkballrating = int(self._convert_unknown(attributes[29].string))
        player.forkballpotential = int(self._convert_unknown(attributes[30].string))
        player.circlechangerating = int(self._convert_unknown(attributes[31].string))
        player.circlechangepotential = int(self._convert_unknown(attributes[32].string))
        player.screwballrating = int(self._convert_unknown(attributes[33].string))
        player.screwballpotential = int(self._convert_unknown(attributes[34].string))
        player.knucklecurverating = int(self._convert_unknown(attributes[35].string))
        player.knucklecurvepotential = int(self._convert_unknown(attributes[36].string))
        player.knuckleballrating = int(self._convert_unknown(attributes[37].string))
        player.knuckleballpotential = int(self._convert_unknown(attributes[38].string))
        player.numpitches = int(self._convert_unknown(attributes[39].string))
        player.groundballflyball = attributes[40].string
        player.velocity = int(self._convert_unknown(attributes[41].string))
        player.armslot = attributes[42].string
        player.pitchertype = attributes[43].string
        player.stamina = int(self._convert_unknown(attributes[44].string))
        player.hold = 0

        return player

    def create_pt_pitching_record(self, player_data, import_date):
        player = PlayerPitching()

        player.playerid = int(player_data[74])
        player.timestamp = import_date
        player.name = player_data[0]

        player.stuffrating = player_data[29]
        player.movementrating = player_data[30]
        player.controlrating = player_data[31]
        player.stuffvleft = player_data[32]
        player.movementvleft = player_data[33]
        player.controlvleft = player_data[34]
        player.stuffvright = player_data[35]
        player.movementvright = player_data[36]
        player.controlvright = player_data[37]
        player.stuffpotential = player_data[29]
        player.movementpotential = player_data[30]
        player.controlpotential = player_data[31]
        player.fastballrating = player_data[38]
        player.fastballpotential = player_data[38]
        player.changeuprating = player_data[41]
        player.changeuppotential = player_data[41]
        player.curveballrating = player_data[40]
        player.curveballpotential = player_data[40]
        player.sliderrating = player_data[39]
        player.sliderpotential = player_data[39]
        player.splitterrating = player_data[44]
        player.splitterpotential = player_data[44]
        player.sinkerrating = player_data[43]
        player.sinkerpotential = player_data[43]
        player.cutterrating = player_data[42]
        player.cutterpotential = player_data[42]
        player.forkballrating = player_data[45]
        player.forkballpotential = player_data[45]
        player.circlechangerating = player_data[46]
        player.circlechangepotential = player_data[46]
        player.screwballrating = player_data[47]
        player.screwballpotential = player_data[47]
        player.knucklecurverating = player_data[48]
        player.knucklecurvepotential = player_data[48]
        player.knuckleballrating = player_data[49]
        player.knuckleballpotential = player_data[49]
        

        num_pitches = 0
        for i in range(38, 50):
            if player_data[i] > 0:
                num_pitches = num_pitches + 1
        player.numpitches = num_pitches

        player.groundballflyball = str(player_data[52])
        player.velocity = player_data[53]
        player.armslot = player_data[54]
        player.pitchertype = ""
        player.stamina = player_data[50]
        player.hold = player_data[51]
        return player

    def create_stats_record(self, player_parser, season):
        attributes = player_parser.find_all("td")
        player = PlayerStats()

        player.playerid = int(attributes[1].string)
        player.season = season
        player.position = attributes[2].string
        player.name = attributes[3].string
        player.plateapp = int(attributes[4].string)
        player.battingwar = float(attributes[5].string)
        player.ip = float(attributes[6].string)
        player.battersfaced = int(attributes[7].string)
        player.pitchingwar = float(attributes[8].string)
        player.zonerating = float(attributes[9].string)
        player.defeff = float(attributes[10].string)
        player.woba = float(attributes[11].string)
        player.wrcplus = float(attributes[12].string)
        player.babip = float(attributes[13].string)
        player.kminuswalk = float(attributes[14].string)
        player.fip = float(attributes[15].string)
        player.opsplus = float(attributes[16].string)
        player.whip = float(attributes[17].string)

        return player

    def create_export_record(self, player_parser):
        attributes = player_parser.find_all("td")
        player = {}

        player["id"] = int(attributes[0].string)
        player["position"] = attributes[1].string
        player["name"] = attributes[2].string

        return player

    @classmethod
    def _convert_unknown(cls, value):
        if value == "-":
            return "0"
        elif value[0] == "$":
            return value[1:].replace(",", "")
        elif value == "Free agent":
            return "0"
        elif "-" in value:
            velocities = value.split(" ")[0].split("-")
            return int((int(velocities[0]) + int(velocities[1])) / 2)
        elif "100+" in value:
            return 101
        else:
            return value.split(" ")[0]

    @classmethod
    def _convert_height(cls, height):
        H_feet = height.split("'")[0]
        H_inch = height.split(" ")[1].split('"')[0]

        H_inches = int(H_feet) * 12 + int(H_inch)

        return H_inches
