import requests,time,re,os

savedir = "./dirs/"
#TODO: crawl reddit for urls labeled for movies
#TODO: have a timeout if sometime's taking too long

#file containing 1 url per line
urlfile = "./urls.txt"

with open(urlfile,"r") as f:
  urllist = f.read().splitlines()
#remove commented urls
urllist = [e for e in urllist if not e.startswith("#")]

#recursively get directories and videos from the directories
def getvids(curdir,vidlist,maxTries=1000):
  print(curdir) #display where we are traversing
  tries=0
  r = None
  while tries<maxTries:
    try:
      r = requests.get(curdir,timeout=10).text #get the new directory
      break
    except Exception:
      print(f"error requesting {curdir}. Trying again...")
      tries+=1
      time.sleep(30)

  if r is not None:
    time.sleep(0.05) #delay to not overload the server
    linklist = r.split("<a href=\"")[1:] #split by links, trim preceding text
    linklist = [e.split("\">")[0] for e in linklist[1:]] #split second half of the link, remove the parent directory link
    newvids = [curdir+e for e in linklist if e.endswith((".mp4",".mkv",".avi",".m4v","mov","flv","wmv","webv"))] #isolate the video files
    vidlist += newvids #append the new videos to the vidlist
    #if(len(newvids)>0): print("found",len(newvids)) #display how many
    dirlist = [e for e in linklist if e.endswith("/") and not e.startswith(("/","?"))] #isolate the directories
    for d in dirlist:
      getvids(curdir+d,vidlist,maxTries=10) #get the videos in each directory
  else:
    print("exceeded max tries attempting to access {curdir}")


for i,u in enumerate(urllist):
  try:
    print("getting",u)
    r = requests.get(u,timeout=10).text #get the base url
  except Exception:
    r = None

  if(r is not None):
    savefile = re.sub(r'[^\w]*','',u.split("://")[1].split("/")[0].split("?")[0])+".txt" #generate the savefile (trim to alphanumeric only)
    print(f"\n\nsave file: {savedir+savefile}") #display where it's saved
    if(os.path.isfile(savedir+savefile)):
      print("file already exists")
    else:
      vidlist = [] #init the vidlist
      getvids(u,vidlist,maxTries=10) #get the videos
    
      #save the file
      with open(savedir+savefile,"w") as f:
        f.write("\n".join(vidlist))
        f.close()

  else:
    print(f"error getting {u}")
    print("commenting url")
    urllist[i] = "#"+u
    with open(urlfile,"w") as f:
      f.write("\n".join(map(str, urllist)))
      f.close()
