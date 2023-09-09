import requests,os
from fuzzywuzzy import fuzz

#compare the technical skills needed for a given position with a list of a person's skills
#position = string of the type of job eg "software engineer" or "landlord" or ""secondary school teacher"
#skillListFile = a file that contains 
#top n positions to loook at/compare to the requested position
def compSkills(position,skillListFile,savedir="./",npos=3):
  savefile = position+".html"
  reqs = {} #output data (skills, education, ...) - TODO: add in credentials

  print(f"searching for similar positions to {position}")
  if(os.path.isfile(savedir+savefile)):
    with open(savedir+savefile,'r') as f:
      r = f.read()
      f.close()
  else:
    r = requests.get(f"https://www.onetonline.org/find/result?s={position}").text
    with open(savedir+savefile,'w') as f:
      f.write(r)
      f.close()
    
  print("isolating similar positions")
  r = "".join(r.split("<tr")[:npos+2])
  #print(r)
  codes = r.split('data-title="Code">')
  codes = [e.split("</td")[0] for e in codes][1:]
  positions = r.split('data-text="')
  positions = [e.split('"')[0] for e in positions][1:]

  #similar positions
  simpos = [[codes[i],positions[i]] for i in range(len(codes))]



  #request each similar positions
  skills = []
  for i,s in enumerate(simpos):
    if(os.path.isfile(savedir+s[0]+".html")):
      with open(savedir+s[0]+".html",'r') as f:
        r = f.read()
        f.close()
    else:
      r = requests.get(f"https://www.onetonline.org/link/summary/{s[0]}").text
      with open(savedir+s[0]+".html",'w') as f:
        f.write(r)
        f.close()
    
    if(i==0):
      print(f"getting education requirements for {s[1]} - closest match to position")
      
      #get the education requirement
      education = r.split('id="JobZone"')[1].split("</div")[0].lower()
      if("master's" in education):
        reqs['education'] = 'masters/bachelors/associates/vocational/high school/ged'
      elif("bachelor's" in education):
        reqs['education'] = 'bachelors/associates/vocational/high school/ged'
      elif("associates's" in education):
        reqs['education'] = 'associates/vocational/high school/ged'
      elif("vocational" in education):
        reqs['education'] = 'vocational/high school/ged'
      elif("high school" in education):
        reqs['education'] = 'high school/ged'
      else:
        reqs['education'] = []
      print("education required:",reqs['education'])
    
    print(f"getting skills for {s[1]}")
    if('section_TechnologySkills' in r):
      techskills = r.split('section_TechnologySkills')[1].split("</ul")[0]
      techskills = techskills.split('<b>')[1:]
      skills += [e.split("</b>")[0].lower() for e in techskills]
    else:
      print("no technical skills listed. TODO: incorporate activities and tasks")
      
    
  skills = set(skills)
  #print(skills)
  print(f"{len(skills)} skills found for {len(simpos)} similar positions to {position}")

  #load my skills
  print("loading person's skills")
  with open(skillListFile,'r') as f:
    myskills = f.read()
    myskills = myskills.replace("\r\n","\n").split("\n")
    f.close()

  matchedskills = []
  print("comparing similar skills")
  for mine in myskills:
    for skill in skills:
      if(fuzz.ratio(mine.lower(),skill)>=79):
        matchedskills+=[(mine.lower(),skill)]
  
  reqs['skills'] = list(set(matchedskills)) #remove duplicates
  print(f"matched skills - {len(reqs['skills'])}")
  
  return reqs



#compSkills("Software Engineer","./masterskills.txt")


