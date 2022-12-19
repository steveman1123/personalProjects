#return whether bag of color 'color' contains bag of color 'wantedColor' based on rules defined in 'bagList'
def hasBag(bagList, color, wantedColor, isTop=0):
  if(wantedColor in bagList[color]):
    return True #wanted bag is contained
  elif(' other' in bagList[color]):
    return False #no bags are contained, so nothing to check
  else:
    hasit = False
    for b in bagList[color]: #check every color in the bag
      hasit = hasit or hasBag(bagList, b, wantedColor)
    return hasit

#returns how many total bags are within a givin bag color
def bagsWithin(bagList, color):
  if(' other' in bagList[color]):
    return 0 #no bags held within
  else:
    total = 0 #init the total # of bags within this one
    for b in bagList[color]: #for all the bags in the in the selected bag
      #raw_input(bagList[color]) #display the bag colors
      total += (int(bagsWithin(bagList, b))+1)*int(bagList[color][b]) #multiply the number of bags within each on of those with the number of that bag in the selected bag (add 1 to account for that bag itself)
    return total



with open('day07in.txt','r') as f:
  r = f.read().split('\n')

bagColor = 'shiny gold' #choose the color we want to look at

#convert data into json dict of dicts, format of:
# { color : { colorA: # of bag, colorB: # of bags }}
bags = {}
for e in r: #for every rule
  if len(e)>0: #if there's text
    e = e.replace(' bags','').replace('.','').replace(' bag','') #remove unneeded words
    [holder, held] = e.split(' contain ') #split between bags containing other bags
    bags[holder] = {l[2:]:l[0] for l in held.split(', ')} #set up the dict: split along commas, seperate # of bags into the value of key:value pair (depends on having the # of bags being single digit)


#get the list of bags containing the bagColor ones
pt1 = [e for e in bags if hasBag(bags, e, bagColor,1)]

#count the number of bags within a single bagColor bag
pt2 = bagsWithin(bags, bagColor)

print(len(pt1))
print(pt2)
