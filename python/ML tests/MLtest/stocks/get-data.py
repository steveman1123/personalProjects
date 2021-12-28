#generate data for a given stock that can be put into the input of an ML model
#should be able ot expand into other asset classes (such as currencies, etf, mutualfunds, etc)

import sys
import ndaqfxns as n
import pricefxns as p
import pandas as pd
import datetime as dt
from workdays import workday as wd

if(len(sys.argv)==2):
  symb = sys.argv[1]
else:
  raise ValueError("Must have exactly 1 argument of the stock symbol")


#generate the data file
#independent values are: historical data (and derivitives), 
#dependent value 1 is t/f price>last week avg
#dependent value 2 is t/f price>yesterday close3
def genData(symb):
  numDays=1000 #appx number of trade days to get the history for (does not account for holidays)
  maxNews = 150 #maximum number of news articles/headlines to pull in
  df_out = pd.DataFrame() #init the output dataframe
  
  #price history
  fromdate=str(wd(dt.date.today(),-numDays) #approximate number of trade days ago
  hist = n.getQuote(assetclass="stocks",symb=symb,data="historical",limit=numDays)
  #convert from json to csv
  hist=hist['data']['tradesTable']['rows'] #list of dicts
  #convert to dataframe and convert strings to numbers
  df_hist = pd.DataFrame(hist)
  foreach e in df_hist:
    df_hist[e] = n.cleanNumbers(df_hist[e])
  
  #get historical data (from past, not present or future)
  #dividends, eps, short interest, earnings suprise, finanicials, insider trades, news headlines & related symbols, 
  divs = n.getQuote(symb=symb,assetclass="stocks",data="dividends")
  eps = n.getQuote(symb=symb,assetclass="stocks",data="eps")
  si = n.getQuote(symb=symb,assetclass="stocks",data="short-interest")
  
  es = n.getCompany(symb=symb,data="earnings-surprise")
  fin = n.getCompany(symb=symb,data="finanicials",freq=1)
  intrades = n.getCompany(symb=symb,data="insider-trades",limit=1) #get the total number of trades
  intrades = n.getCompany(symb=symb,data="insider-trades",limit=int(intrades['data']['transactionTable']['totalRecords'])) #use the total number of trades to request all of them
  
  news = n.getNews(symb=symb,assetclass="stocks",limit=1)
  news = n.getNews(symb=symb,assetclass="stocks",limit=min(int(news['data']['totalRecords']),maxNews))
  tgtp = n.getAnalyst(symb,"targetprice")
  
  #get the nasdax index
  ndx = n.getQuote(symb="ndx",assetclass="index",data="historical",limit="numDays") #nasdaq index
  df_ndx = pd.DataFrame(ndx['data']['tradesTable']['rows']) #convert to dataframe
  
  #parse data
  df_divs = pd.DataFrame(divs['data']['dividends']['rows'])
  df_eps = pd.DataFrame(eps['data']['earningsPerShare'])
  df_si = pd.DataFrame(si['data']['shortInterestTable']['rows'])
  df_es = pd.DataFrame(es['data']['earningsSurpriseTable']['rows'])
  df_incomeStatement = pd.DataFrame(fin['data']['incomeStatementTable'])
  df_balanceSheet = pd.DataFrame(fin['data']['balanceSheetTable'])
  df_cashFlow = pd.DataFrame(fin['data']['cashFlowTable'])
  df_finRatios = pd.DataFrame(fin['data']['financialRatiosTable'])
  df_intrades = pd.DataFrame(intrades['data']['transactionTable']['table']['rows'])
  df_news = pd.DataFrame(news['data']['rows'])
  
  
  #calculate additional columns from historical
  vwap = p.vwap(df_hist) #volume weight average price - https://www.investopedia.com/articles/trading/11/trading-with-vwap-mvwap.asp
  vpt = p.vpt(df_hist) #volume price trend
  ema = p.ema(df_hist) #exponential moving average
  sma = p.sma(df_hist) #simple moving average
  delta = p.delta(df_hist) #change day over day
  obv = p.obv(df_hist) #on-balance volume
  
  #combine data into dataframe
  
  return "function incomplete"
