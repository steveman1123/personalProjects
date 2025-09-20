import os
import eyed3
import io
from PIL import Image


directory = "./"

alb = os.path.abspath(directory).split("/")[-1]

img = None
imgpath = directory+"/folder.jpg"
if(os.path.isfile(imgpath)):
  print("folder image present")
  print("ensuring 600x600")
  with Image.open(imgpath) as img:
    img = img.convert("RGB")
    img = img.resize((600,600),Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf,format="JPEG")
    #print(buf.getvalue())



for filename in os.listdir(directory):
  if filename.endswith(".mp3"):
    parts = filename[:-4].split(" - ")
    old_path = os.path.join(directory, filename)

    audio = eyed3.load(old_path)
    if audio.tag is None:
      audio.initTag()
    audio.tag.track_num = parts[0]
    audio.tag.artist = parts[1]
    audio.tag.title = parts[-1]
    audio.tag.album = alb

    if(img is not None):
      print(f"writing img to {filename}")
      with open(imgpath, "rb") as img:
        audio.tag.images.set(3, img.read(), "image/jpeg")
    
    audio.tag.save(version=eyed3.id3.ID3_V2_3)
    audio.tag.save(version=eyed3.id3.ID3_V1_1)

    print(audio.tag.track_num,audio.tag.title)


    new_name = f"{parts[0]} - {parts[-1]}.mp3"
    new_path = os.path.join(directory, new_name)
    print(f"renaming {filename} to {new_name}")
    os.rename(old_path, new_path)
