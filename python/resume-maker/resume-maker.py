#https://www.geeksforgeeks.org/creating-pdf-documents-with-python/
#https://docs.reportlab.com/reportlab/userguide/ch2_graphics/

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

import datetime as dt
from compskills import compSkills
from math import ceil
import json

skillListFile = "./sample-masterskills.txt" #where my skills are stored (one skill per line)
myinfofile = "./sample-myinfo.json" #where my info is stored (name, contact, education, work, etc)
datadir = "./data/" #where intermediate files should be stored
with open(myinfofile,'r') as f:
  myinfo = json.loads(f.read())
  f.close()

#TODO: ensure first letter of each word is always capitalized
company = myinfo['appinfo']['company']
position = myinfo['appinfo']['position']
positionType = myinfo['appinfo']['positionType'] #full-time||part-time||contractual
isRemote = myinfo['appinfo']['isRemote'] #request a remote position or not

#validate data
if(type(isRemote)!=bool):
  raise ValueError("isRemote must be bool")
if(positionType.lower() not in ['full-time','full time','part-time','part time','contractual','contract']):
  raise ValueError("position type must be full-time, part-time, or contractual")



objectiveStatement = f"Obtain a {positionType.lower()}{' remote' if(isRemote) else ''} position at {company} as a{'n' if(position.lower()[0] in ['a','e','i','o','u']) else ''} {position.lower()}."
print("objective statement:",objectiveStatement)

jobreqs = compSkills(position,skillListFile,savedir=datadir) #get the skills and education requirements for the position
skills = jobreqs['skills']
education = jobreqs['education']

documentTitle = f"{myinfo['name'].lower()} - {company.lower()} - {position.lower()} - {dt.datetime.strftime(dt.datetime.now(),'%Y-%m-%d')}"
fileName = documentTitle+".pdf"




#create pdf object - default page size=A4 - x=595.27, y=841.89
pdf = canvas.Canvas(fileName)
#set document title
pdf.setTitle(documentTitle)
#print(pdf._pagesize) #show the page size

#set position and text vars
centerx = int(pdf._pagesize[0]/2)
centery = int(pdf._pagesize[1]/2)
lmargin = 30
rmargin = pdf._pagesize[0]-lmargin
bmargin = lmargin
tmargin = pdf._pagesize[1]-2*bmargin #not sure why that needs to be x2 to work?
titleFont = "Helvetica"
titleSize = 36
subtitleFont = "Helvetica-Bold"
subtitleSize = 20
textFont = "Helvetica"
textSize = 14
tabWidth = 15
lineheight = 25


#register external fonts as needed
#pdfmetrics.registerFont(TTFont('nasa-font', 'c:/Windows/Fonts/nasalization-rg.ttf'))



#set the title (my name)
pdf.setFont(titleFont, titleSize)
pdf.drawCentredString(centerx, tmargin, myinfo['name'])

#print the contact section
pdf.setFont(textFont,textSize)
contacty = tmargin-titleSize
pdf.drawString(lmargin,contacty,myinfo['email'])
pdf.drawCentredString(centerx,contacty,myinfo['phone'])
pdf.drawRightString(rmargin,contacty,myinfo['website'])


#line
liney = contacty-lineheight
pdf.line(lmargin, liney, rmargin, liney)


#objective statement
pdf.setFont(subtitleFont,subtitleSize)
pdf.drawString(lmargin+tabWidth,liney-lineheight,"Objective")
pdf.setFont(textFont,textSize)
pdf.drawString(lmargin+tabWidth,liney-lineheight*2,objectiveStatement)


#line
liney = int(liney-3*lineheight)
pdf.line(lmargin, liney, rmargin, liney)


#relevant skills
pdf.setFont(subtitleFont,subtitleSize)
pdf.drawString(lmargin+tabWidth,liney-lineheight,"Relevant Skills")
pdf.setFont(textFont,textSize)

#print the first column
text = pdf.beginText(lmargin+tabWidth, liney-lineheight*2)
text.setFont(textFont, textSize)
text.setLeading(20)
for s in skills[:ceil(len(skills)/2)]:
  text.textLine(s[1].capitalize())
pdf.drawText(text)

#print the second column
text = pdf.beginText(centerx+tabWidth, liney-lineheight*2)
text.setFont(textFont, textSize)
text.setLeading(20)
for s in skills[ceil(len(skills)/2):]:
  text.textLine(s[1].capitalize())
pdf.drawText(text)



#line
liney = int(liney-ceil(len(skills)/2+(len(skills)+1)%2)*lineheight) #TODO: dynamically set the y position better (this mostly works, but not 100%
pdf.line(lmargin, liney, rmargin, liney)


#work history
pdf.setFont(subtitleFont,subtitleSize)
pdf.drawString(lmargin+tabWidth,liney-lineheight,"Work History")
pdf.setFont(textFont,textSize)

for i,w in enumerate(myinfo['workhistory']):
  pdf.drawString(lmargin+tabWidth,liney-(i+2)*lineheight,w['company'])
  pdf.drawCentredString(centerx+tabWidth,liney-(i+2)*lineheight,w['title'])
  pdf.drawRightString(rmargin-tabWidth,liney-(i+2)*lineheight,w['time'])
  

#line
liney = int(liney-(len(myinfo['workhistory'])+2)*lineheight)
pdf.line(lmargin, liney, rmargin, liney)


#education
pdf.setFont(subtitleFont,subtitleSize)
pdf.drawString(lmargin+tabWidth,liney-lineheight,"Education")
pdf.setFont(textFont,textSize)

for i,e in enumerate(myinfo['eduhist']):
  #only show the relavant education
  if(e['degree'].lower().replace("'","") in jobreqs['education']):
      pdf.drawString(lmargin+tabWidth,liney-(i+2)*lineheight,e['degree'])
      pdf.drawCentredString(centerx,liney-(i+2)*lineheight,e['institute'])
      if('focus' in e):
        pdf.drawRightString(rmargin-tabWidth,liney-(i+2)*lineheight,e['focus'])


#line
liney = int(liney-(len(myinfo['eduhist'])+2)*lineheight)
pdf.line(lmargin, liney, rmargin, liney)


#references
pdf.setFont(subtitleFont,subtitleSize)
pdf.drawString(lmargin+tabWidth,liney-lineheight,"References")
pdf.setFont(textFont,textSize)

for i,r in enumerate(myinfo['references']):
  pdf.drawString(lmargin+tabWidth,liney-(i+2)*lineheight,r)
  pdf.drawRightString(rmargin-tabWidth,liney-(i+2)*lineheight,myinfo['references'][r])



#end the first page
pdf.showPage()
print("first page done")







#second page - generate projects
print("second page")

#show name and contact info again
pdf.setFont(titleFont, titleSize)
pdf.drawCentredString(centerx, tmargin, myinfo['name'])

#print the contact section
pdf.setFont(textFont,textSize)
contacty = tmargin-titleSize
pdf.drawString(lmargin,contacty,myinfo['email'])
pdf.drawCentredString(centerx,contacty,myinfo['phone'])
pdf.drawRightString(rmargin,contacty,myinfo['website'])


#line
liney = contacty-lineheight
pdf.line(lmargin, liney, rmargin, liney)


#projects section
#TODO: set to be full HW, full SW, or mixed
pdf.setFont(subtitleFont,subtitleSize)
pdf.drawString(lmargin+tabWidth,liney-lineheight,"Projects")
pdf.setFont(textFont,textSize)
pdf.drawString(lmargin+tabWidth, liney-2*lineheight,"Test Robot")
pdf.drawString(lmargin+tabWidth, liney-5*lineheight,"Aluminum Air Battery")
pdf.drawString(lmargin+tabWidth, liney-8*lineheight,"Automated Resume Generator")


pdf.drawCentredString(centerx,bmargin,"more projects can be found on my website")


  
# saving the pdf
pdf.save()

print("done")