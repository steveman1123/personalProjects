#grab stocks and mutual fund latest prices and put into html table
import requests, json
eurl = 'https://api.nasdaq.com/api/quote/' #endpoint url


#choose the securities that should be queried
stocks = ["aapl","msft","nvda"]
mfs = ["agthx"]



#return dict of current prices of assets (symblist is list format of symb|assetclass) output of {symb|assetclass:price}
def getPrices(symbList,maxTries=3):
  maxSymbs = 20 #cannot do more than 20 at a time, so loop through requests
  d = [] #init data var
  r = {}
  #loop through the symbols by breaking them into managable chunks for th api
  for i in range(0,len(symbList),maxSymbs):
    tries=0
    while tries<maxTries:
      try: #try getting the data
        r = json.loads(requests.get("https://api.nasdaq.com/api/quote/watchlist",params={'symbol':symbList[i:min(i+maxSymbs,len(symbList))]},headers={'user-agent':'-'},timeout=5).text)
        break
      except Exception: #if it doesn't work, try again
        print("Error getting prices. Trying again...")
        r['data'] = [] #if something fails, then set it to nothin in the event it completely fails out (this way it won't throw an error when trying to extend)
        tries+=1
        time.sleep(3)
        continue
    d.extend(r['data']) #append the lists

  #isolate the symbols and prices and remove any that are none's
  prices = {f"{e['symbol']}|{e['assetClass']}":{'price':float(e['lastSalePrice'].replace("$",""))} for e in d if e['lastSalePrice'] is not None}

  return prices


if __name__ == '__main__':

  #write the stocks/mutual funds to an html table style file so it can easily be loaded into openoffice calc
  stocks = [e+"|stocks" for e in stocks]
  mfs = [e+"|mutualfunds" for e in mfs]

  prices = getPrices(sorted(stocks+mfs))
  with open("stocks.html","w") as f:
    f.write("<table><tbody>")
    for i,e in enumerate(prices):
      print(f"({i+1}/{len(prices)})\t- {e.split('|')[0]}\t- {prices[e]['price']}")
      f.write(f"<tr><td>{e.split('|')[0]}</td><td>{prices[e]['price']}</td></tr>")
    f.write("</table></tbody>")

  print("Done")
