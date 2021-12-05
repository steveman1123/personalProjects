import json, time, re
#use python 2.7

with open('day04in.txt','r') as f:
  t = f.read()

#format into json
t = t.replace('\n\n','"},{"').replace(':','":"')
t = '[{"'+t.replace('\n','","').replace(' ','","')+'"}]'
t = json.loads(t)

#make sure it has all 8 fields, or if it doesn't, then make sure the only missing field is 'cid'
pt1 = [e for e in t if len(e)==8 or (len(e)==7 and'cid' not in e)]

'''
pt2 make sure the following appy:
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''

pt2 = [e for e in pt1 if (int(e['byr'])>=1920 and int(e['byr'])<=2002)]
pt2 = [e for e in pt2 if (int(e['iyr'])>=2010 and int(e['iyr'])<=2020)]
pt2 = [e for e in pt2 if (int(e['eyr'])>=2020 and int(e['eyr'])<=2030)]
pt2 = [e for e in pt2 if ((int(e['hgt'][:-2])>=150 and int(e['hgt'][:-2])<=193) if e['hgt'][-2:]=='cm' else (int(e['hgt'][:-2])>=59 and int(e['hgt'][:-2])<=76))]
pt2 = [e for e in pt2 if (e['hcl'][0]=="#" and len(re.findall('[0-9a-f]',e['hcl'][1:]))==6)]
pt2 = [e for e in pt2 if re.search('amb|blu|brn|gry|grn|hzl|oth',e['ecl'])]
pt2 = [e for e in pt2 if (e['pid'].isnumeric() and len(e['pid'])==9)]


print len(pt1)
print len(pt2)