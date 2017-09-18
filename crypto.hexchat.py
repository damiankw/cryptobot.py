__module_name__ = "cryptoPuller"
__module_version__ = "0.0a"
__module_description__ = "Adds /crypto to pull crypto currency list prices."

import hexchat
import string
import json
import urllib.request

#import time
#import re
#import threading
#import traceback
#import logging
#import importlib
#from imp import reload

def alias_crypto(word, word_eol, userdata):
  if (len(word_eol) > 1):
    text = word_eol[1]
  else:
    text = ''
  cur_list = {"AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"}
  cur = None
  cry = None
  for arg in text.split(' '):
    if (arg == ''):
      continue
    elif (arg[0] == '-'):
      #this is a -CUR
      if arg[1:].upper() in cur_list:
        cur = arg[1:].upper()
    else:
      #this is a CRY
      cry = arg

  if (cur == None):
    cur = 'AUD'

  if (cry == None):
    items = get_crypto(cur)
    head = 'Top 15 list of cryptocies'
  else:
    items = get_crypto(cur, 1, cry)
    head = 'Current list price of %s' % cry

  if (items == None):
    print("Unable to process request, unable to find bitcoin currency.")
  else:
    print("*** %s (%s) ***" % (head, cur))
    print("\x16SYM    NAME                MARKET CAP         PRICE(%s)              SUPPLY     1HR      1D      7D\x16" % cur)
    for item in items:
      print("{0:6} {1:19} ${2:16,.0f}  $ {3:11,.4f} {4:16,.0f}  {5:6}  {6:6}  {7:6}".format(item['symbol'], item['name'], float(item['market_cap_' + cur.lower()]), float(item['price_' + cur.lower()]), float(item['total_supply']), float(item['percent_change_1h']), float(item['percent_change_24h']), float(item['percent_change_7d'])))
    print("*** End of List ***")
    
  return hexchat.EAT_ALL

def get_crypto(cur="AUD", limit=15, cry=None):

  if (cry == None):
    http = urllib.request.urlopen('https://api.coinmarketcap.com/v1/ticker/?convert=%s&limit=%s' % (cur, limit))
    html = http.read().decode('utf-8')
    items = json.loads(html)

    return items
  else:
    try:
      http = urllib.request.urlopen('https://api.coinmarketcap.com/v1/ticker/%s/?convert=%s' % (cry, cur))
      html = http.read().decode('utf-8')
      items = json.loads(html)
    except urllib.request.HTTPError as err:
      return None

    return items

hexchat.hook_command('crypto', alias_crypto, help="/CRYPTO [<-CURRENCY> <CRYPTO NAME>]")