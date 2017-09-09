# import common
import sys
import os # for changing the folder
os.chdir(os.path.dirname(sys.argv[0]))

# import custom
from cryptobot import *


CONFIG = {
  'server': 'irc.austnet.org',
  'port': 6667,
  'nickserv': 'NickOP',
  'nickpass': 'TvemxLYKBYA23xwB',
  'channels': {
    '#nictitate',
    '#nerdhacks'
  },
  'nick': 'cryptobot',
  'ident': 'crypto',
  'name': 'a crypto currency bot',
  'cmd': '.',
}

bot = cryptobot(CONFIG)
bot.connect()

bot.catch()