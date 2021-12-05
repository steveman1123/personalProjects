#grab quotes from various avatar: the last airbender characters

import requests, re, json, os
from bs4 import BeautifulSoup as bs

def getEpiLinks():
  url = 'http://atla.avatarspirit.net/transcripts.php'
  try:
    r = requests.get(url).text
    soup = bs(r, 'html.parser')
    table = soup.find_all('table')[1]
    return [e.get('href') for e in table.find_all('a') if e.get('href') != None]
  except Exception:
    return []

#get all quotes from a character given their name and the url of the episode
def getEpiQuotes(name, url):
  r = requests.get(url).text.split('\r<br>') #split by linebreaks
  tmp = [e[9+len(name):] for e in r if (e.lower()).startswith(f'<b>{name.lower()}</b>: ')] #trim off the first bit
  quotes = [re.sub('  ',' ',re.sub('<i>.+</i>|\(.+\)','',e)).strip() for e in tmp] #remove italicized/parens actions, double spaces & leading/trailing spaces
  return quotes

#get all quotes from a given character
def getQuotes(name, fileName=""):
  if(fileName==""):
    fileName = f".\{name}.json"
  if(not os.path.isfile(fileName)): #if file doesn't exist, then get it from the internet
    l = getEpiLinks()
    q = []
    for e in l:
      q += getEpiQuotes(name,e)
    
    with open(fileName,'w') as f: #write to a json file
      f.write(json.dumps(q))
      
  else: #file does exist, so read from that instead
    with open(fileName,'r') as f:
      q = json.loads(f.read())

  return q