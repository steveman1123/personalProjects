#generate data for a given stock that can be put into the input of an ML model
#should be able ot expand into other asset classes (such as currencies, etf, mutualfunds, etc)

import sys
import ndaqfxns as n
import pricefxns as p
import pandas as pd
import numpy as np
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
  numDays=500 #appx number of trade days to get the history for (does not account for holidays)
  fromdate=str(wd(dt.date.today(),-numDays)) #approximate number of trade days ago
  maxNews = 150 #maximum number of news articles/headlines to pull in
  df_out = pd.DataFrame() #init the output dataframe
  if(verbose):
    print("max number of days to get:",numDays)
    print("max number of news articles:",maxNews)
  
  #price history
  if(verbose): print("getting history")
  hist = n.getQuote(assetclass="stocks",symb=symb,data="historical",limit=numDays,fromdate=fromdate)
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
  divs = n.getQuote(symb=symb,assetclass="stocks",data="dividends",limit=50) #limit to the 50 most recent since too far back the data becomes unstable
  df_divs = pd.DataFrame(divs['data']['dividends']['rows'])
  
  '''
  #removed due to redundancy found in earnings surprise
  if(verbose): print("getting eps")
  eps = n.getQuote(symb=symb,assetclass="stocks",data="eps")
  df_eps = pd.DataFrame(eps['data']['earningsPerShare'])
  '''
  
  if(verbose): print("getting short interest")
  si = n.getQuote(symb=symb,assetclass="stocks",data="short-interest")
  df_si = pd.DataFrame(si['data']['shortInterestTable']['rows'])

  if(verbose): print("getting earning surprise")
  es = n.getCompany(symb=symb,data="earnings-surprise")
  df_es = pd.DataFrame(es['data']['earningsSurpriseTable']['rows'])

  if(verbose): print("getting financials")
  fin = n.getCompany(symb=symb,data="financials",freq=1)
  if(verbose): print("\tparsing income statement")
  #generate the income statement with the appropriate headers (and set the index as the header instead of being numeric) and transpose it so there's many columns with dates
  df_incomeStatement = pd.DataFrame(fins['data']['incomeStatementTable']['rows']).rename(columns=fins['data']['incomeStatementTable']['headers']).set_index("Period Ending:").T
  
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
  
  '''
  if(verbose): print("getting news")
  news = n.getNews(symb=symb,assetclass="stocks",limit=1)
  news = n.getNews(symb=symb,assetclass="stocks",limit=min(int(news['data']['totalrecords']),maxNews))
  df_news = pd.DataFrame(news['data']['rows'])
  '''
  
  if(verbose): print("getting target price history")
  tgtp = n.getAnalyst(symb,"targetprice")
  df_tgtp = pd.DataFrame(tgtp['data']['historicalConsensus'])
  
  #get the nasdax index
  if(verbose): print("getting nasdaq quote")
  ndx = n.getQuote(symb="ndx",assetclass="index",data="historical",limit=numDays,fromdate=fromdate) #nasdaq index
  df_ndx = pd.DataFrame(ndx['data']['tradesTable']['rows']) #convert to dataframe
  
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
  
  #prep the data so that it'll fit into the dataframe
  if(verbose): print("cleaning data")
  # hist - baseline (should have the most data points)
  print("hist")
  print(df_hist)
  # divs
  #should transform from cols of exDate,amt,decDate,recDate,pmtDate to 2 cols of amt and divDates where 0=not important, 1=ex,2=dec,3=rec,4=pmt
  #ignore the type col
  print("\ndivs")
  print(df_divs)
  #remove unneeded column
  df_divs.drop(columns='type',inplace=True)
  #change string to number
  df_divs['amount'] = n.cleanNumbers(df_divs['amount'])
  #remove N/A values
  df_divs = df_divs.replace("N/A",np.NaN).dropna()
  #create new dataframe, 1 column of combined date columns
  df_divs = df_divs.melt(id_vars="amount",var_name="datetype",value_name="date").replace({"datetype":{"exOrEffDate":1,"declarationDate":2,"recordDate":3,"paymentDate":4}})
  
  '''
  # eps
  #omit. All useful data can be found in df_es
  print("\neps")
  print(df_eps)
  '''
  # si
  print("\nsi")
  print(df_si)
  #cols should be converted to numeric (date strings to dates)
  df_si['interest'] = n.cleanNumbers(df_si['interest'])
  df_si['avgDailyShareVolume'] = n.cleanNumbers(df_si['avgDailyShareVolume'])
  df_si['daysToCover'] = n.cleanNumbers(df_si['daysToCover'])
  
  # es
  print("\nes")
  print(df_es)
  #rm fiscalQtrEnd col
  df_es.drop(columns="fiscalQtrEnd",inplace=True)
  #ensure cols are numeric (should be already)
  df_es['eps'] = n.cleanNumbers(df_es['eps'])
  df_es['consensusForecast'] = n.cleanNumbers(df_es['consensusForecast'])
  df_es['percentageSurprise'] = n.cleanNumbers(df_es['percentageSurprise'])
  
  # income
  print("\nincome")
  print(df_incomeStatement)
  #rename "Period Ending:" to "date"
  df_incomeStatement.rename({"Period Ending:":"date"})
  for e in df_incomeStatement:
    if(e!="date"): #exclude the date from numeric conversion
      #ensure data is numeric
      df_incomeStatement[e] = n.cleanNumbers(df_incomeStatement[e])
  
  # balance
  #same as income
  print("\nbalance")
  print(df_balanceSheet)
  #rename "Period Ending:" to "date"
  df_balanceSheet.rename({"Period Ending:":"date"})
  for e in df_balanceSheet:
    if(e!="date"): #exclude the date from numeric conversion
      #ensure data is numeric
      df_balanceSheet[e] = n.cleanNumbers(df_balanceSheet[e])

  # cash
  #same as income
  print("\ncash flow")
  print(df_cashFlow)
  #rename "Period Ending:" to "date"
  df_cashFlow.rename({"Period Ending:":"date"})
  for e in df_cashFlow:
    if(e!="date"): #exclude the date from numeric conversion
      #ensure data is numeric
      df_cashFlow[e] = n.cleanNumbers(df_cashFlow[e])

  # ratios
  #same as income
  print("\nratios")
  print(df_finRatios)
  #rename "Period Ending:" to "date"
  df_finRatios.rename({"Period Ending:":"date"})
  for e in df_finRatios:
    if(e!="date"): #exclude the date from numeric conversion
      #ensure data is numeric
      df_finRatios[e] = n.cleanNumbers(df_finRatios[e])

  
  # intrades
  #convert names, relations, xtn type, own type to numeric (based on uniqueness)
  #ensure data is numeric
  print("\nintrades")
  print(df_intrades)
  #rm url col
  df_intrades.drop(columns="url")
  
  
  '''
  # news - omit for now (will have to make a secondary one for sentiment analysis of the headlines)
  #rm url,id,imagedomain,created,image,publisher cols
  #convert ago to date
  print("\nnews")
  print(df_news)
  '''
  # tgtp
  #isolate to z (ignore x & y)
  #add rows to complete to hist
  #added rows of buy/hold/sell should have values of -1
  #TODO: might want to consider experimenting with having the added rows have the previous value (so if 1/1 is 20, then 1/2-1/31 should also be 20 instead of -1)
  #convert consensus to numeric (based on uniquness)
  print("\ntgtp")
  print(df_tgtp)
  # ndx
  #ensure numbers are numeric (also rename cols to differentiate from target asset)
  print("\nndx")
  print(df_ndx)
  
  '''
  #calculated ones should be fine (just be appended to the output)
  # vwap
  print("\nvwap")
  print(vwap)
  # vpt
  print("\nvpt")
  print(vpt)
  # ema
  print("\nema")
  print(ema)
  # sma
  print("\nsma")
  print(sma)
  # delta
  print("\ndelta")
  print(delta)
  # obv
  print("\nobv")
  print(obv)
  '''
  
  #combine data into dataframe
  if(verbose): print("combining into single dataframe")
  df_out = df_hist
  df_out.merge(df_divs,how="outer").fillna(0)
  
  
  #convert date to datetime rather than string
  df_out.date = pd.to_datetime(df_out.date)
  
  if(verbose): print("done")  
  return df_out
