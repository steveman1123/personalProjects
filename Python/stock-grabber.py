#grab stocks and mutual fund latest prices and put into html table
import requests, json
eurl = 'https://api.nasdaq.com/api/quote/' #endpoint url


#TODO: use etrade api to get symbols directly from the account
stocks = ["aal", "amd", "atvi", "cat", "ccl", "cgc", "cost", "csco", "dal", "dg", "enph", "ge", "gm", "hon", "infy", "intc", "jblu", "logi", "luv", "mixt", "msft", "mu", "ndaq", "nio", "nvda", "on", "pfe", "pg", "plnt", "qcom", "sjw", "spce", "syy", "tgt", "ual", "unh", "v", "vtrs", "wec", "wkhs", "wmt", "yeti"]

mfs = ["agthx", "trbcx"]



#return dict of current prices of assets (symblist is list format of symb|assetclass) output of {symb|assetclass:price}
def getPrices(symbList,withVol=False,maxTries=3):
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
  if(withVol):
    prices = {f"{e['symbol']}|{e['assetClass']}":{'price':float(e['lastSalePrice'].replace("$","")),'vol':int(e['volume'].replace(",",""))} for e in d if e['volume'] is not None and e['lastSalePrice'] is not None}
  else:
    prices = {f"{e['symbol']}|{e['assetClass']}":{'price':float(e['lastSalePrice'].replace("$",""))} for e in d if e['lastSalePrice'] is not None}
  return prices


#run stuff
if __name__ == '__main__':
  #write the alpaca current acct value
  with open('alpaca.html','w') as f:
    keys = json.loads(open('../Misc/Tech/Projects/github/stockStuff/apiKeys/steve.txt','r').read())
    acct = json.loads(requests.get(keys['ALPACAURL']+'/v2/account',headers={"APCA-API-KEY-ID":keys['ALPACAKEY'],"APCA-API-SECRET-KEY":keys['ALPACASECRETKEY']},timeout=5).text)
    f.write(f"<table><tbody><tr><td>{acct['portfolio_value']}</td></tr></tbody></table>")


  #write the stocks/mutual funds
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