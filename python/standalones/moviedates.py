#add dates to movie filenames, get suggestions from wikipedia

import os, re
import wikipediaapi as wapi
import wikipedia as wiki

w = wapi.Wikipedia("movies (example@email.com)","en")

moviedir = "./movies/"

movielist = [e for e in os.listdir(moviedir) if not e.endswith(").mp4") and os.path.isfile(os.path.join(moviedir,e))]

for i,m in enumerate(movielist):
  movietitle = ".".join(m.split(".")[:-1]).replace(" - "," ")

  print()
  print("({}/{}) - {}".format(i+1,len(movielist),m))

  wikisearch = wiki.search(movietitle+" film")
  
  if(len(wikisearch)>0):
    wikipage = w.page(wikisearch[0])
    if(wikipage.exists()):
      dates = re.findall(r"\s(\d{4})\s",wikipage.summary)
      print("suggested dates from wikipedia: ",dates)
  
  date = ""
  while len(date) != 4:
    date = input("release year: ")
  oldname = moviedir+m
  newname = moviedir+movietitle+" ("+date+")."+m.split(".")[-1]

  print("renaming "+oldname+" to "+newname)

  os.rename(oldname,newname)
