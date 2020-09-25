from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

class OOTPParser():

    def parse_player_file(self, playerfile):
        parser = BeautifulSoup(playerfile, 'lxml')

        player_table = parser.body.table.table
        players = player_table.find_all('tr')[1:10]
        for player in players:
            attributes = player.find_all('td')
            print(f'name: {attributes[2].string}')