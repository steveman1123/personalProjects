import requests,time,re,os

savedir = "./opendirstuff/"
#TODO: crawl reddit for urls labeled for movies
#TODO: put url list in its own file
#TODO: have a timeout if sometime's taking too long

urllist = ("https://dl1.3rver.org/",
           "https://mp4mvz.in/",
           "http://5.135.178.104:10987/",
           "http://37.187.121.54:38946/",
           "https://sv3.hivamovie.com/",
           "http://movie.basnetbd.com/Data/Movies/Hollywood/", #sometimes very slow
           #"http://78.203.154.250/", #connection timeout
           "http://149.202.66.6:8080/",
           "http://ns1.kwiti.net/",
           "https://www.cdn4.dlmvz.ir/",
           "http://51.158.151.61:8080/",
           "http://movie.basnetbd.com/Data/Movies/Hollywood/",
           "http://movie.basnetbd.com/Data/movies1/hollywood/",
           "https://dl2.tarahipro.ir/",
           #"http://85.218.172.74/" #needs JS
           #"http://ir2.papionvod.ir/Media/", #not available
           #"http://www.moviefyy.com/Film/", #might be dead?
           #"http://103.222.20.150/ftpdata/Movies/", #slow
           "http://167.114.174.132:9092/movies/",
           #"http://192.95.30.30/lol/films/", #empty
           #"http://158.69.224.17:88/", #nerfed
           "http://167.114.174.132:9092/movies/",
           #"http://3-152splinter.pulsedmedia.com/public-xyzzy/done/", #timedout
           "http://dogjdw.ipdisk.co.kr/public/VOL1/public/movie/",
           #"http://92.131.197.89:8000/",
           "http://51.158.151.61:8080/",
           #"http://85.218.172.74/", #needs JS to turn vars into href links - not standard
           "http://23.147.64.113/",
           "http://51.15.174.150/torrent/",
           "http://195.154.236.164:48/",
           "http://51.159.53.92/",
           "http://51.15.160.202:8080/",
           "http://163.172.98.148:8081/",
           "http://51.15.142.32:8008/",
           "http://51.15.179.151/",
           "https://dl3.doostihaa.com/Animation/",
           "http://213.58.179.90/media/store/",
           "https://51.178.9.98/",
           "http://91.121.80.14:8080/",
           "https://37.187.117.176:38946/",
           "http://5.39.88.99:18080/",
           "http://62.210.132.17/",
           "http://51.158.153.210/",
           #"https://data1.basedate.workers.dev/movies/",
           "http://195.154.166.82/",
           "https://sv3.hivamovie.com/new/Movie/",
           "http://vod.simpletv.eu/media/storage/",
           "https://dl2.tarahipro.ir/",
           "http://144.137.216.162:8080/Movies/",
           "http://144.137.216.162:8080/TV Shows/",
           "https://zfelleg.useribm.hu/videos/movies/",
           "http://158.69.224.17:88/edmian/",
           "http://212.66.58.15:88/",
           "https://dl3.3rver.org/",
           "http://188.165.227.112/portail/films/",
           )

#recursively get directories and videos from the directories
def getvids(curdir,vidlist,maxTries=1000):
  print(curdir) #display where we are traversing
  tries=0
  while tries<maxTries:
    try:
      r = requests.get(curdir,timeout=10).text #get the new directory
      break
    except Exception:
      print(f"error requesting {curdir}. Trying again...")
      tries+=1
      time.sleep(30)
  time.sleep(0.05) #delay to not overload the server
  linklist = r.split("<a href=\"")[1:] #split by links, trim preceding text
  linklist = [e.split("\">")[0] for e in linklist[1:]] #split second half of the link, remove the parent directory link
  newvids = [curdir+e for e in linklist if e.endswith((".mp4",".mkv",".avi",".m4v","mov","flv","wmv","webv"))] #isolate the video files
  vidlist += newvids #append the new videos to the vidlist
  #if(len(newvids)>0): print("found",len(newvids)) #display how many
  dirlist = [e for e in linklist if e.endswith("/") and not e.startswith(("/","?"))] #isolate the directories
  for d in dirlist:
    getvids(curdir+d,vidlist) #get the videos in each directory


for u in urllist:
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
      getvids(u,vidlist) #get the videos
    
      #save the file
      with open(savedir+savefile,"w") as f:
        f.write("\n".join(vidlist))
        f.close()
