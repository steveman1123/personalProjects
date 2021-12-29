#generate data for a given stock that can be put into the input of an ML model
#should be able ot expand into other asset classes (such as currencies, etf, mutualfunds, etc)

import sys
import ndaqfxns as n
import pricefxns as p
import pandas as pd
import datetime as dt
from workdays import workday as wd

'''
if(len(sys.argv)==2):
  symb = sys.argv[1]
else:
  raise ValueError("Must have exactly 1 argument of the stock symbol")
'''

#generate the data file
#independent values are: historical data (and derivitives), 
#dependent value 1 is t/f price>last week avg
#dependent value 2 is t/f price>yesterday close3
def genData(symb,verbose=True):
  numDays=1000 #appx number of trade days to get the history for (does not account for holidays)
  maxNews = 150 #maximum number of news articles/headlines to pull in
  df_out = pd.DataFrame() #init the output dataframe
  if(verbose):
    print("max number of days to get:",numDays)
    print("max number of news articles:",maxNews)
  
  #price history
  if(verbose): print("getting history")
  fromdate=str(wd(dt.date.today(),-numDays)) #approximate number of trade days ago
  hist = n.getQuote(assetclass="stocks",symb=symb,data="historical",limit=numDays)
  #convert from json to csv
  hist=hist['data']['tradesTable']['rows'] #list of dicts
  # convert to dataframe and convert strings to numbers
  df_hist = pd.DataFrame(hist)
  for e in df_hist:
    if(e!='date'): #do not parse the date
      df_hist[e] = n.cleanNumbers(df_hist[e])
  
  #get historical data (from past, not present or future)
  #dividends, eps, short interest, earnings suprise, finanicials, insider trades, news headlines & related symbols, 
  if(verbose): print("getting dividends")
  divs = n.getQuote(symb=symb,assetclass="stocks",data="dividends")
  df_divs = pd.DataFrame(divs['data']['dividends']['rows'])

  if(verbose): print("getting eps")
  eps = n.getQuote(symb=symb,assetclass="stocks",data="eps")
  df_eps = pd.DataFrame(eps['data']['earningsPerShare'])

  if(verbose): print("getting short interest")
  si = n.getQuote(symb=symb,assetclass="stocks",data="short-interest")
  df_si = pd.DataFrame(si['data']['shortInterestTable']['rows'])

  if(verbose): print("getting earning surprise")
  es = n.getCompany(symb=symb,data="earnings-surprise")
  df_es = pd.DataFrame(es['data']['earningsSurpriseTable']['rows'])

  if(verbose): print("getting financials")
  fin = n.getCompany(symb=symb,data="financials",freq=1)
  if(verbose): print("\tparsing income statement")
  df_incomeStatement = pd.DataFrame(fin['data']['incomeStatementTable']['rows'])
  if(verbose): print("\tparsing balance sheet")
  df_balanceSheet = pd.DataFrame(fin['data']['balanceSheetTable']['rows'])
  if(verbose): print("\tparsing cash flow")
  df_cashFlow = pd.DataFrame(fin['data']['cashFlowTable']['rows'])
  if(verbose): print("\tparsing financial ratios")
  df_finRatios = pd.DataFrame(fin['data']['financialRatiosTable']['rows'])
  
  if(verbose): print("getting insider trades")
  intrades = n.getCompany(symb=symb,data="insider-trades",limit=1) #get the total number of trades
  intrades = n.getCompany(symb=symb,data="insider-trades",limit=int(intrades['data']['transactionTable']['totalRecords'])) #use the total number of trades to request all of them
  df_intrades = pd.DataFrame(intrades['data']['transactionTable']['table']['rows'])
  
  if(verbose): print("getting news")
  news = n.getNews(symb=symb,assetclass="stocks",limit=1)
  news = n.getNews(symb=symb,assetclass="stocks",limit=min(int(news['data']['totalrecords']),maxNews))
  df_news = pd.DataFrame(news['data']['rows'])
  
  if(verbose): print("getting target price history")
  tgtp = n.getAnalyst(symb,"targetprice")
  df_tgtp = pd.DataFrame(tgtp['data']['historicalConsensus'])
  
  #get the nasdax index
  if(verbose): print("getting nasdaq quote")
  ndx = n.getQuote(symb="ndx",assetclass="index",data="historical",limit=numDays) #nasdaq index
  df_ndx = pd.DataFrame(ndx['data']['tradesTable']['rows']) #convert to dataframe
  
  print(df_hist)
  
  #calculate additional columns from historical
  if(verbose): print("calculating vwap")
  vwap = p.vwap(df_hist) #volume weight average price - https://www.investopedia.com/articles/trading/11/trading-with-vwap-mvwap.asp
  if(verbose): print("calculating vpt")
  vpt = p.vpt(df_hist) #volume price trend
  if(verbose): print("calculating ema")
  ema = p.ema(df_hist) #exponential moving average
  if(verbose): print("calculating sma")
  sma = p.sma(df_hist) #simple moving average
  if(verbose): print("calculating delta")
  delta = p.delta(df_hist) #change day over day
  if(verbose): print("calculating obv")
  obv = p.obv(df_hist) #on-balance volume
  
  #combine data into dataframe
  if(verbose): print("cleaning data")
  
  
  if(verbose): print("combining into single dataframe")
  
  
  
  if(verbose): print("done")  
  return df_out
