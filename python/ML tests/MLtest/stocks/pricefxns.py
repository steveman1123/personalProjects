#this should contain funtions related to calculating different indicators based on prices and volumes (such as EMA, SMA and VWAP)

import pandas as pd


# https://www.investopedia.com/terms/v/vwap.asp
#calculate the vwap (volume weighted average price)
#given prices is a pandas dataframe containing at the very least open, close, high, low, and volume columns
#where cutoff is the number of periods
def vwap(prices,cutoff=100):
  #calculate average prices
  avgprice = ((prices['High']+prices['Low']+prices['Close/Last'])/3)
  #calculate cumulative avg prices
  cumavg = avgprice.rolling(cutoff).sum()
  #calculate cumulative volume
  cumvol = prices['Volume'].rolling(cutoff).sum()
  #calculate vwap by cumavg/cumvol
  vwap = cumavg/cumvol
  
  return vwap

#simple moving average
#given prices is a pandas dataframe containing at the very least the close column
#length is the number of periods to average over
def sma(prices,length=5):
  sma = prices['Close/Last'].rolling(length).sum()/length
  return sma

#exponential moving average
# https://www.statology.org/exponential-moving-average-pandas/
def ema(prices,length=5):
  ema = prices['Close/Last'].ewm(span=length,adjust=False).mean()
  return ema

#volume price trend
# https://www.investopedia.com/terms/v/vptindicator.asp
# https://www.investopedia.com/ask/answers/030315/what-volume-price-trend-indicator-vpt-formula-and-how-it-calculated.asp
# https://www.daytrading.com/volume-price-trend
# VPT = Previous VPT + Volume x (Today’s Close – Previous Close) / Previous Close
def vpt(prices):
   #multiply volume by the percentage price change between today's close and the previous day's close and then add the result to the previous day's PVT value.
  
  deltaPerc = prices['Volume']*(prices['Close/Last'].diff().div(prices['Close/Last'].shift(1)))
  vpt = deltaPerc.cumsum()
  return vpt

#change in closes
def delta(prices):
  delta = prices['Close/Last'].diff()
  return delta

#on-balance volume
#https://www.investopedia.com/terms/o/onbalancevolume.asp
# https://www.investopedia.com/terms/o/onbalancevolume.asp
def obv(prices):
  obv = prices['Volume']*(prices['Close/Last']>prices['Close/Last'].shift(1)-prices['Close/Last']<prices['Close/Last'].shift(1))
  obv = obv.cumsum()
  return obv



