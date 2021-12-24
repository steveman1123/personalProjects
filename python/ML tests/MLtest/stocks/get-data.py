#generate data for a given stock that can be put into the input of an ML model
#should be able ot expand into other asset classes (such as currencies, etf, mutualfunds, etc)

import sys
import ndaqfxns as n

if(len(sys.argv)==2):
  symb = sys.argv[1]
else:
  raise ValueError("Must have exactly 1 argument of the stock symbol")


#generate the data file
'''
file should include:
  price history (and volume)
  SR zones
  vpt
  vwap
  dividends
  EMA
  SMA
  sector
  market
  news
  earnings
  p/e ratio
  analyst?
  eps
  calendar (dividends, splits, etc)
  
  
  dependent should be: price > some % over average of last week's
'''
def genData(symb):
  return "function incomplete"