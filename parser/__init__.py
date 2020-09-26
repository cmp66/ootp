from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from db import Player
import datetime

class OOTPParser():

    def parse_player_file(self, playerfile):
        parser = BeautifulSoup(playerfile, 'lxml')
        parsed_players = []

        player_table = parser.body.table.table
        players = player_table.find_all('tr')[1:]
        for player in players:
            parsed_players.append(self.create_player_record(player))

        return parsed_players

    def create_player_record(self, player_parser):
        attributes = player_parser.find_all('td')
        print(f'name: {attributes[2].string}')
        player = Player()
        player.id = int(attributes[0].string)
        player.position = attributes[1].string
        player.name = attributes[2].string
        player.team = attributes[3].string
        player.org = attributes[4].string
        player.league = attributes[5].string
        player.level = attributes[6].string
        player.dob = datetime.datetime.strptime(attributes[7].string, '%m/%d/%Y')
        player.age = attributes[8].string
        player.height = attributes[9].string
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