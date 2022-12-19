#functions for getting data from the nasdaq api
#directly return json data from the api

#TODO: add comments (explain why things are the way they are)

import requests,json
import datetime as dt
from time import sleep

HEADERS={"user-agent":"-","contact":"github.com/steveman1123"}
BASEURL="https://api.nasdaq.com/api"
VALIDASSETS=["commodities","crypto","currencies","etf","fixedincome","futures","index","mutualfunds","stocks"]

#robust request, standard request but simplified and made more robust
#return request object
def robreq(url,method="get",headers={},params={},maxTries=3,timeout=5):
  tries=0
  while tries<maxTries or maxTries<0:
    try:
      r=requests.request(method,url,headers=headers,params=params,timeout=timeout)
      if(r is not None and len(r.content)>0):
        return r
    except Exception:
      print(f"No connection or other error encountered for {url}")
      print(f"Trying again ({tries+1}/{maxTries})")
      tries+=1
      sleep(3)
      continue
  if(tries>=maxTries):
    print("url:",url)
    print("method:",method)
    print("headers:",headers)
    print("params:",params)
    raise ValueError("Could not get response")

#clean numbers and convert from strings to numerics (remove anything not numeric or "." or "-", but replace "--" with "0")
#where series is a pandas series containing strings with numbers
def cleanNumbers(series,verbose=True):
  try:
    nums = series.str.replace("[^-0-9.]","",regex=True).str.replace("--","0").astype(float)
    return nums
  except Exception:
    #data is not string type
    if(verbose): print("data is not a string type. no changes made")
    return series
    
#get symbol quote info where:
#assetclass: type of asset (commodities|crypto|currencies|fixedincome|futures|index|mutualfunds|stocks)
#symbol: security name (eg MSFT, BTC, EURUSD)
#data: data to return (chart|dividends|eps|extended-trading|historical|info|option-chain|realtime-trades|short-interest|summary)
#fromdate: when getting history, specify the start date (datetime date type)
#todate: when getting histroy, specify the end date (datetime date type)
#offset: when getting history, can offset the number of days (eg if 100 days are requested, and 0-20 are returned, can offset by 20 to get 20-40)
#limit: when getting history, number of days returned per request
#charttype: when getting chart, omit for getting basic asset info (name, last sale price, etc), set to "real" to get volume, price, price close
#markettype: when getting extended-trading, determine if the data should be pre or post market (pre|post)
#return json object
def getQuote(assetclass,
            symb,
            data,
            fromdate=dt.date.today()-dt.timedelta(1),
            todate=dt.date.today(),
            offset=0,
            limit=-1,
            charttype=None,
            markettype="pre"
            ):
  #ensure valid data
  validdata = ["chart","dividends","eps","extended-trading","historical","info","option-chain","realtime-trades","short-interest","summary"]
  if(assetclass not in VALIDASSETS or data not in validdata):
    raise ValueError("Invalid data or asset class specified")
  
  params={"assetclass":assetclass}
  if(data=="historical"):
    if(limit<=0): limit = (todate-fromdate).days
    params.update({"fromdate":str(fromdate),"todate":str(todate),"offset":offset,"limit":limit})
  elif(data=="chart"):
    params.update({"charttype":charttype})
  elif(data=="extended-trading"):
    params.update({"markettype":markettype})
  
  url = f"{BASEURL}/quote/{symb}/{data}"
  r = robreq(url=url,method="get",headers=HEADERS,params=params).json()
  
  return r



#get info for multiple assets
#symbclasslist: list of format ["symb|assetclass",...,"symb|assetclass"]
#type is optional as being set to "Rv" or not (possibly means row/value)
#return json object
def getWatchlist(symbclasslist=[], type=None):
  if(type is not None): type="Rv"
  params={"symbol":symbclasslist}
  url=f"{BASEURL}/quote/watchlist"
  r = robreq(url=url,method="get",headers=HEADERS,params=params).json()
  return r


#get info about specific indicies
#indexlist: list of format ["indexname",indexname",...]
#chartlist: list of format ["indexname",indexname",...]
#return json object
def getIndices(indexlist=None,chartlist=None):
  url=f"{BASEURL}/quote/indices"
  params={}
  if(indexlist is not None): params['symbol']=indexlist
  if(chartlist is not None): params['chartfor']=chartlist
  print(params)
  r = robreq(url=url,method="get",headers=HEADERS,params=params).json()
  return r


#get company info
#symb: company ticker symbol
#data: data about company (company-profile|earnings-surprise|financials|historical-nocp|insider-trades|institutional-holdings|revenue|sec-filings)
#freq: period or quarter endings for financials,? (1|2)
#timeframe: used in historical-nocp (d5|M1||M3|M6|Y1)
#limit: limit number of rows
#type: optional for institutional-holdings (TOTAL|NEW|INCREASED|DECREASED|ACTIVITY|SOLDOUT) and insider-trades (ALL|buys|sells)
#sortColumn: sort column order, optional for institutional-holdings (marketValue|sharesChangePCT|sharesChange|sharesHeld|date|ownerName), insider-trades (lastDate|insider|relation|transactionType|ownType|sharesTraded), sec-filing (filed)
#sortOrder: descending or ascending (DESC|ASC)
#tableOnly: show only the table or not (true|false)
#return json object
def getCompany(symb,
              data,
              freq=None,
              timeframe=None,
              limit=None,
              type=None,
              sortColumn=None,
              sortOrder=None,
              tableOnly=None
              ):
  validdata=["company-profile","earnings-surprise","financials","historical-nocp","insider-trades","institutional-holdings","revenue","sec-filings"]
  validfreq=[1,2],
  validtime=["d5","M1","M3","M6","Y1"]
  url=f"{BASEURL}/company/{symb}/{data}"
  
  if(data not in validdata):
    raise ValueError("invalid data specified")
  
  params={}
  if(freq is not None and freq in validfreq):
    params["frequency"]=freq
  if(data=="historical-nocp"):
    if(timeframe is not None and timeframe in validtime):
      params['timeframe']=timeframe
  if(limit is not None):
    params['limit']=limit
  if(data=="insititutional-holdings"):
    if(type is not None and type in ["TOTAL","NEW","INCREASED","DECREASED","ACTIVITY","SOLDOUT"]):
      params['type']=type
    if(sortColumn is not None and sortColumn in ["marketValue","sharesChangePCT","sharesChange","sharesHeld","date","ownerName"]):
      params['sortColumn']=sortColumn
  elif(data=="insider-trades"):
    if(type is not None and type in ["ALL","buys","sells"]):
      params['type']=type
    if(sortColumn is not None and sortColumn in ["lastDate","insider","relation","transactionType","ownType","sharesTraded"]):
      params['sortColumn']=sortColumn
  if(data=="sec-filings"):
    if(sortColumn is not None):
      params['sortColumn']="filed"
  if(sortOrder is not None and sortOrder in ["DESC","ASC"]):
    params['sortOrder']=sortOrder
  if(tableOnly is not None and tableOnly in ["true","false"]):
    params['tableOnly']=tableOnly
  
  r = robreq(url=url,method="get",headers=HEADERS,params=params).json()
  return r


#get basic info about the NASDAQ market
#return json object
def getMktInfo():
  url=f"{BASEURL}/market-info"
  r=robreq(url=url,method="get",headers=HEADERS).json()
  return r

#get the biggest movers of the specified asset class, or of all available asset classes (stocks|etf|mutualfunds|commodities|futures)
#return json object
def getMovers(assetclass=None):
  url=f"{BASEURL}/marketmovers"
  params={}
  if(assetclass is not None and assetclass in ["stocks","etf","mutualfunds","commodities","futures"]):
    params["assetclass"]=assetclass
  r=robreq(url=url,method="get",headers=HEADERS,params=params).json()
  return r


#get calendar info
#data: the type to get (dividends|earnings|economicevents|splits|upcoming)
#isipo: use the IPO calendar
#date: the specific date to get the data for (yyyy-mm-dd for isipo=False, yyyy-mm for isipo=True)
#type: used only if isipo=True, can be set to SPO
#return json object
def getCalendar(data=None,isipo=False,date=None,type=None):
  if(isipo):
    url=f"{BASEURL}/ipo/calendar"
    #TODO: ensure date is in yyyy-mm format
    if(type is not None): type="spo" #TODO: explore more if this can be other values
    params={"date":date,"type":type}
  else:
    validdata=["dividends","earnings","economicevents","splits","upcoming"]
    if(data not in validdata):
      raise ValueError("Data required if IPO is false")
    url=f"{BASEURL}/calendar/{data}"
    #TODO: ensure date is in yyyy-mm-dd format
    params={"date":date}
    
  r=robreq(url=url,method="get",headers=HEADERS,params=params).json()
  return r

#asset screener

def screen(assetclass,
          tableonly=True,
          offset=50):
  validasset=["etf","index","mutualfunds","stocks"]
  if(assetclass not in validasset):
    raise ValueError("Invalid assetclass specified")
  
  return "function incomplete"
  

#get the analyst data for a specific stock
#symb: stock ticker symbol
#data: analyst data (earnings-date|earnings-forecast|estimate-momentum|peg-ratio|ratings|targetprice)
#return json object
def getAnalyst(symb,data):
  validdata=["earnings-date","earnings-forecast","estimate-momentum","peg-ratio","ratings","targetprice"]
  if(data not in validdata):
    raise ValueError("Invalid data specified")
  url=f"{BASEURL}/analyst/{symb}/{data}"
  r=robreq(url=url,method="get",headers=HEADERS).json()
  return r



#get news headlines and urls for a given asset
#symb: asset symbol
#assetclass: asset class (must be valid)
#offset: offset new articles by this many
#limit: limit the results to this many articles
#return json object
def getNews(symb,assetclass,offset=0,limit=5):
  url=f"{BASEURL}/news/topic/articlebysymbol"
  if(assetclass not in VALIDASSETS):
    raise ValueError("Invalid assetclass specified")
  params={"q":symb+"|"+assetclass,"offset":offset,"limit":limit}
  #TODO: explore other possible parameters
  r=robreq(url=url,method="get",headers=HEADERS,params=params).json()
  return r

