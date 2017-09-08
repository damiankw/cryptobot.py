# import common
import sys
import os # for changing the folder
os.chdir(os.path.dirname(sys.argv[0]))

# import custom
from boredbot import *


CONFIG = {
  'server': 'irc.austnet.org',
  'port': 6667,
  'nick': 'cryptobot',
  'ident': 'crypto',
  'name': 'a crypto currency bot',
  'cmd': '.'
}

bot = boredbot(CONFIG)
bot.connect()

bot.catch()