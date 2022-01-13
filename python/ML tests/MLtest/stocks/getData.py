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
def getData(symb,verbose=True):
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
  #convert to dataframe
  df_hist = pd.DataFrame(hist['data']['tradesTable']['rows'])
  #convert strings to numbers
  for e in df_hist:
    if(e!='date'): #do not parse the date
      df_hist[e] = n.cleanNumbers(df_hist[e])
  #remove N/A values
  df_hist = df_hist.replace("N/A",np.NaN).dropna()
  
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
  df_incomeStatement = pd.DataFrame(fin['data']['incomeStatementTable']['rows']).rename(columns=fin['data']['incomeStatementTable']['headers']).rename(columns={"Period Ending:":"date"}).set_index("date").T.reset_index().rename(columns={"index":"date"})
  
  if(verbose): print("\tparsing balance sheet")
  df_balanceSheet = pd.DataFrame(fin['data']['balanceSheetTable']['rows']).rename(columns=fin['data']['balanceSheetTable']['headers']).rename(columns={"Period Ending:":"date"}).set_index("date").T.reset_index().rename(columns={"index":"date"})
  
  if(verbose): print("\tparsing cash flow")
  df_cashFlow = pd.DataFrame(fin['data']['cashFlowTable']['rows']).rename(columns=fin['data']['cashFlowTable']['headers']).rename(columns={"Period Ending:":"date"}).set_index("date").T.reset_index().rename(columns={"index":"date"})
  
  if(verbose): print("\tparsing financial ratios")
  df_finRatios = pd.DataFrame(fin['data']['financialRatiosTable']['rows']).rename(columns=fin['data']['financialRatiosTable']['headers']).rename(columns={"Period Ending:":"date"}).set_index("date").T.reset_index().rename(columns={"index":"date"})
  
  '''
  #skipping for now
  if(verbose): print("getting insider trades")
  intrades = n.getCompany(symb=symb,data="insider-trades",limit=1) #get the total number of trades
  intrades = n.getCompany(symb=symb,data="insider-trades",limit=int(intrades['data']['transactionTable']['totalRecords'])) #use the total number of trades to request all of them
  df_intrades = pd.DataFrame(intrades['data']['transactionTable']['table']['rows'])
  '''
  
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
  #convert to dataframe
  df_ndx = pd.DataFrame(ndx['data']['tradesTable']['rows'])
  #convert strings to numbers and rename columns
  for e in df_ndx:
    if(e!='date'): #do not parse the date
      df_ndx[e] = n.cleanNumbers(df_ndx[e])
      df_ndx.rename(columns={e:"ndx-"+e},inplace=True)
  #remove N/A values
  df_ndx = df_ndx.replace("N/A",np.NaN).dropna()
  
  
  #calculate additional columns from historical
  if(verbose): print("calculating vwap5")
  vwap5 = p.vwap(df_hist,length=5) #volume weight average price
  if(verbose): print("calculating vwap20")
  vwap20 = p.vwap(df_hist,length=20) #volume weight average price
  if(verbose): print("calculating vpt")
  vpt = p.vpt(df_hist) #volume price trend
  if(verbose): print("calculating ema5")
  ema5 = p.ema(df_hist,length=5) #exponential moving average
  if(verbose): print("calculating ema20")
  ema20 = p.ema(df_hist,length=20) #exponential moving average
  if(verbose): print("calculating sma5")
  sma5 = p.sma(df_hist,length=5) #simple moving average
  if(verbose): print("calculating sma20")
  sma20 = p.sma(df_hist,length=20) #simple moving average
  if(verbose): print("calculating delta")
  delta = p.delta(df_hist) #change day over day
  if(verbose): print("calculating obv")
  obv = p.obv(df_hist) #on-balance volume
  
  
  #prep the data so that it'll fit into the dataframe
  if(verbose): print("cleaning data")
  
  if(verbose):
    print("\nhist")
    print(df_hist)
  
  # divs
  #should transform from cols of exDate,amt,decDate,recDate,pmtDate to 2 cols of amt and divDates where 0=not important, 1=ex,2=dec,3=rec,4=pmt
  #ignore the type col
  #remove unneeded column
  df_divs.drop(columns='type',inplace=True)
  #change string to number
  df_divs['amount'] = n.cleanNumbers(df_divs['amount'])
  #remove N/A values
  df_divs = df_divs.replace("N/A",np.NaN).dropna()
  #create new dataframe, 1 column of combined date columns, 1 column of date types, 1 column of dividend amount
  df_divs = df_divs.melt(id_vars="amount",var_name="divdatetype",value_name="date").replace({"divdatetype":{"exOrEffDate":1,"declarationDate":2,"recordDate":3,"paymentDate":4}})
  if(verbose):
    print("\ndivs")
    print(df_divs)
  
  '''
  # eps
  #omit. All useful data can be found in df_es
  if(verbose):
    print("\neps")
    print(df_eps)
  '''
  
  # si
  #rename settlementDate to date
  df_si.rename(columns={"settlementDate":"date"},inplace=True)
  #cols should be converted to numeric
  df_si['interest'] = n.cleanNumbers(df_si['interest'])
  df_si['avgDailyShareVolume'] = n.cleanNumbers(df_si['avgDailyShareVolume'])
  #daysToCover is already a float type
  # df_si['daysToCover'] = n.cleanNumbers(df_si['daysToCover'])
  if(verbose):
    print("\nsi")
    print(df_si)
  
  # es
  #rm fiscalQtrEnd col
  df_es.drop(columns="fiscalQtrEnd",inplace=True)
  #ensure cols are numeric (should be already)
  #eps is already a float type
  # df_es['eps'] = n.cleanNumbers(df_es['eps'])
  df_es['consensusForecast'] = n.cleanNumbers(df_es['consensusForecast'])
  df_es['percentageSurprise'] = n.cleanNumbers(df_es['percentageSurprise'])
  #rename dateReported column to date
  df_es.rename(columns={"dateReported":"date"},inplace=True)
  if(verbose):
    print("\nes")
    print(df_es)
  
  # income
  #rename "Period Ending:" to "date"
  df_incomeStatement.rename(columns={"Period Ending:":"date"},inplace=True)
  for e in df_incomeStatement:
    if(e!="date"): #exclude the date from numeric conversion
      #ensure data is numeric
      df_incomeStatement[e] = n.cleanNumbers(df_incomeStatement[e])
  if(verbose):
    print("\nincome")
    print(df_incomeStatement)
  
  # balance
  #rename "Period Ending:" to "date"
  df_balanceSheet.rename(columns={"Period Ending:":"date"},inplace=True)
  for e in df_balanceSheet:
    if(e!="date"): #exclude the date from numeric conversion
      #ensure data is numeric
      df_balanceSheet[e] = n.cleanNumbers(df_balanceSheet[e])
  if(verbose):
    print("\nbalance")
    print(df_balanceSheet)

  # cash
  #rename "Period Ending:" to "date"
  df_cashFlow.rename(columns={"Period Ending:":"date"},inplace=True)
  for e in df_cashFlow:
    if(e!="date"): #exclude the date from numeric conversion
      #ensure data is numeric
      df_cashFlow[e] = n.cleanNumbers(df_cashFlow[e])
  if(verbose):
    print("\ncash flow")
    print(df_cashFlow)

  # ratios
  #rename "Period Ending:" to "date"
  df_finRatios.rename(columns={"Period Ending:":"date"},inplace=True)
  for e in df_finRatios:
    if(e!="date"): #exclude the date from numeric conversion
      #ensure data is numeric
      df_finRatios[e] = n.cleanNumbers(df_finRatios[e])
  if(verbose):
    print("\nratios")
    print(df_finRatios)

  '''
  #skip for now, may come back when we know more
  # intrades
  #convert names, relations, xtn type, own type to numeric (based on uniqueness)
  #rm url col
  df_intrades.drop(columns="url",inplace=True)
  #renme date col for consistency
  df_intrades.rename(columns={"lastDate":"date"},inplace=True)
  #ensure data is numeric
  for c in ["sharesTraded","lastPrice","sharesHeld"]:
    df_intrades[c] = n.cleanNumbers(df_intrades[c])
  if(verbose):
    print("\nintrades")
    print(df_intrades)
  '''
  
  '''
  # news - omit for now (will have to make a secondary one for sentiment analysis of the headlines)
  #rm url,id,imagedomain,created,image,publisher cols
  #convert ago to date
  if(verbose):
    print("\nnews")
    print(df_news)
  '''
  # tgtp
  #isolate to z (ignore x & y) and explode into it's own columns (remove the "latest" column since it's mostly empty)
  df_tgtp = pd.DataFrame(list(df_tgtp['z'])).drop(columns="latest")
  #rename buy/hold/sell to shouldBuy,shouldHold,shouldSell
  df_tgtp.rename(columns={"buy":"shouldBuy","sell":"shouldSell","hold":"shouldHold"},inplace=True)
  #TODO: there may be other values other than these 3, or potentially no data at all. Those cases should be handled (should be based on uniqueness rather than direct translation)
  #convert consensus to numeric  
  df_tgtp['consensus'] = df_tgtp['consensus'].replace({"Buy":"1","Hold":"0","Sell":"-1"}).astype(int)
  if(verbose):
    print("\ntgtp")
    print(df_tgtp)
  
  # ndx
  if(verbose):
    print("\nndx")
    print(df_ndx)
  
  if(verbose):
    #calculated ones should be fine (just be appended to the output)
    # vwap
    print("\nvwap5")
    print(vwap5)
    print("\nvwap20")
    print(vwap20)
    # vpt
    print("\nvpt")
    print(vpt)
    # ema
    print("\nema5")
    print(ema5)
    print("\nema20")
    print(ema20)
    # sma
    print("\nsma5")
    print(sma5)
    print("\nsma20")
    print(sma20)
    # delta
    print("\ndelta")
    print(delta)
    # obv
    print("\nobv")
    print(obv)
  
  #combine data into dataframe
  if(verbose): print("combining into single dataframe")
  df_out = df_hist
  df_out = df_out.merge(df_divs,how="outer")
  df_out = df_out.merge(df_si,how="outer")
  df_out = df_out.merge(df_es,how="outer")
  df_out = df_out.merge(df_incomeStatement,how="outer")
  df_out = df_out.merge(df_balanceSheet,how="outer")
  df_out = df_out.merge(df_cashFlow,how="outer")
  df_out = df_out.merge(df_finRatios,how="outer")
  df_out = df_out.merge(df_tgtp,how="outer")
  df_out = df_out.merge(df_ndx,how="outer")
  df_out['vwap5'] = vwap5
  df_out['vwap20'] = vwap20
  df_out['vpt'] = vpt
  df_out['ema5'] = ema5
  df_out['ema20'] = ema20
  df_out['sma5'] = sma5
  df_out['sma20'] = sma20
  df_out['obv'] = obv
  
  #convert date to datetime rather than string
  df_out.date = pd.to_datetime(df_out.date)
  #replace any NaN's with 0
  # df_out.fillna(0,inplace=True)
  #ensure dates are all consecutive and in chronological order
  df_out.sort_values("date",inplace=True)
  #TODO: ensure without duplicates
  #TODO: ensure data are correct
  
  df_out.to_csv("./"+symb+".csv")
  
  if(verbose): print("done")
  return df_out
