from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from db import Player, PlayerBatting, PlayerFielding, PlayerPitching, PlayerStats
import datetime


class OOTPParser:
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
        player.powerrightt = int(self._convert_unknown(attributes[14].string))
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
        player.primarydefensiverating = int(
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
