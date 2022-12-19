import json

jsonFile = open("./lights.txt","r")
jStr = str(jsonFile.read())
#print(jStr)

j = json.loads(jStr)
print(j[0])