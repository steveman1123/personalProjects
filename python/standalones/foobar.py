#interact with the beefweb foobar extension
#docs: https://hyperblast.org/beefweb/api/

import requests, json
from base64 import b64encode

url = 'http://192.168.1.103:8880/api'
usernm = "steve"
pswrd = "steve"
unp = b64encode(bytes(f"{usernm}:{pswrd}","ascii")).decode('ascii')

#add one or more items at a given position
def addItems(items=["https://youtu.be/dQw4w9WgXcQ"], index=0):
  r = requests.post(f"{url}/playlists/0/items/add",params={
  "index":1,
  "items": items
  },
  headers={
  "Content-Type": "application/json", 
  "accept":"application/json",
  "Authorization" : f"Basic {unp}"}, timeout=5)
  return r



def playpause():
  r = requests.post(f"{url}/player/pause/toggle", headers={
  "accept":"application/json",
  "Authorization" : f"Basic {unp}"},timeout=5)
  return r
