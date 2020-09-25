from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

class OOTPParser():

    def parse_player_file(self, playerfile):
        parser = BeautifulSoup(playerfile, 'lxml')
        print(parser.head)