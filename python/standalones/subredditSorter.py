#find subreddits based on name, description, date created, or number of subs
#TODO: read the csv file and allow user to set filters

import requests, time, os
import pandas as pd


maxTries=3
tries=0
savePath = "../../../"

while tries<maxTries:
  try:
    #get the date of the latest file
    r = requests.get("https://frontpagemetrics.com/list-all-subreddits").text
    date = r.split('width="160">')[1][:10]
    #get the latest csv file
    csvurl = f"https://frontpagemetrics.com/files/{date}.csv"
    #if the file does not exist, pull it down
    if(not os.path.isfile(f"{savePath}{date}.csv")):
      print(f"downloading {date}.csv")
      csvdoc = requests.get(csvurl).text
      open(f"{savePath}{date}.csv",'w', encoding="utf-8").write(csvdoc)
    
    break
  except Exception:
    print(f"connection error. Trying again ({tries+1}/{maxTries})")
    tries+=1
    time.sleep(3)
    continue

#remove subreddits that contain these keywords (remove NSFW ones as much as possible)
nsfwblacklist = ['breast', 'tit', 'onlyfan', 'thot', 'pussy', 'porn', 'ass', 'sex', 'busty', 'gonewild', 'nude', 'slut', 'flashing', 'fucking', 'inappropriate', 'kinky', 'NSFW', 'amateur','nudity']

subs = pd.read_csv(f"{savePath}{date}.csv")

minSubs = int(input("min subscribers: "))
maxSubs = int(input("max subscribers: "))

print(subs)
subs.drop(subs[subs.subs>=maxSubs].index,inplace=True)
print(subs)
subs.drop(subs[minSubs>subs.subs].index,inplace=True)
#TODO: add in nsfw blacklist here (probably using regex in Series.str.contains() )

#subs.sort_values('subs')

print(subs)