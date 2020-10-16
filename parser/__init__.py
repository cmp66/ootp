from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from db import Player, PlayerBatting, PlayerFielding, PlayerPitching
import datetime

class OOTPParser():

    def parse_player_file(self, playerfile, import_date):
        parser = BeautifulSoup(playerfile, 'lxml')
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all('tr')[1:]
        for player in players:
            parsed_players.append(self.create_player_record(player, import_date))

        return parsed_players

    def parse_batting_file(self, playerfile, import_date):
        parser = BeautifulSoup(playerfile, 'lxml')
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all('tr')[1:]
        for player in players:
            parsed_players.append(self.create_batting_record(player, import_date))

        return parsed_players

    def parse_fielding_file(self, playerfile, import_date):
        parser = BeautifulSoup(playerfile, 'lxml')
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all('tr')[1:]
        for player in players:
            parsed_players.append(self.create_fielding_record(player, import_date))

        return parsed_players

    def parse_pitching_file(self, playerfile, import_date):
        parser = BeautifulSoup(playerfile, 'lxml')
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all('tr')[1:]
        for player in players:
            parsed_players.append(self.create_pitching_record(player, import_date))

        return parsed_players

    def create_player_record(self, player_parser, import_date):
        attributes = player_parser.find_all('td')
        player = Player()
        player.id = int(attributes[0].string)
        player.timestamp = import_date
        player.position = attributes[1].string
        player.name = attributes[2].string
        player.team = attributes[3].string
        print(f'ORG: {attributes[4].string}')
        player.org = attributes[4].string
        player.league = attributes[5].string
        player.level = attributes[6].string
        player.dob = datetime.datetime.strptime(attributes[7].string, '%m/%d/%Y')
        player.age = attributes[8].string
        player.height = self._convert_height(attributes[9].string)
        player.weight = int(attributes[10].string.split(" ")[0])
        player.bats = attributes[11].string
        player.throws = attributes[12].string
        player.leader = attributes[13].string
        player.loyalty = attributes[14].string
        player.adaptability = attributes[15].string
        player.greed = attributes[16].string
        player.workethic = attributes[17].string
        player.intelligence = attributes[18].string
        player.personality = attributes[19].string
        player.injury = attributes[20].string
        player.competition = attributes[21].string
        player.hscol = attributes[22].string
        player.salary = int(self._convert_unknown(attributes[23].string))
        player.yearsleft = int(self._convert_unknown(attributes[24].string))
        player.contractvalue = int(self._convert_unknown(attributes[25].string))
        player.totalyears = int(self._convert_unknown(attributes[26].string))
        player.majorleagueyears = int(attributes[27].string)
        player.majorleaguedays = int(attributes[28].string)
        player.proyears = int(attributes[29].string)
        player.draftleague = attributes[30].string
        player.draftteam = attributes[31].string
        player.draftyear = int(attributes[32].string)

        if 'S' in attributes[33].string:
            player.draftround = int(attributes[33].string.replace('S', ''))
            player.draftsupplimental = 1
        else:
            player.draftround = int(attributes[33].string)
            player.draftsupplimental = 0

        player.draftpick = int(attributes[34].string)
        player.overallpick = int(attributes[35].string)
        player.discoveryyear = int(attributes[36].string)
        player.discoveryteam = attributes[37].string

        return player

    def create_batting_record(self, player_parser, import_date):
        attributes = player_parser.find_all('td')
        player = PlayerBatting()
        
        player.playerid = int(attributes[0].string)
        player.timestamp = import_date
        player.name = attributes[1].string
        player.contactrating = int(attributes[2].string)
        player.gaprating = int(attributes[3].string)
        player.powerrating = int(attributes[4].string)
        player.eyerating = int(attributes[5].string)
        player.krating = int(attributes[6].string)
        player.contactvleft = int(attributes[7].string)
        player.gapvleft = int(attributes[8].string)
        player.powervleft = int(attributes[9].string)
        player.eyevleft = int(attributes[10].string)
        player.kvleft = int(attributes[11].string)
        player.contactvright = int(attributes[12].string)
        player.gapvright = int(attributes[13].string)
        player.powerrightt = int(attributes[14].string)
        player.eyevright = int(attributes[15].string)
        player.kvright = int(attributes[16].string)
        player.contactpotential = int(attributes[17].string)
        player.gappotential = int(attributes[18].string)
        player.powerpotential = int(attributes[19].string)
        player.eyeprotential = int(attributes[20].string)
        player.kprotential = int(attributes[21].string)
        player.buntrating = int(attributes[22].string)
        player.buntforhitrating = int(attributes[23].string)
        player.battedballtype = attributes[24].string
        player.groundballtype = attributes[25].string
        player.flyballtype = attributes[26].string
        player.speedrating = int(attributes[27].string)
        player.stealrating = int(attributes[28].string)
        player.baserunningrating = int(attributes[29].string)

        return player

    def create_fielding_record(self, player_parser, import_date):
        attributes = player_parser.find_all('td')
        player = PlayerFielding()

        player.playerid = int(attributes[0].string)
        player.timestamp = import_date
        player.name = attributes[1].string
        player.infieldrange = int(attributes[3].string)
        player.infieldarm = int(attributes[4].string)
        player.turndoubleplay = int(self._convert_unknown(attributes[5].string))
        player.infielderror = int(attributes[6].string)
        player.outfieldrange = int(attributes[7].string)
        player.outfieldarm = int(attributes[8].string)
        player.outfielderror = int(attributes[9].string)
        player.catcherarm = int(attributes[10].string)
        player.catcherability = int(attributes[11].string)
        player.primarydefensiverating = int(self._convert_unknown(attributes[12].string))
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
        attributes = player_parser.find_all('td')
        player = PlayerPitching()
        print(f'name: {attributes[1].string}')

        player.playerid = int(attributes[0].string)
        player.timestamp = import_date
        player.name = attributes[1].string

        player.stuffrating = int(attributes[3].string)
        player.movementrating =  int(attributes[4].string)
        player.controlrating =  int(attributes[5].string)
        player.stuffvleft =  int(attributes[6].string)
        player.movementvleft = 0
        player.controlvleft = 0
        player.stuffvright =  int(attributes[7].string)
        player.movementvright =  int(attributes[8].string)
        player.controlvright =  int(attributes[9].string)
        player.fastballrating =  int(self._convert_unknown(attributes[10].string))
        player.fastballpotential =  int(self._convert_unknown(attributes[11].string))
        player.changeuprating =  int(self._convert_unknown(attributes[12].string))
        player.changeuppotential =  int(self._convert_unknown(attributes[13].string))
        player.curveballrating =  int(self._convert_unknown(attributes[14].string))
        player.curveballpotential =  int(self._convert_unknown(attributes[15].string))
        player.sliderrating =  int(self._convert_unknown(attributes[16].string))
        player.sliderpotential = int(self._convert_unknown(attributes[17].string))
        player.splitterrating = int(self._convert_unknown(attributes[20].string))
        player.splitterpotential = int(self._convert_unknown(attributes[21].string))
        player.sinkerrating = int(self._convert_unknown(attributes[18].string))
        player.sinkerpotential = int(self._convert_unknown(attributes[19].string))
        player.cutterrating = int(self._convert_unknown(attributes[22].string))
        player.cutterpotential = int(self._convert_unknown(attributes[23].string))
        player.forkballrating = int(self._convert_unknown(attributes[24].string))
        player.forkballpotential = int(self._convert_unknown(attributes[25].string))
        player.circlechangerating = int(self._convert_unknown(attributes[26].string))
        player.circlechangepotential = int(self._convert_unknown(attributes[27].string))
        player.screwballrating = int(self._convert_unknown(attributes[28].string))
        player.screwballpotential = int(self._convert_unknown(attributes[29].string))
        player.knucklecurverating = int(self._convert_unknown(attributes[30].string))
        player.knucklecurvepotential = int(self._convert_unknown(attributes[31].string))
        player.knuckleballrating = int(self._convert_unknown(attributes[32].string))
        player.knuckleballpotential = int(self._convert_unknown(attributes[33].string))
        player.numpitches = int(self._convert_unknown(attributes[34].string))
        player.groundballflyball = attributes[35].string
        player.velocity = int(self._convert_unknown(attributes[36].string))
        player.armslot = attributes[35].string
        player.pitchertype = attributes[36].string
        player.stamina = int(attributes[37].string)

        return player
    
    @classmethod
    def _convert_unknown(cls, value):
        if value == '-':
            return "0"
        elif value[0] == "$":
            return value[1:].replace(',', '')
        elif value == 'Free agent':
            return "0"
        else:
            return value.split(" ")[0]

    @classmethod
    def _convert_height(cls, height):
        H_feet = height.split("'")[0]
        H_inch = height.split(" ")[1].split("\"")[0]

        H_inches = int(H_feet) * 12 + int(H_inch)

        return H_inches