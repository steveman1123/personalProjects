#generate data for a given stock that can be put into the input of an ML model
#should be able ot expand into other asset classes (such as currencies, etf, mutualfunds, etc)

import sys
import ndaqfxns as n
import pandas as pd
import datetime as dt

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
  
  #price history
  numDays=1000
  fromdate=str(dt.date.today()-dt.timedelta(numDays))
  hist = n.getQuote(assetclass="stocks",symb=symb,data="historical",limit=numDays)
  #convert from json to csv
  hist=hist['data']['tradesTable']['rows'] #list of dicts
  #convert to dataframe
  hist = pd.DataFrame(hist)
  
  #earnings, dividends and eps history
  earn = n.getQuote(symb=symb,assetclass="stocks",data="earnings")
  divs = n.getQuote(symb=symb,assetclass="stocks",data="dividends")
  eps = n.getQuote(symb=symb,assetclass="stocks",data="eps")
  
  return "function incomplete"
