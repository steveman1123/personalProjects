import requests,time,re,os

savedir = "./opendirstuff/"
#TODO: crawl reddit for urls labeled for movies
#TODO: put urls' in their own file
urllist = ["https://dl1.3rver.org/",
           "https://dl3.3rver.org/",
           "http://5.135.178.104:10987/",
           "http://37.187.121.54:38946/",
           "http://78.203.154.250/",
           "http://51.158.151.61:8080/",
           #"http://85.218.172.74/" #needs JS
           #"http://ir2.papionvod.ir/Media/", #not available
           #"http://www.moviefyy.com/Film/", #might be dead?
           #"http://103.222.20.150/ftpdata/Movies/", #slow
           "http://167.114.174.132:9092/movies/",
           #"http://192.95.30.30/lol/films/", #empty
           #"http://158.69.224.17:88/", #nerfed
           "http://167.114.174.132:9092/movies/",
           "http://3-152splinter.pulsedmedia.com/public-xyzzy/done/",
           "http://dogjdw.ipdisk.co.kr/public/VOL1/public/movie/",
           "http://92.131.197.89:8000/",
           "http://51.158.151.61:8080/",
           #"http://85.218.172.74/", #needs JS to turn vars into href links - not standard
           "http://23.147.64.113/",
          ]

#recursively get directories and videos from the directories
def getvids(curdir,vidlist):
  print(curdir) #display where we are traversing
  r = requests.get(curdir).text #get the new directory
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
  r = requests.get(u).text #get the base url
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
